from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Avg, Count
import json
from .models import Pandal, Favourite, Review, CrowdLevel
from .utils.chatbot import pandel_chatbot
import re
from .models import ChatMessage





# ================= HOME =================
def home(request):
    return render(request, 'pandals/home.html')


# ================= REGISTER =================
def register(request):
    if request.method == "POST":

        username = request.POST.get("username","")
        username = " ".join(username.split())   #  space fix

        email = request.POST.get("email","")
        password = request.POST.get("password","")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'pandals/register.html')


# ================= LOGIN =================
def login_view(request):
    if request.method == "POST":

        username = request.POST.get("username","")
        username = " ".join(username.split())   #  space fix

        password = request.POST.get("password","")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)

            #  24 hour session
            request.session.set_expiry(86400)

            return redirect('dashboard')
        else:
            return render(request, 'pandals/login.html', {'error': 'Invalid credentials'})

    return render(request, 'pandals/login.html')


# ================= LOGOUT =================
def logout_view(request):
    logout(request)
    request.session.flush()   #  full session clear
    return redirect('home')


# ================= BEST TIME =================
def get_best_time(pandal):
    qs = CrowdLevel.objects.filter(pandal=pandal).exclude(time_slot="Unknown")

    best = qs.values("time_slot").annotate(total=Count("time_slot")).order_by("-total").first()

    if best:
        return best["time_slot"]
    return "No data"


# ================= TOP RATED =================
def get_top_rated_pandals():
    rating_data = Review.objects.values('pandal').annotate(avg_rating=Avg('rating'))

    crowd_data = CrowdLevel.objects.values('pandal','level') \
        .annotate(c=Count('id')).order_by('pandal','-c')

    time_data = CrowdLevel.objects.exclude(time_slot="Unknown") \
        .values('pandal','time_slot') \
        .annotate(c=Count('id')).order_by('pandal','-c')

    result = {}

    for r in rating_data:
        result[r['pandal']] = {
            "rating": round(r['avg_rating'],2),
            "crowd": None,
            "time": None
        }

    for c in crowd_data:
        if c['pandal'] in result and result[c['pandal']]['crowd'] is None:
            result[c['pandal']]['crowd'] = c['level']

    for t in time_data:
        if t['pandal'] in result and result[t['pandal']]['time'] is None:
            result[t['pandal']]['time'] = t['time_slot']

    return sorted(result.items(), key=lambda x: x[1]['rating'], reverse=True)[:3]


# ================= DASHBOARD =================
@login_required(login_url='login')
def dashboard(request):

    total = Pandal.objects.count()
    top_rated = get_top_rated_pandals()

    favs = Favourite.objects.filter(user=request.user).select_related("pandal")

    fav_data = []
    for f in favs:
        fav_data.append({
            "pandal": f.pandal,
            "best_time": get_best_time(f.pandal)
        })

    top_data = []
    for pid, info in top_rated:
        p = Pandal.objects.get(id=pid)
        top_data.append({
            "name": p.name,
            "rating": info["rating"],
            "crowd": info["crowd"],
            "time": info["time"]
        })

    return render(request, 'pandals/dashboard.html', {
        'total_pandals': total,
        'top_pandals': top_data,
        'fav_data': fav_data,
        'fav_count': favs.count()
    })


# ================= MAP =================
@login_required(login_url='login')
def map_view(request):
    return render(request, 'pandals/map.html')


# ================= PANDAL LIST API =================
@login_required(login_url='login')
def pandal_list(request):
    pandals = Pandal.objects.all()
    data = []

    for p in pandals:
        counts = CrowdLevel.objects.filter(pandal=p).values("level").annotate(total=Count("level"))

        crowd = {"low":0,"medium":0,"high":0}
        for c in counts:
            if c["level"] in crowd:
                crowd[c["level"]] = c["total"]

        if crowd["low"] >= crowd["medium"] and crowd["low"] >= crowd["high"]:
            final = "low"
        elif crowd["medium"] >= crowd["low"] and crowd["medium"] >= crowd["high"]:
            final = "medium"
        else:
            final = "high"

        data.append({
    "id":p.id,
    "name":p.name,
    "area":p.area,
    "theme":p.theme,
    "rating":p.rating,
    "latitude":p.latitude,
    "longitude":p.longitude,

    "crowd_low": crowd["low"],
    "crowd_medium": crowd["medium"],
    "crowd_high": crowd["high"],

    "crowd": final,
    "best_time": get_best_time(p)
})


    return JsonResponse(data, safe=False)


# ================= FAVOURITE =================
@login_required
def toggle_favourite(request, pid):
    fav = Favourite.objects.filter(user=request.user, pandal_id=pid)

    if fav.exists():
        fav.delete()
        return JsonResponse({"status":"removed"})
    else:
        Favourite.objects.create(user=request.user, pandal_id=pid)
        return JsonResponse({"status":"added"})


# ================= REVIEW =================
@csrf_exempt
@login_required
def submit_review(request, pid):
    data = json.loads(request.body)
    pandal = Pandal.objects.get(id=pid)

    Review.objects.update_or_create(
        user=request.user,
        pandal=pandal,
        defaults={
            "rating": data["rating"],
            "comment": data["comment"]
        }
    )

    avg = Review.objects.filter(pandal=pandal).aggregate(Avg("rating"))["rating__avg"]
    pandal.rating = round(avg,1)
    pandal.save()

    return JsonResponse({"msg":"Review saved"})

# ================= MY REVIEWS =================
@login_required
def my_reviews(request):
    reviews = Review.objects.filter(user=request.user).select_related("pandal")
    return render(request, "pandals/my_reviews.html", {"reviews":reviews})

# ================= REVIEW =================
@login_required
def delete_review(request, rid):
    review = Review.objects.get(id=rid, user=request.user)
    pandal = review.pandal
    review.delete()

    avg = Review.objects.filter(pandal=pandal).aggregate(Avg("rating"))["rating__avg"]
    pandal.rating = round(avg,1) if avg else 0
    pandal.save()

    return redirect("my_reviews")


# ================= CROWD =================
@login_required
def submit_crowd(request):
    CrowdLevel.objects.update_or_create(
        user=request.user,
        pandal_id=request.POST.get("pandal_id"),
        defaults={
            "level": request.POST.get("level"),
            "time_slot": request.POST.get("time_slot")
        }
    )
    return JsonResponse({"status": "success"})

# ================= REVIEWS =================
def get_reviews(request, pid):
    reviews = Review.objects.filter(pandal_id=pid).select_related("user")
    data = []

    for r in reviews:
        data.append({
            "user": r.user.username,
            "rating": r.rating,
            "comment": r.comment
        })

    return JsonResponse(data, safe=False)

# ================= EDIT REVIEW =================
@csrf_exempt
@login_required
def edit_review(request, rid):
    data = json.loads(request.body)

    r = Review.objects.get(id=rid, user=request.user)

    r.rating = data["rating"]
    r.comment = data["comment"]
    r.save()

    avg = Review.objects.filter(pandal=r.pandal).aggregate(Avg("rating"))["rating__avg"]
    r.pandal.rating = round(avg,1)
    r.pandal.save()

    return JsonResponse({"msg":"Review updated"})


# ================= CHATBOT =================
@csrf_exempt
def chatbot_reply(request):

    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    if not request.user.is_authenticated:
        return JsonResponse({"error": "Login required"}, status=401)

    data = json.loads(request.body)
    msg = data.get("message", "")

    ai_reply = pandel_chatbot(msg)

    # Button detect
    show_button = "[SHOW_BUTTON]" in ai_reply

    # Destination extract
    dest = None
    match = re.search(r"\[DEST:(.*?)\]", ai_reply)
    if match:
        dest = match.group(1).strip()

    # Clean reply text
    clean_reply = ai_reply.replace("[SHOW_BUTTON]", "")
    clean_reply = re.sub(r"\[DEST:.*?\]", "", clean_reply)

    # 🔥 BACKEND VALIDATION
    from pandals.models import Pandal

    valid_pandal = None
    if dest:
        valid_pandal = Pandal.objects.filter(name__icontains=dest).first()

    if dest and not valid_pandal:
        clean_reply = "Ei naam er kono pandal paini 😕 Ektu thik naam diye try koro."
        show_button = False
        dest = None

    if valid_pandal:
        dest = valid_pandal.name   # exact DB name fix

    # Fallback if empty
    if not clean_reply.strip():
        clean_reply = "Pujo vibe e full energy 😄 Tumi kon pandal niye jante chao?"

    # SAVE USER MSG
    ChatMessage.objects.create(
        user=request.user,
        message=msg,
        sender="user"
    )

    # SAVE BOT MSG
    ChatMessage.objects.create(
        user=request.user,
        message=clean_reply.strip(),
        sender="bot"
    )

    return JsonResponse({
        "reply": clean_reply.strip(),
        "button": show_button,
        "destination": dest
    })

@login_required
def load_chat_history(request):
    chats = ChatMessage.objects.filter(user=request.user).order_by("created_at")

    return JsonResponse([
        {"message": c.message, "sender": c.sender}
        for c in chats
    ], safe=False)