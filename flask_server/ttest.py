import tensorflow as tf
from neural_style import style_transfer_tester, utils

# load content image
content_path = 'neural_style/content/female_knight.jpg'
content_image = utils.load_image(content_path, max_size=None)

style_path = 'neural_style/models/wave.ckpt'

# open session
soft_config = tf.ConfigProto(allow_soft_placement=True)
soft_config.gpu_options.allow_growth = True # to deal with large image
sess = tf.Session(config=soft_config)


transformer = style_transfer_tester.StyleTransferTester(session=sess,
                                                        model_path=style_path,
                                                        content_image=content_image,
                                                        )

# execute the graph
output_image = transformer.test()

# save result
utils.save_image(output_image, 'ttest.jpg')