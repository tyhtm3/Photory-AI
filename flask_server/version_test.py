import tensorflow as tf
from neural_style import style_transfer_tester, utils

path = 'sample.jpg'
image = utils.load_image(path, max_size=None)

style_model = 'neural_style/fast_neural_style/wave.ckpt'

transformer = style_transfer_tester.StyleTransferTester(
    img, style_model
)
output = transformer.test()