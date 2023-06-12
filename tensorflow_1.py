# -*- coding: utf-8 -*-
"""tensorflow_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_e7kDNNG3sbdqp3dOUxX0ZX14T-PYnmr

@tf.functions - a way to speed up your regular python functions.
"""

import tensorflow as tf
print(tf.__version__)

scalar=tf.constant(7)
scalar

scalar.ndim

vector=tf.constant([10,7])
vector

vector.ndim

matrix=tf.constant([[10,7], 
                    [7,10]])
matrix

matrix.ndim

another_matrix=tf.constant([[1,2],
                            [2,3],
                            [3,4]])
another_matrix

another_matrix.ndim

tensor=tf.constant([[[1,2],[2,3]],
                    [[3,4],[4,5]],
                    [[5,6],[6,7]]])
tensor

tensor.ndim

