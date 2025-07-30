from flask import Flask, request, render_template
from dotenv import load_dotenv
import openai
import os

load_dotenv()
app = Flask(__name__)
openai.api_key=os.getenv("OPENAI_API_KEY")






def get_user_prompt(user_input):
  promt=get_prompt(user_input)
  response=openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role":"user","content":promt}]
  )
  return response.choices[0].message.content.strip()





def get_prompt(user_input):
 return f"""
You are a professional and friendly AI Career Counselor.

Your job is to understand the user's input and respond in the **same language** — Hindi or English — automatically.

User's Input: "{user_input}"

Please respond in the following format:

1. 🧠 **Career Suggestion** – Suggest a suitable career path and explain why it fits.
2. 🎯 **Key Skills to Focus On** – Mention 2–3 important skills with 1-line explanation.
3. 📚 **Learning Plan** – Recommend at least one free/affordable course with platform name.
4. 💡 **Final Advice** – End with a motivational or practical tip.

Use bullet points, bold titles, and clear formatting.  
Keep tone friendly, professional, and encouraging.
"""


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["question"]
        response = get_user_prompt(user_input)
        return render_template("index.html", response=response)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

