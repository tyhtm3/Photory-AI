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
from image_captioning.image_caption import Image_caption
import os

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

IMAGE_SERVER_URL = "http://127.0.0.1:8000"
STYLE_PATH = ['wave.ckpt', 'udnie.ckpt', 'the_scream.ckpt', 'shipwreck.ckpt', 'rain_princess.ckpt', 'la_muse.ckpt']

@app.route('/')
def index_page():
    return "AI server!"

@app.route('/tale', methods=['POST'])
def tale():
    data = json.loads(request.get_data(), encoding='utf-8')
    story_pk = data['story_pk']
    paths = data['imagePaths']

    cnt = 0

    for path in paths:
        # image load from url
        image_url = IMAGE_SERVER_URL + '/media/' +path
        res = requests.get(image_url)
        img = Image.open(BytesIO(res.content))
        img = np.asarray(img)

        for i in range(6):
            with tf.Graph().as_default():
                transformer = style_transfer_tester.StyleTransferTester(
                    img, 'neural_style/fast_neural_style/' + STYLE_PATH[i]
                )
                output = transformer.test()
            
            result_path = str(story_pk) + '_' + str(cnt) + '_'+ str(i) + '.jpg'
            utils.save_image(output, 'static/' + result_path)
        cnt = cnt + 1

    params = {
        'story_pk' : story_pk,
        'tale': ['아직', '준비중인', '컨텐츠', '입니다', 'ㅎㅎ']
    }

    requests.post('http://127.0.0.1:8000/storys/editable/', data = params)
    return 'ok'


@app.route('/style', methods=['POST'])
def style():
    # Get image url from json
    path = json.loads(request.get_data(), encoding='utf-8')
    image_url = path['url']
    
    # Image load from url
    res = requests.get(image_url)
    img = Image.open(BytesIO(res.content))
    img = np.asarray(img)

    img_extension = image_url[-4:]
    img_extension_path = tf.keras.utils.get_file('image'+img_extension,
                                                origin=image_url)

    for i in range(1,6):
        with tf.Graph().as_default():
        # run neural network
            transformer = style_transfer_tester.StyleTransferTester(
                img, 'neural_style/fast_neural_style/wave.ckpt'
            )
            output = transformer.test()

        # save result
        result_path = 'asdf3.jpg'
        utils.save_image(output, 'static/'+str(i)+'_1'+result_path)

        with tf.Graph().as_default():
            # run neural network
            transformer = style_transfer_tester.StyleTransferTester(
                img, 'neural_style/fast_neural_style/udnie.ckpt'
            )
            output = transformer.test()

        # save result
        result_path = 'asdf3.jpg'
        utils.save_image(output, 'static/'+str(i)+'_2'+result_path)
    
    with tf.Graph().as_default():
        caption_model =  Image_caption()
        result_cap , plot = caption_model(img_extension_path)
    return result_cap

@app.route('/image/<filename>')
def image(filename):
    return render_template('static.html', filename=filename)

if __name__=='__main__':
    #app.run(host='0.0.0.0')
    app.run()