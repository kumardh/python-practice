import tensorflow as tf
# Computational Graph:
c1 = tf.constant(0.034)
c2 = tf.constant(1000.0)
x = tf.multiply(c1, c1)
y = tf.multiply(c1, c2)
final_node = tf.add(x, y)
# Running the session:
with tf.Session() as sess:
    result = sess.run(final_node)
    print(result, type(result))