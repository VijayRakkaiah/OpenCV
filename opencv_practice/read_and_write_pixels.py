import cv2 as cv
import os
import matplotlib.pylab as plt

def readAndWriteSinglePixel():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    eyePixel = imgRGB[230, 700]
    imgRGB[230, 700] = (255, 0, 0)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

def readAndWritePixelRegion():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    eyeRegion = imgRGB[218:248, 683:716]

    dx = 248-218
    dy = 716-683

    startX = 100
    startY = 660

    imgRGB[startX:startX+dx, startY:startY+dy] = eyeRegion
    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

if __name__ == "__main__":
    # readAndWriteSinglePixel()
    readAndWritePixelRegion()