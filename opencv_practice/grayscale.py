import cv2 as cv
import os

def grayscale():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat.jpg')
    img = cv.imread(imgPath)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow('Gray', imgGray)
    cv.waitKey(0)

def readAsGray():
    root = os.getcwd()
    imgPath = os.path.join(root, 'images\cat.jpg')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)

    cv.imshow('Gray', img)
    cv.waitKey(0)

if __name__ == '__main__':
    # grayscale()
    readAsGray()