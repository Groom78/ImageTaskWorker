from flask import Flask, request
import redis
import base64

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.route("/upload", methods=["POST"])
def upload():
    image_data = request.files["image"].read()
    encoded = base64.b64encode(image_data).decode("utf-8")
    r.lpush("tasks", encoded)
    return "Image added to queue", 200