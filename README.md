# ChatGPT Discord Bot

A Python-based Discord chatbot integrating the Discord API with the OpenAI API.

## Features

The bot provides three user-facing commands:

| Command | Purpose |
|---|---|
| `!ask <question>` | Sends a question to the OpenAI API and returns the response |
| `!summarize <text>` | Requests a concise summary of supplied text |
| `!helpbot` | Displays available commands and usage examples |

## Technical highlights

- Python
- `discord.py` for the Discord bot command framework
- OpenAI Python SDK and Responses API
- Environment-based credential handling with `python-dotenv`
- Exception handling for API and command failures
- Input validation before API calls
- Offline unit tests using `pytest`

## Architecture

```text
Discord User
     |
     v
discord.py command
     |
     +--> input validation
     |
     +--> prompt builder
     |
     v
OpenAIService
     |
     v
OpenAI Responses API
     |
     v
Discord response
```

## Testing

The project includes three offline test cases in `tests/test_bot_logic.py`.

1. **Valid Q&A input** — verifies that a normal question is accepted and converted into a prompt.
2. **Summarization input** — verifies that supplied text is accepted and placed into the summarization prompt.
3. **Invalid/empty input** — verifies that blank input is rejected before an API call.

Run:

```bash
pytest -q
```

The tests do **not** call Discord or OpenAI, so they can run without API credentials.

## Local setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy `.env.example` to `.env` and add your own credentials:

```text
DISCORD_TOKEN=...
OPENAI_API_KEY=...
OPENAI_MODEL=gpt-5
```

Never commit `.env` or real API keys.

### 4. Configure the Discord bot

Create a Discord application/bot in the Discord Developer Portal.

Enable the **Message Content Intent** for the bot and enable the same intent in the code. The `discord.py` commands extension requires this intent for prefix commands.

Invite the bot to a test server with the permissions required to read and send messages.

### 5. Run the bot

```bash
python bot.py
```

Then test in Discord:

```text
!helpbot
!ask explain recursion in simple terms
!summarize Python is a general-purpose programming language...
```

## Security

- Secrets are read from environment variables.
- `.env` is excluded through `.gitignore`.
- `.env.example` contains placeholders only.
- The repository should never contain real Discord tokens or OpenAI API keys.

## Project structure

```text
chatgpt-discord-bot/
├── bot.py
├── bot_logic.py
├── openai_service.py
├── tests/
│   └── test_bot_logic.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Resume alignment

This repository supports the following resume claims:

- Developed a Discord chatbot integrating the OpenAI API.
- Implemented three user-facing commands for Q&A, summarization, and help.
- Implemented environment-based credential handling.
- Added exception management and input validation.
- Validated prompt and command logic through a three-case offline testing workflow.

## Notes

This project is intended as a portfolio/learning project. Do not use it as a medical, financial, or other high-stakes decision system.
