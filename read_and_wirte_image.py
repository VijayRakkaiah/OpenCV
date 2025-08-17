import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def readImage():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat_dog_1.jpg')
    img = cv.imread(imgPath)
    cv.imshow('window', img)
    cv.waitKey(0)

def writeImage():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat_dog_1.jpg')
    img = cv.imread(imgPath)
    outPath = os.path.join(root, 'images\output.jpg')
    cv.imwrite(outPath, img)


if __name__ == '__main__':
    # readImage()
    writeImage()