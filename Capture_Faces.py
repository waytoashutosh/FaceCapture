import cv2


def fun():
    face_cascade_obj = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")             #harcascade object 
    video = cv2.VideoCapture(0)                                                                 # 0 is the camera number


    while True:                                    
        check, frame = video.read()                                 #check return true if frames are created successfully

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)               #to convert into grayscale image

        
        faces = face_cascade_obj.detectMultiScale(gray, scaleFactor = 1.05, minNeighbors=11)
        
        for x,y,w,h in faces:
            frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)   #rectangle(frame, topLeft, BottomRight, x+width, y+depth, colorOfLine, widhtOfLine)

        cv2.imshow("frame", frame)
        key = cv2.waitKey(1)

        if key ==ord('x'):
            break

    video.release()
    cv2.destroyAllWindows()


def main():
    #Video Frame to indentify Human Faces
    print("Press X to close the window!!!")
    fun()

main()
