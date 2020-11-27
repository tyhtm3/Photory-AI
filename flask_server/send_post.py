import requests
import json
import time

def send_post():
    start = time.time()
    params = {
        "story_pk": 1,
        "imagePaths":["asdf"]
    }
    res = requests.post("http://127.0.0.1:5000/tale", data=json.dumps(params))
    print("time to return : " + str(time.time() - start))
    return res.text

print(send_post())