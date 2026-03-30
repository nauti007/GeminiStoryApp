# 🤖 Unit Story Generator
<img width="592" height="528" alt="image" src="https://github.com/user-attachments/assets/e83d4f79-4d69-4bcb-91cc-4986f46e43c2" />


An AI-powered desktop application built with **Python**, **PyQt6**, and **Google Gemini 2.5 Flash**.

## ✨ Features
- **Custom UI:** Built with PyQt6 for a smooth desktop experience.
- **Advanced Prompt Engineering:** Uses structured tasking to ensure the AI provides complete, 3-sentence narratives.
- **Robust Logic:** Includes error handling for network timeouts and API safety filters.

## 🛠️ Installation
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `config.py` in your local folder with your `api_key`.
4. Run: `python genai_story_app.py`

## 🧠 What I Learned
During this project, I moved from OpenAI to Gemini 2.5 Flash. I learned to handle **Kernel deadlocks**, implement **Request Timeouts**, and use **Top-P/Top-K** sampling to prevent the AI from truncating responses.
