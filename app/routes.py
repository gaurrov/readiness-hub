from flask import Flask, jsonify, request
from app.storage import save_student
app = Flask(__name__)


@app.post("/students")
def register_student():
    data = request.get_json()
    name = data["name"]
    if name == "":
        return jsonify(error="Name is required"), 400
    student = save_student(name)
    return jsonify(student), 201
