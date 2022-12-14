import time
import redis
from flask import Flask
from greet import greet
# import the welcome function from welcome.py
app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

# def get_hit_count():
#     retries = 5
#     while True:
#         try:
#             return cache.incr('hits')
#         except redis.exceptions.ConnectionError as exc:
#             if retries == 0:
#                 raise exc
#             retries -= 1
#             time.sleep(0.5)

@app.route('/')
def hello():
    return greet()