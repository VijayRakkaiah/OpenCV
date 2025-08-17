import os
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def convolution2d():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\car.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    n = 100
    kernal = np.ones((n,n), np.float32) / (n*n)
    imgFilter = cv.filter2D(src=imgRGB, ddepth=-1, kernel=kernal)

    plt.figure()
    plt.subplot(121)
    plt.imshow(imgRGB)

    plt.subplot(122)
    plt.imshow(imgFilter)

    plt.show()


if __name__ == '__main__':
    convolution2d()