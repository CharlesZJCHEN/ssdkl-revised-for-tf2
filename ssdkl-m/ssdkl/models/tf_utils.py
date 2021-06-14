import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()



def eye(N, name=None):
    """
    Returns NxN identity matrix.
    """
    return tf.diag(tf.ones(tf.stack([N, ]), dtype=tf.float32), name=name)
