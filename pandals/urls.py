from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('map/', views.map_view, name='map'),
    path('logout/', views.logout_view, name='logout'),
    path('api/pandals/', views.pandal_list, name='pandal_list'),
    path('favourite/<int:pid>/', views.toggle_favourite, name='toggle_favourite'),
    path("get-reviews/<int:pid>/", views.get_reviews, name="get_reviews"),
    path("my-reviews/", views.my_reviews, name="my_reviews"),
    path("delete-review/<int:rid>/", views.delete_review, name="delete_review"),
    path("submit-review/<int:pid>/", views.submit_review, name="submit_review"),
    path("edit-review/<int:rid>/", views.edit_review, name="edit_review"),
    path("submit-crowd/", views.submit_crowd, name="submit_crowd"),
    # Chatbot API
    path("chatbot/ask/", views.chatbot_reply, name="chatbot_reply"),
    path("chat/history/", views.load_chat_history, name="chat_history"),
]

