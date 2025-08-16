import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def hsvColorSegmentation():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    lowerBound = np.array([0, 0, 200])
    upperBound = np.array([20, 160, 250])
    mask = cv.inRange(hsv, lowerb=lowerBound, upperb=upperBound)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    cv.imshow('mask', mask)
    cv.waitKey(0)

if __name__ == '__main__':
    hsvColorSegmentation()