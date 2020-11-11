import tensorflow.compat.v1 as tf

g = tf.Graph()
print(g)
sess = tf.Session()
saver = tf.train.import_meta_graph('fast_neural_style/wave.ckpt.meta')



