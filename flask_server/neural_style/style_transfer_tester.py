import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
from neural_style import transform

class StyleTransferTester:

    def __init__(self, content_image, model_path):
        # input model
        self.model_path = model_path

        # input images
        self.x0 = content_image

        # image transform network
        self.transform = transform.Transform()

        # build graph for style transfer
        self._build_graph()



    def _build_graph(self):

        # graph input
        self.x = tf.placeholder(tf.float32, shape=self.x0.shape, name='input')
        self.xi = tf.expand_dims(self.x, 0) # add one dim for batch

        # result image from transform-net
        self.y_hat = self.transform.net(self.xi/255.0)
        self.y_hat = tf.squeeze(self.y_hat) # remove one dim for batch
        self.y_hat = tf.clip_by_value(self.y_hat, 0., 255.)

    def test(self):
        
        with tf.Session() as sess:

            # load pre-trained model
            saver = tf.compat.v1.train.Saver()
            saver.restore(sess, self.model_path)

            # get transformed image
            output = sess.run(self.y_hat, feed_dict={self.x: self.x0})

        return output





