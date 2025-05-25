from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pairs = [
    [r"(ชื่อ|คุณชื่ออะไร)", ["ผมชื่อแชทบอทครับ"]],
    [r"(ทำอะไรได้บ้าง)", ["ผมตอบคำถามทั่วไปได้นิดหน่อย ลองถามมาเลยครับ"]],
    [r"(ลาก่อน|บ๊ายบาย)", ["บ๊ายบายครับ แล้วพบกันใหม่"]],
    [r"(.*)", ["ขอโทษครับ ผมยังไม่เข้าใจคำถามนี้ ลองถามใหม่ได้นะครับ"]],
]

chatbot = Chat(pairs, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json["message"]
    bot_reply = chatbot.respond(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
