from flask import Flask, request, render_template
from flask_cors import CORS
import tensorflow as tf
from neural_style import style_transfer_tester, utils
from io import BytesIO
import requests
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

# 임시
content_path = 'neural_style/content/female_knight.jpg'
content_image = utils.load_image(content_path,max_size=None)

style_model = 'neural_style/fast_neural_style/wave.ckpt'

transformer = style_transfer_tester.StyleTransferTester(
    content_image, style_model
)

g = tf.get_default_graph()

@app.route('/')
def index_page():
    
    return "AI server!"

@app.route('/style', methods=['POST'])
def style():
    # Get image url from json
    path = json.loads(request.get_data(), encoding='utf-8')
    image_url = path['url']
    print(image_url)

    #with g.as_default():
    #    output = transformer.test()
    return 'good!'

@app.route('/image/<filename>')
def image(filename):
    return render_template('static.html', filename=filename)

if __name__=='__main__':
    #app.run(host='0.0.0.0')
    app.run()