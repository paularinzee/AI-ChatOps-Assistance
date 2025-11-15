# 🤖 Slack DevOps AI Assistant Bot

A powerful AI-driven Slack bot that provides instant DevOps troubleshooting, cloud guidance, error explanations, and automation tips directly inside Slack.  
This bot uses **OpenAI GPT models** to interpret user messages and respond with intelligent, actionable DevOps solutions.

---

## 🚀 Features

- ⚙️ **AI-Powered DevOps Assistance**  
  Automatically analyzes errors, logs, and DevOps issues posted in Slack and provides suggested fixes.

- 🤖 **Smart @Mentions**  
  Responds when mentioned in a channel or via direct messages.

- 🔐 **Secure Environment Variables**  
  Uses `.env` to store API keys.

- 🧠 **Powered by OpenAI Responses API**  
  Uses latest GPT-4.1 API for fast and accurate responses.

- 🛡️ **Slack Bot Protected**  
  Prevents infinite loops by ignoring its own messages.

- 🌐 **Fast & Lightweight Backend**  
  Built using Flask and Slack SDK.

---

## 🏗️ Project Structure

project/
│── chatops_bot.py
│── requirements.txt
│── .env.example
└── README.md


---

## 🔧 Technology Stack

- **Python 3.9+**
- **Flask** (Webhook server)
- **Slack SDK (WebClient)**
- **OpenAI Responses API**
- **dotenv** (Environment management)

---

## 🧰 Installation & Setup

### **1. Clone the repository**
```bash
git clone https://github.com/paularinzee/AI-ChatOps-Assistance.git
cd AI-ChatOps-Assistance
```
### **2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```
### **3. Install dependencies**
```bash
pip install -r requirements.txt
```

### **4. Rename and configure environment variables**
Create a .env file:

```bash
SLACK_BOT_TOKEN=your-slack-bot-token
SLACK_SIGNING_SECRET="your-slack-signing-secret"
OPENAI_API_KEY=your-openai-api-key
```
### **5. Run the Flask server**
```bash
python bot.py
```
Your bot will now listen on:
```bash
http://localhost:3000/slack/events
```

## Author

[Paul Nnaji](https://github.com/paularinzee)

## License

[MIT](./LICENSE)