# 🤖 Discord AI Assistant

A Python-based Discord bot that uses Google's Gemini API to provide AI-powered responses directly inside Discord.

## ✨ Features

- 💬 AI-powered conversational responses
- 🧠 Google Gemini API integration
- 🔐 Secure API-key management using environment variables
- ⚡ Simple Discord command interface
- 🧩 Modular Python project structure
- 🛡️ Exception handling for runtime errors
- 🧪 Automated tests using pytest

## 🛠️ Tech Stack

- 🐍 Python
- 💬 Discord.py
- ✨ Google Gemini API
- 🔑 python-dotenv
- 🧪 pytest

## 📁 Project Structure

```text
chagpt-discord-bot/
│
├── bot.py
├── bot_logic.py
├── gemini_service.py
├── requirements.txt
├── README.md
├── .gitignore
└── tests/
    └── test_bot_logic.py
```

## 🔄 How It Works

```text
👤 Discord User
       ↓
💬 Discord Command
       ↓
🐍 Python Bot
       ↓
🧩 Bot Logic
       ↓
✨ Gemini Service
       ↓
🧠 Google Gemini API
       ↓
💬 Generated Response
       ↓
👤 Discord User
```

The bot receives a command from Discord, processes the input using the bot logic, sends the request to Google's Gemini API, and returns the generated response to Discord.

## 💻 Available Commands

### 🤖 Ask

Ask the AI a question:

```text
!ask What is machine learning?
```

### 📝 Summarize

Summarize provided text:

```text
!summarize Artificial intelligence enables computers to perform tasks that normally require human intelligence.
```

### ℹ️ Help

Display available bot commands:

```text
!helpbot
```

## 🔐 Environment Variables

Create a `.env` file in the project directory:

```env
DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

⚠️ **Never upload your `.env` file or expose your API keys publicly.**

The `.env` file is excluded from version control using `.gitignore`.

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aishwaryaranisahu/chagpt-discord-bot.git
cd chagpt-discord-bot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux:**

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a `.env` file and add:

```env
DISCORD_TOKEN=your_discord_bot_token
GEMINI_API_KEY=your_gemini_api_key
```

### 6. Run the bot

```bash
python bot.py
```

## 🧪 Testing

The project includes tests for the core bot logic using pytest.

Run the tests with:

```bash
pytest
```

## 🔒 Security

- 🔑 API credentials are stored in environment variables.
- 🚫 `.env` is excluded from Git.
- 🚫 API keys are not hard-coded in the source code.
- 🚫 Virtual environments and cache files should not be committed.

## 📌 Project Highlights

- 🔌 Integrated a generative AI service with a Discord bot.
- 🧩 Separated bot commands, application logic, and AI-service functionality into modules.
- 🛡️ Added exception handling for API/runtime failures.
- 🔐 Used environment variables for sensitive credentials.
- 🧪 Added automated tests for core logic.

## 👩‍💻 Author

**Aishwarya Rani Sahu**

GitHub: https://github.com/Aishwaryaranisahu
