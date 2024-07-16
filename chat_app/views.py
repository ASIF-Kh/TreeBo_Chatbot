from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai

# Create your views here.
# add here to your generated API key
genai.configure(api_key="AIzaSyDrefuYMMd23jgptIbmyu7ZbdggrREDfWI")

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")
        print(text)



        model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
        # safety_settings = Adjust safety settings
        # See https://ai.google.dev/gemini-api/docs/safety-settings
        system_instruction="You are a ChatBot named TreeBo, your task is to answers all the queries related to Sustainable Development and sustainable development goals. If a question is unrelated to Sustainable Development, answer \"Please  ask questions only related to sustainable  development.\"",
        )

        chat_session = model.start_chat(
    history=[
        {
        "role": "user",
        "parts": [
            "hi",
        ],
        },
        {
        "role": "model",
        "parts": [
            "Hello! 👋  I'm TreeBo, your guide to all things sustainable development. What can I help you learn about today? 🌎 \n",
        ],
        },
    ]
    )

        response = chat_session.send_message(text)

 
 
        response_data = {
            "text": response.text,  # Assuming response.text contains the relevant response data
            # Add other relevant data from response if needed
        }
        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(
            reverse("chat")
        )  # Redirect to chat page for GET requests



def chat(request):
    # user = request.user
    # chats = ChatBot.objects.filter(user=user)
    return render(request, "base.html",) #{"chats": chats})
