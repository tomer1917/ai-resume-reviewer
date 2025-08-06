# AI Resume Reviewer

A simple full-stack application that uses an LLM to compare a candidate’s resume (PDF) against a job description and return a match score, missing keywords, and actionable suggestions.

---

## 🔍 Features

- **PDF resume upload** (via multipart/form-data)  
- **Job description** input  
- **AI-powered analysis** using OpenAI’s GPT models  
- **Match score** between 0.0–1.0  
- **Missing keywords** list  
- **Actionable suggestions** for improving the resume  
- **Health check** endpoint at `/health`

---

## 🛠 Tech Stack

- **Backend**: Python 3.11+, FastAPI, Uvicorn  
- **AI/NLP**: OpenAI Python SDK (`gpt-3.5-turbo`)  
- **PDF parsing**: `pdfminer.six`  
- **Frontend**: React (Vite + JSX), Axios  
- **Dev tools**: Git, GitHub, npm, virtual environments  

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-reviewer.git
cd ai-resume-reviewer
```

### 2. Backend Setup

```bash
cd backend
python3 -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows (CMD)
.venv\Scripts\activate

pip install --upgrade pip
pip install -r requirements.txt
```

1. **Create** a file named `.env` in `backend/` (it’s already in `.gitignore`):  
   ```dotenv
   OPENAI_API_KEY=sk-your_real_key_here
   # Optional for dev-only mock mode:
   DEV_MOCK=true
   ```
2. **Run** the backend server:
   ```bash
   uvicorn app.main:app --reload
   ```
3. **Verify** health check in your browser or via `curl`:
   ```
   GET http://127.0.0.1:8000/health
   → {"status":"ok"}
   ```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
```

- **Proxy** to the backend is configured in `vite.config.js`—you can call `/review` directly.

1. **Start** the React dev server:
   ```bash
   npm run dev
   ```
2. **Open** your browser at `http://localhost:5173`

---

## 💡 Usage

1. In the frontend UI, **select** a PDF resume.  
2. **Paste** the job description text.  
3. Click **Analyze Resume**.  
4. View your **match score**, **missing keywords**, and **suggestions**.

---

## 🗂 Project Structure

```
ai-resume-reviewer/
├── backend/
│   ├── .env                # (ignored) your API key + flags
│   ├── .venv/              # virtual environment
│   ├── requirements.txt
│   └── app/
│       ├── main.py
│       ├── routers/
│       ├── services/
│       └── models/
└── frontend/
    ├── public/
    ├── src/
    │   ├── App.js
    │   └── components/
    ├── package.json
    └── vite.config.js
```

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/YourFeature`)  
3. Commit your changes (`git commit -m "feat: add …"`)  
4. Push to your branch (`git push origin feature/YourFeature`)  
5. Open a Pull Request  

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
