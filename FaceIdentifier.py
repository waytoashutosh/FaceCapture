import cv2

face_cascade_obj = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")             #harcascade object 


image = cv2.imread("family.jpg",1)                                                          #keep as it is to finally frame the colorful screen
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)                                               #to conver into grayscale image


faces = face_cascade_obj.detectMultiScale(gray, scaleFactor = 1.09, minNeighbors=11)        #tweek scaleFactor and minNeighbors to identify accurately
print(faces)

for x,y,w,h in faces:
    image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),5)                                #making rectangles around faces

image = cv2.resize(image, (int(image.shape[1]/4),int(image.shape[0]/4)))

cv2.imshow("frame",image)
cv2.waitKey(0)
cv2.destroyAllWindows()