import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os

def greyHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat_dog.jpg')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.imshow(img, cmap='gray')

    hist = cv.calcHist(images=[img], channels=[0], mask=None, histSize=[256], ranges=[0,256])

    plt.figure()
    plt.plot(hist)
    plt.xlabel('Pixel Intensity')
    plt.ylabel('No. of plxels')

    plt.show()

def colorHistogram():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat_dog.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)

    colors = ['b', 'g', 'r']
    plt.figure()
    for i in range(len(colors)):
        hist = cv.calcHist([imgRGB], [i], None, [256], [0,256])
        plt.plot(hist, colors[i])

    plt.xlabel('Pixel Intensity')
    plt.ylabel('no. of plxels')

    plt.show()

if __name__ == '__main__':
    # greyHistogram()
    colorHistogram()