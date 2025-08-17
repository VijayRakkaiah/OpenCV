import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def harrisCorner():
    root = os.getcwd()
    imgPath = os.path.join(root, r'images\car.jpg')
    img = cv.imread(imgPath)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgGray = np.float32(imgGray)

    plt.figure()
    plt.subplot(131)
    plt.imshow(imgGray, cmap='gray')

    plt.subplot(132)
    blockSize = 3
    sobelSize = 3
    k = 0.05
    harris = cv.cornerHarris(src=imgGray, blockSize=blockSize, ksize=sobelSize, k=k)
    plt.imshow(harris, cmap='jet')

    plt.subplot(133)
    threshold = 0.05
    imgRGB[harris > threshold * harris.max()] = [255, 0, 0]
    plt.imshow(imgRGB)

    plt.show()

if __name__ == '__main__':
    harrisCorner()