from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)

# ---- Dán API KEY của bạn vào đây ----
API_KEY = "AIzaSyA4jR4s2gfzoiQ2mgeY0GkXPYQkG9JhNh8"
# --------------------------------------

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET"])
def home():
    return "StudyBot API đang hoạt động 24/7!"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("q", "")

    response = model.generate_content(
        f"""
        Bạn là StudyBot - trợ lý học tập AI.
        Chỉ trả lời các câu hỏi học tập (Toán, Lý, Hóa, Sinh, Văn, Sử, Địa...).
        Nếu câu hỏi không thuộc học tập, trả lời:
        'Tôi chỉ có thể giúp bạn trong việc học thôi nhé 😊'.

        Câu hỏi: {question}
        """
    )

    return jsonify({"answer": response.text})
