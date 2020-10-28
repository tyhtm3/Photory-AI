import requests
import json
import time

def send_post():
    start = time.time()
    params = {
        "url": "http://ecotopia.hani.co.kr/files/attach/images/69/406/492/d2.jpg",
    }
    res = requests.post("http://127.0.0.1:5000/style", data=json.dumps(params))
    print("time to return : " + str(time.time() - start))
    return res.text

print(send_post())