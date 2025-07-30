# 🎓 Career Counselor AI Bot

An AI-powered career guidance web app that gives personalized suggestions based on user input. Built with **Flask** and **OpenAI GPT-3.5**, styled with HTML & CSS, and fully responsive.

---

## 🌟 Features

- 💬 Ask questions in **Hindi or English**
- 📚 Get career suggestions with:
  - Suitable field
  - Key skills
  - Learning resources
  - Final advice
- 🎯 Clean, simple & mobile-friendly UI
- 🔐 Secure `.env` for API key

---

## 🚀 Live Demo

👉 [Click to open the app](https://career-counselor-bot.onrender.com/).

---

## 🛠️ Tech Stack

- Python (Flask)
- OpenAI GPT-3.5 Turbo
- HTML + CSS (Responsive)
- Render (Hosting)

---

## 🔧 How to Run Locally

```bash
# 1. Clone this repo
git clone https://github.com/yourusername/career-counselor-bot.git

# 2. Move into the project folder
cd career-counselor-bot

# 3. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate   # Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Add your OpenAI API key to .env
OPENAI_API_KEY=your_openai_key_here

# 6. Run the Flask app
python app.py

