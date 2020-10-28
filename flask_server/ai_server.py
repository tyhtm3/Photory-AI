from flask import Flask, request, render_template
from flask_cors import CORS
import tensorflow as tf
from neural_style import style_transfer_tester, utils
from io import BytesIO
import requests
import json
from PIL import Image
from io import BytesIO
import numpy as np

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# 임시
content_path = 'neural_style/content/female_knight.jpg'
content_image = utils.load_image(content_path,max_size=None)

style_model = 'neural_style/fast_neural_style/wave.ckpt'



g = tf.get_default_graph()

@app.route('/')
def index_page():
    
    return "AI server!"

@app.route('/style', methods=['POST'])
def style():
    # Get image url from json
    path = json.loads(request.get_data(), encoding='utf-8')
    image_url = path['url']
    
    # Image load from url
    res = requests.get(image_url)
    img = Image.open(BytesIO(res.content))
    img = np.asarray(img)

    # run neural network
    transformer = style_transfer_tester.StyleTransferTester(
        img, style_model
    )
    output = transformer.test()

    # save result
    result_path = 'asdf.jpg'
    utils.save_image(output, 'static/'+result_path)
    return result_path

@app.route('/image/<filename>')
def image(filename):
    return render_template('static.html', filename=filename)

if __name__=='__main__':
    #app.run(host='0.0.0.0')
    app.run()