import requests
import json
import time

def send_post():
    start = time.time()
    params = {
        "url": "https://images.mypetlife.co.kr/content/uploads/2019/09/04222847/dog-panting-1024x683.jpg",
    }
    res = requests.post("http://127.0.0.1:5000/tale", data=json.dumps(params))
    print("time to return : " + str(time.time() - start))
    return res.text

print(send_post())