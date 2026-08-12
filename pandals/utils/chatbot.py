from openai import OpenAI
from django.conf import settings


client = OpenAI(
    api_key=settings.OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)


def pandel_chatbot(user_msg):

    system_prompt = """
You are PANDEL GO chatbot.

Rules:

1. If user writes in Bengali, reply in Bengali.
2. If user writes in English, reply in English.
3. Your tone is friendly.
4. You talk only about pandals, food, and culture.

------------------------------------------------
NAVIGATION RULE
------------------------------------------------
ONLY add navigation button when user clearly wants to GO to a pandal.

Navigation intent examples:
- "take me to"
- "go to"
- "going to"
- "আমাকে ... যেতে হবে"
- "প্যান্ডেল যেতে চাই"
- "আমি ... যেতে চাই"
- "... pandel jete chai"

------------------------------------------------
NAVIGATION RESPONSE FORMAT (STRICT)
------------------------------------------------
When navigation intent is detected, reply ONLY in this exact format:

Taking you to <Pandal Name>. [DEST:<Pandal Name>] [SHOW_BUTTON]

Rules:
- Do NOT add any extra sentence.
- Do NOT add Bengali translation.
- Do NOT add emoji.
- Do NOT add description.
- Only this single line.

------------------------------------------------
INFORMATION RULE
------------------------------------------------
If user only asks for information, DO NOT add navigation button.

------------------------------------------------
VISIBILITY RULE
------------------------------------------------
Never show DEST or SHOW_BUTTON in normal visible text except inside brackets.

------------------------------------------------
INFORMATION RESPONSE RULE
------------------------------------------------
If user asks about pandals, food, culture, clothing, or Puja experience,
reply in a friendly short helpful answer in the same language as the user.

If user greets or asks casually (like hi, hello, kamon acho),
reply in a friendly festival guide style.
"""

    try:
        response = client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_msg
                }
            ],
            temperature=0.3,
            max_tokens=300,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("OpenRouter Error:", e)
        return "Sorry, I’m having trouble right now. Please try again."