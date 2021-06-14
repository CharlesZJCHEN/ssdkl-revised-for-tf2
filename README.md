# ssdkl-revised-for-tf2

These files are revised codes accompanying the paper *Semi-supervised Deep Kernel Learning: Regression with Unlabeled Data by Minimizing Predictive Variance*. These codes were designed for TensorFlow 1. Now they are also available in TensorFlow 2.

Please make sure that you are using Debian instead of CentOS. `libeigen3-dev` package is necessary and is only available in Debian systems. The version of your Python should be 2.7.

In addition to the original instructions, please do mind that, ahead of all codes, run `python setup.py build` and `python setup.py install`, and then copy `pinv_svd_log.so` into the generated package.
