from flask import Flask, request, render_template
from flask_cors import CORS
import tensorflow as tf2
from neural_style import style_transfer_tester, utils
from io import BytesIO
import requests
import json
from PIL import Image
from io import BytesIO
import numpy as np
from image_captioning.image_caption import Image_caption
import os

print('!!!!!!!!!!!!!!!')
print(tf2.executing_eagerly())
print('!!!!!!!!!!!!!!!!!!!!!!')

# Get image url from json
image_url = "https://images.mypetlife.co.kr/content/uploads/2019/09/04222847/dog-panting-1024x683.jpg"

# Image load from url
res = requests.get(image_url)
img = Image.open(BytesIO(res.content))
img = np.asarray(img)

img_extension_path = tf2.keras.utils.get_file('image323.jpg',
                                                origin=image_url)
cap = Image_caption()
result_cap , plot = cap.evaluate(img_extension_path)

print(result_cap)