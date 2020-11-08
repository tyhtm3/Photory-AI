from image_captioning.image_caption import Image_caption
import tensorflow as tf

print('aaa')
caption_model = Image_caption()

print('asdfasdf')

image_url = input()
image_extention = image_url[-3:]
print(image_extention)
image_path = tf.keras.utils.get_file('image'+image_extention,
                                            origin=image_url)

result, aa = caption_model.evaluate(image_path)
print(' '.join(result))
