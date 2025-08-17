import cv2 as cv
import numpy as np
import os
import matplotlib.pyplot as plt

def callback():
    pass

def averageFiltering():
    root = os.getcwd()
    imgPath = os.path.join(root, r'images\car.jpg')
    img = cv.imread(imgPath)

    winName = 'avg filter'
    cv.namedWindow(winName)
    cv.createTrackbar('n', winName, 1, 100, callback)

    height, width, _ = img.shape
    scale = 1/4
    width = int(width * scale)
    height = int(height * scale)
    img = cv.resize(img, (width, height))

    while True:
        if cv.waitKey(1) == ord('q'):
            break

        n = cv.getTrackbarPos(trackbarname='n', winname=winName)
        imgFilter = cv.blur(img, (n,n))
        cv.imshow(winname=winName, mat=imgFilter)

    cv.destroyAllWindows()

if __name__ == '__main__':
    averageFiltering()