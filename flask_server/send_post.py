import requests
import json
import time

def send_post():
    start = time.time()
    params = {
        "url": "https://japan-magazine.jnto.go.jp/jnto2wm/wp-content/uploads/1701_japanese_dog_main.jpg",
    }
    res = requests.post("http://127.0.0.1:5000/style", data=json.dumps(params))
    print("time to return : " + str(time.time() - start))
    return res.text

print(send_post())