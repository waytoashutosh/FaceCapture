import cv2

video = cv2.VideoCapture(0)                 # 0 is the camera number


while True:                                    
    check, frame = video.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)

    if key ==ord('x'):
        break

video.release()
cv2.destroyAllWindows()