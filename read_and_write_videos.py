import numpy as np
import cv2 as cv
import os

def videoFromWebcam():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if ret:
            cv.imshow('webcam', frame)
        
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def videoFromFile():
    root = os.getcwd()
    videoPath = os.path.join(root, 'videos\sample.mp4')
    cap = cv.VideoCapture(videoPath)

    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video', frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def writeVideoToFile():
    cap = cv.VideoCapture(0)

    fourcc = cv.VideoWriter_fourcc(*'XVID')
    root = os.getcwd()
    outPath = os.path.join(root, 'videos\webcam.avi')

    out = cv.VideoWriter(filename=outPath, fourcc=fourcc, fps=20.0, frameSize=(640,480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            out.write(frame)
            cv.imshow('webcam', frame)

        if cv.waitKey(1) == ord('q'):
            break
    
    cap.release()
    out.release()
    cv.destroyAllWindows()    

if __name__ == '__main__':
    # videoFromWebcam()
    # videoFromFile()
    writeVideoToFile()