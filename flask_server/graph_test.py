import tensorflow as tf
from neural_style import style_transfer_tester, utils
import requests
from PIL import Image
from io import BytesIO
import numpy as np

style1 = 'neural_style/fast_neural_style/wave.ckpt'
style2 = 'neural_style/fast_neural_style/udnie.ckpt'
style3 = 'neural_style/fast_neural_style/the_scream.ckpt'
style4 = 'neural_style/fast_neural_style/shipwreck.ckpt'
style5 = 'neural_style/fast_neural_style/rain_princess.ckpt'
style6 = 'neural_style/fast_neural_style/la_muse.ckpt'

# Image load from url
image_url = 'http://image.dongascience.com/Photo/2020/03/5bddba7b6574b95d37b6079c199d7101.jpg'
res = requests.get(image_url)
img = Image.open(BytesIO(res.content))
img = np.asarray(img)

g = tf.Graph()

transformer = style_transfer_tester.StyleTransferTester(
    style1
)

output = transformer.test(img)