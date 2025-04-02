
from flask import Flask, request, jsonify, render_template
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/novaq", methods=["POST"])
def novaq():
    user_input = request.form.get("input")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Du bist NovaQ Core."},
            {"role": "user", "content": user_input}
        ]
    )
    reply = response.choices[0].message["content"]
    return render_template("index.html", answer=reply, user_input=user_input)
