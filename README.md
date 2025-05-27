
# 🎓 Sonun University RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built for **Sonun University**, Bishkek, Kyrgyzstan. The bot can answer questions based on university policy documents (PDFs), leveraging a vector search engine and LLMs (Ollama or Azure-hosted).

---

## 🚀 Features

- 📄 Ingests and embeds university PDFs
- 🔍 FAISS vector search for relevant context
- 🧠 LLM-powered answer generation (Ollama or Azure)
- 🤖 Telegram bot interface (via Aiogram)
- 🇰🇬 Responds in Kyrgyz language
- 🧩 Supports both Markdown (input) and HTML (Telegram output)

---

## 📁 Project Structure

```
rag_knu/
│
├── rag_knu.py            # Main RAG logic
├── bot.py                # Telegram bot using Aiogram
├── pdfs/                 # Folder with policy PDFs
├── utils.py              # Markdown → HTML converter
├── README.md             # You're here
└── requirements.txt      # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/rag-knu.git
cd rag-knu
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Start Ollama (Optional)

```bash
ollama run llama3
```

Or use your Azure endpoint.

### 4. Set Environment Variables

Create a `.env` file or set them directly:

```bash
export V3_TOKEN=your_azure_token_here
export BOT_TOKEN=your_telegram_bot_token
```

---

## 🧠 Answer Generation Logic

```python
def generate_answer(question: str, context: str, use_ollama: bool = False):
    ...
```

If `use_ollama=True`, the response will be streamed from local Ollama. Otherwise, it uses Azure's hosted model.

---

## 💬 Telegram Bot Commands

- `/start` — Greet the user and explain the bot
- `/ask` — Enter a question based on policy
- `/help` — Show usage info

---

## ✅ HTML Formatting for Telegram

Markdown-style input like `**bold**` is converted to Telegram-safe HTML:

```python
**bold** → <b>bold</b>
\n       → <br/>
```

---

## 🧪 Example Prompt

> **Question:** Университетте AI колдонсо болобу?  
> **Answer:** <br/> <b>AI Use:</b> Окуу максатында колдонсо болот, бирок сөзсүз түрдө көрсөтүлүшү жана шилтемеси берилиши керек.

---

## 🏫 About

Developed as part of a digital guide initiative for Sonun University (Kyrgyz National University context) to support students and staff in accessing university rules using natural language.

---
