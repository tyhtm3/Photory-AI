from image_captioning.image_caption import Image_caption
import tensorflow as tf

image_url = 'https://tensorflow.org/images/surf.jpg'
img_extension_path = tf.keras.utils.get_file('image1231.jpg',
                                            origin=image_url)
caption_model = Image_caption()
res, plot = caption_model.evaluate(img_extension_path)

print(res)