import redis
import base64
import time

r = redis.Redis(host="redis", port=6379)

while True:
    _, job = r.brpop("tasks")
    img = base64.b64decode(job)
    print("Processed image of size:", len(img))
    time.sleep(2)