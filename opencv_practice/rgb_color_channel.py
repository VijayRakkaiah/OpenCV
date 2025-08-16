import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def pureColors():
    zeros = np.zeros(shape=(100,100))
    ones = np.ones(shape=(100,100))

    bImg = cv.merge(mv=(zeros, zeros, 255*ones))
    gImg = cv.merge(mv=(zeros, 255*ones, zeros))
    rImg = cv.merge(mv=(255*ones, zeros, zeros))

    blackImg = cv.merge(mv=(zeros, zeros, zeros))
    whiteImage = cv.merge(mv=(255*ones, 255*ones, 255*ones))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)
    plt.title('Blue')
    
    plt.subplot(232)
    plt.imshow(gImg)
    plt.title('Green')

    plt.subplot(233)
    plt.imshow(rImg)
    plt.title('Red')

    plt.subplot(234)
    plt.imshow(blackImg)
    plt.title('Black')

    plt.subplot(235)
    plt.imshow(whiteImage)
    plt.title('White')

    plt.show()

def bgrChannelGrayScale():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat.jpg')
    img = cv.imread(imgPath)
    b,g,r = cv.split(img)

    plt.figure()
    plt.subplot(131)
    plt.imshow(b, cmap='gray')
    plt.title('Blue Channel in Gray')

    plt.subplot(132)
    plt.imshow(g, cmap='gray')
    plt.title('Green Channel in Gray')

    plt.subplot(133)
    plt.imshow(r, cmap='gray')
    plt.title('Red Channel in Gray')

    plt.show()

def bgrChannelColor():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat.jpg')
    img = cv.imread(imgPath)
    b, g, r = cv.split(img)
    zeros = np.zeros_like(b)
    bImg = cv.merge((zeros, zeros, b))
    gImg = cv.merge((zeros, g, zeros))
    rImg = cv.merge((r, zeros, zeros))

    plt.figure()
    plt.subplot(131)
    plt.imshow(bImg)
    plt.title('Blue Channel')

    plt.subplot(132)
    plt.imshow(gImg)
    plt.title('Green Channel')

    plt.subplot(133)
    plt.imshow(rImg)
    plt.title('Red Channel')

    plt.show()

if __name__ == "__main__":
    # pureColors()
    # bgrChannelGrayScale()
    bgrChannelColor()