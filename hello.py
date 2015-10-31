from flask import Flask
import redis

app = Flask(__name__)

@app.route("/")
def hello():
    in_redis = {}
    client = redis.Redis()
    keys = client.keys()
    for key in keys:
        in_redis[key] = client.get(key)
    return "Hello World!<br>Redis has<br>{}<br>in it".format(in_redis)

if __name__ == "__main__":
   app.run()