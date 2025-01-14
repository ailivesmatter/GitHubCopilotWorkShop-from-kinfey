import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=150
    )

    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
