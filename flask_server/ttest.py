import tensorflow as tf
from neural_style import style_transfer_tester, utils, transform

# load content image
content_path = 'neural_style/content/example.JPG'
content_image = utils.load_image(content_path, max_size=None)

style_path = 'neural_style/fast_neural_style/wave.ckpt'

# open session
soft_config = tf.ConfigProto(allow_soft_placement=True)
soft_config.gpu_options.allow_growth = True # to deal with large image
sess = tf.Session(config=soft_config)

x = tf.placeholder(tf.float32, shape=content_image.shape, name='input')
xi = tf.expand_dims(x,0)

t = transform.Transform()
y_hat = t.net(xi/255.0)

y_hat = tf.squeeze(y_hat)
y_hat = tf.clip_by_value(y_hat, 0., 255.)

saver = tf.train.Saver()
saver.restore(sess, style_path)

cnt = 0
def gogo():

    output = sess.run(y_hat, feed_dict={x: content_image}) 
    path_name = "asdf"+str(cnt)+".jpg"
    utils.save_image(output, path_name)

gogo()