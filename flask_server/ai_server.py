from flask import Flask, request
from flask_cors import CORS
import tensorflow as tf
from neural_style import style_transfer_tester, utils

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def index_page():
    return "AI server!"

@app.route('/test')
def test_path():
    # load image and style model
    content_path = 'neural_style/content/female_knight.jpg'
    content_image = utils.load_image(content_path,max_size=None)

    style_model = 'neural_stlye/models.wave.ckpt'
    # session setting
    soft_config = tf.ConfigProto(allow_soft_placement=True)
    soft_config.gpu_options.allow_growth = True # to deal with large image
    sess = tf.Session(config=soft_config)

    transformer = style_transfer_tester.StyleTransferTester(session=sess,
                                                        model_path=style_model,
                                                        content_image=content_image,
                                                        )

    print(transformer.model_path)
    return 'good!'
    
if __name__=='__main__':
    app.run(host='0.0.0.0')