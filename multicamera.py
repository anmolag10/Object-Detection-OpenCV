import numpy as np
import cv2
import threading
import time
global flag
flag = 0
def Cap():
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if(ret):
            cv2.imshow("frame",frame)
        if(cv2.waitKey(1) & 0xFF == 27):
            break
        if(flag == 1):
            break
    cap.release()
    cv2.destroyAllWindows()
def Cap1():
    cap1 = cv2.VideoCapture(2)
    while(cap1.isOpened()):
        ret1, frame1 = cap1.read()
        if(ret1):
            cv2.imshow("frame1",frame1)
        if(cv2.waitKey(1) & 0xFF == 27):
            break
        if(flag == 1):
            break
    cap1.release()
    cv2.destroyAllWindows()
if __name__ == '__main__':
    e1 = threading.Event()
    t = threading.Thread(target=Cap)
    t1 = threading.Thread(target=Cap1)
    t.start()
    t1.start()
try:
    while 1:
        time.sleep(.1)
except KeyboardInterrupt:
    flag = 1
    t.join()
    t1.join()