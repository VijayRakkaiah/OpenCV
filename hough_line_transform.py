import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np

def houghLineTransform():
    root = os.getcwd()
    imgPath = os.path.join(root, r'images\car_road.jpg')
    img = cv.imread(imgPath, cv.IMREAD_GRAYSCALE)
    imgBlur = cv.GaussianBlur(img, (21,21), 3)
    cannyEdge = cv.Canny(imgBlur, 50, 160)

    plt.figure()
    plt.subplot(1, 4, 1)
    plt.imshow(img)

    plt.subplot(1, 4, 2)
    plt.imshow(imgBlur)

    plt.subplot(1, 4, 3)
    plt.imshow(cannyEdge)

    distResol = 1
    angleResol = np.pi/180
    threshold = 180
    lines = cv.HoughLines(cannyEdge, rho=distResol, theta=angleResol, threshold=threshold)

    k = 3000
    
    for curLine in lines:
        rho, theta = curLine[0]
        dhat = np.array([[np.cos(theta)], [np.sin(theta)]])
        d = rho * dhat
        lhat = np.array([[-np.sin(theta)], [np.cos(theta)]])
        p1 = d + k*lhat
        p2 = d - k*lhat
        p1 = p1.astype(int)
        p2 = p2.astype(int)
        cv.line(img, pt1=(p1[0][0], p1[1][0]), pt2=(p2[0][0], p2[1][0]), color=(255,255,255), thickness=10)

    plt.subplot(1, 4, 4)
    plt.imshow(img)

    plt.show()

if __name__ == '__main__':
    houghLineTransform() 