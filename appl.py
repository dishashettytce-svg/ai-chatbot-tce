from flask import Flask, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

# Base prompt for Tulu chatbot
BASE_PROMPT = """
You are a friendly Tulu language teaching chatbot.
Your purpose is to help beginners learn Tulu through storytelling and quizzes.

Flow:
1. Tell a short, simple story in English.
2. After the story, pick 1-2 key Tulu words or phrases from the story.
3. Present each word/phrase as a multiple-choice question:
   - Give 4 English options labeled A, B, C, D.
   - Ask the user to choose the correct meaning.
4. Give immediate feedback:
   - If correct: say "Correct!" and explain the meaning in simple English.
   - If wrong: say "Incorrect. The correct answer is ___" and explain.
5. Keep sentences short and simple.
6. Make it fun and encouraging.
7. Track the user's score and summarize at the end.
Rules:
- Use Romanized Tulu for words/phrases.
- Introduce only one Tulu word at a time in the quiz.
- Make the story engaging and suitable for beginners.
"""

# Flask route to chat with Tulu bot
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Combine base prompt + user message
    full_prompt = f"{BASE_PROMPT}\nUser: {user_message}\nBot:"

    # Send prompt to OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=full_prompt,
        temperature=0.7,
        max_tokens=200
    )

    bot_message = response.choices[0].text.strip()
    return jsonify({"response": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
