from flask import Flask, request, render_template
from flask_cors import CORS
import tensorflow as tf
from neural_style import style_transfer_tester, utils

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

@app.route('/test')
def test_path():
    with g.as_default():
        output = transformer.test()
    return 'good!'

@app.route('/image/<filename>')
def image(filename):
    return render_template('static.html', filename=filename)

if __name__=='__main__':
    #app.run(host='0.0.0.0')
    app.run()