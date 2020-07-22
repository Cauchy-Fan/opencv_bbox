import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('lena.jpg', cv2.IMREAD_COLOR)[:, :, ::-1]
# numpy 默认是取模运算， 250 + 10 = 260%256 = 4
# 所以这里使用np.clip进行范围限定
# a<0 => a=0, a>255 => a=255
res = np.uint8(np.clip((1.5 * img + 10), 0, 255))

# 两张图片横向合并(便于对比显示)
tmp = np.hstack((img, res))
plt.imshow(tmp)
plt.show()
