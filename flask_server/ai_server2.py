from flask import Flask, request, render_template
from flask_cors import CORS
from TextGeneration.Module import StoryGenerator_photory as SGEN
import tensorflow as tf
from image_captioning.image_caption import Image_caption


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def index_page():
    return "AI server2!"

@app.route('/tale')
def tale():
    st = SGEN.StoryGeneration()
    return st.Generate_p_sampling('나는 서있다')


@app.route('/test')
def test():
    image_url = 'https://tensorflow.org/images/surf.jpg'
    img_extension_path = tf.keras.utils.get_file('image13231.jpg',
                                                origin=image_url)
    caption_model = Image_caption()
    res, plot = caption_model.evaluate(img_extension_path)

    st = SGEN.StoryGeneration()
    return st.Generate_p_sampling(' '.join(res))

if __name__=='__main__':
    app.run(host='0.0.0.0')

