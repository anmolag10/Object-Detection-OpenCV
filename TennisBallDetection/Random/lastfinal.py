import cv2
import numpy as np
conval=list()
hfval=list()
def nothing(x):
    pass
cap = cv2.VideoCapture(0);
aratio=1
cv2.namedWindow("Track")
cv2.createTrackbar("LH", "Track", 0, 255, nothing)
cv2.createTrackbar("LS", "Track", 0, 255, nothing)
cv2.createTrackbar("LV", "Track", 0, 255, nothing)
cv2.createTrackbar("UH", "Track", 255, 255, nothing)
cv2.createTrackbar("US", "Track", 255, 255, nothing)
cv2.createTrackbar("UV", "Track", 255, 255, nothing)

while True:
    ret, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #hsv = cv2.GaussianBlur(hsv, (5, 5), 0)

    lh = cv2.getTrackbarPos("LH", "Track")
    ls = cv2.getTrackbarPos("LS", "Track")
    lv = cv2.getTrackbarPos("LV", "Track")

    uh = cv2.getTrackbarPos("UH", "Track")
    us = cv2.getTrackbarPos("US", "Track")
    uv = cv2.getTrackbarPos("UV", "Track")

    savekey = cv2.waitKey(1)
    if savekey == 115:
        lowerball = np.array([lh, ls, lv])
        upperball = np.array([uh, us, uv])
        print(lowerball)
        print(upperball)

    lowerball = np.array([25, 53, 61])
    upperball = np.array([61, 255, 255])
    kernal = np.ones((2, 2), np.uint8) / 4
    mask = cv2.inRange(hsv, lowerball, upperball)
    mask = cv2.dilate(mask, kernal)
    mask = cv2.filter2D(mask, -1, kernal)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    resgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(resgray, 127, 255, 0)
    conts, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    if len(conts)>0:
      for c in conts:
        r= cv2.minAreaRect(c)
        if(r[1][1]==0):
             pass
        else:
            rati0=r[1][0]/r[1][1]


    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=50, param2=20, minRadius=20, maxRadius=50)
    if circles is not None:

      detectedcircles=np.uint16(np.around(circles))
      for (x,y,r) in detectedcircles[0,:]:



             if( r>0.88 and  r<1.1):
               cv2.circle(frame,(x,y),r1,(0,255,255),3)

               cv2.putText(frame,'*BALL DETECTED*', (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (25, 2, 100), 1)



    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)
    #cv2.imshow("hsv",hsv)
    key = cv2.waitKey(1)
    if key == 27:
        break
print(r1)
print(r)
cap.release()
cv2.destroyAllWindows()
#MIGHT NOT WORK FOR MULTIPLE BALLS IN SOME SITUTATIONS
