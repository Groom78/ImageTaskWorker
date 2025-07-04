import redis
import base64
import time

while True:
    try:
        r = redis.Redis(host="redis", port=6379)
        r.ping()
        break
    except redis.exceptions.ConnectionError:
        print("Redis is not ready. Retrying in 2 seconds...")
        time.sleep(2)

while True:
    _, job = r.brpop("tasks")
    img = base64.b64decode(job)
    print("Processed image of size:", len(img))
    time.sleep(2)
