import os
from openai import OpenAI
import json
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

# Load API keys
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

slack_client = WebClient(token=SLACK_BOT_TOKEN)
openai_client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)


def get_ai_suggestion(message):
    """Uses OpenAI to suggest a fix based on the user's message."""
    try:
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert DevOps assistant."},
                {"role": "user", "content": message},
            ],
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logging.error(f"OpenAI API Error: {e}")
        return "Sorry, I encountered an error processing your request."


@app.route("/slack/events", methods=["POST"])
def slack_events():
    """Listens for messages and responds with AI-based troubleshooting suggestions."""
    data = request.json
    
    # Handle Slack URL verification challenge
    if "challenge" in data:
        return jsonify({"challenge": data["challenge"]})
    
    if "event" in data:
        event = data["event"]
        
        # Prevent bot from responding to its own messages
        if event.get("bot_id"):
            return jsonify({"status": "ok"})
        
        # Handle app mentions and direct messages
        if event.get("type") == "app_mention" or (
            event.get("type") == "message" and event.get("channel_type") == "im"
        ):
            user_message = event.get("text", "")
            channel_id = event["channel"]
            
            # Remove bot mention from message
            user_message = user_message.replace(f"<@{event.get('bot_id', '')}>", "").strip()
            
            if user_message:
                response_text = get_ai_suggestion(user_message)
                try:
                    slack_client.chat_postMessage(
                        channel=channel_id, 
                        text=response_text
                    )
                except SlackApiError as e:
                    logging.error(f"Slack API Error: {e.response['error']}")
    
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(port=3000, debug=True)