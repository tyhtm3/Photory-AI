import tensorflow as tf
from neural_style import style_transfer_tester, utils, transform

# load content image
content_path = 'neural_style/content/example.JPG'
content_image = utils.load_image(content_path, max_size=None)

style_path = 'neural_style/fast_neural_style/wave.ckpt'

transformer = style_transfer_tester.StyleTransferTester(
    content_image, style_path
)

output = transformer.test()
utils.save_image(output, "result.jpg")