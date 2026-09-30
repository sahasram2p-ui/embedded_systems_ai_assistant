# Embedded Systems AI Assistant

Professional domain-restricted AI chatbot using Flask + Google GenAI + Gemini.

## Setup
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Edit `.env`:
```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
GEMINI_MODEL=gemini-3.1-flash-lite
```
Then run:
```powershell
python app.py
```
Open `http://127.0.0.1:5000`.

## Structure
```text
embedded_systems_ai_assistant/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── README.md
├── templates/index.html
└── static/
    ├── style.css
    └── script.js
```

The API key is server-side only and `.env` is ignored by Git. The assistant is restricted to embedded-systems topics.
