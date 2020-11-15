from flask import Flask, request, render_template
from flask_cors import CORS
from TextGeneration.Module import StoryGenerator_photory as SGEN
import tensorflow as tf
from image_captioning.image_caption import Image_caption
import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

IMAGE_SERVER_URL = "http://121.125.56.92:50740"

@app.route('/')
def index_page():
    return "AI server2!"


@app.route('/tale', methods=['POST'])
def test():
    data = json.loads(request.get_data(), encoding='utf-8')
    story_pk = data['story_pk']
    paths = data['imagePaths']

    # model load
    caption_model = Image_caption()
    st = SGEN.StoryGeneration()

    # exe
    texts = []
    for path in paths:
        image_url = IMAGE_SERVER_URL + '/media/' +path
        image_url = path
        img_extension_path = tf.keras.utils.get_file('image.jpg',
                                                origin=image_url)
        res, plot = caption_model.evaluate(img_extension_path)
        texts += st.Generate_p_sampling(' '.join(res))

    result = {
        'texts' : texts
    }
    return result

if __name__=='__main__':
    app.run(host='0.0.0.0')

