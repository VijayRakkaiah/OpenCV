import cv2 as cv
import os
import numpy as np
import matplotlib.pyplot as plt

def imageGradient():
    root = os.getcwd()
    imgPath = os.path.join(root, r'images\car.jpg')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)

    plt.figure()
    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')

    laplacian = cv.Laplacian(img, cv.CV_64F, ksize=21)
    plt.subplot(2, 2, 2)
    plt.imshow(laplacian, cmap='gray')

    sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=21)
    plt.subplot(2, 2, 3)
    plt.imshow(sobelX, cmap='gray')
    kx, ky = cv.getDerivKernels(1, 0, 3)
    print(ky@kx.T)

    sobelY = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=21)
    plt.subplot(2, 2, 4)
    plt.imshow(sobelY, cmap='gray')
    kx, ky = cv.getDerivKernels(0, 1, 3)
    print(ky@kx.T)

    plt.show()



if __name__ == '__main__':
    imageGradient()