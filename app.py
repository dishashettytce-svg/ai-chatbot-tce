from flask import Flask, request, jsonify
import openai
import os
from dotenv import load_dotenv


# Load your OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize 
app = Flask(__name__)

# Base prompt for Tulu chatbot
BASE_PROMPT = """
You are a friendly Tulu language teaching chatbot.
You help beginners learn Tulu through storytelling and multiple-choice quizzes.
"""

# Function to get response from GPT
def get_completion(prompt):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message["content"]

# API endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    full_prompt = BASE_PROMPT + "\nUser: " + user_input + "\nChatbot:"
    reply = get_completion(full_prompt)
    return jsonify({"response": reply})

# Run server
if __name__ == "__main__":
    app.run(debug=True)
