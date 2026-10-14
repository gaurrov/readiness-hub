from flask import Flask, jsonify, request
from app.storage import save_student

app = Flask(__name__)


@app.post("/students")
def register_student():
    data = request.get_json()
    name = data["name"]
    student = save_student(name)
    return jsonify(student), 201
