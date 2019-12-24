import face_learning as fl
import cv2
import time_save
import time_save as ts
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
cascade_path = '../opencv-master/data/haarcascades/haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascade_path)
a = 0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = faceCascade.detectMultiScale(gray, 1.1, 3)
    if len(face) > 0:
        for rect in face:
            x = rect[0]
            y = rect[1]
            w = rect[2]
            h = rect[3]
            wh = (x+w) - x
            hi = (y+h) - y
            if wh > 300 and hi > 300:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), thickness=5)

    cv2.imshow('frame',frame)  
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    if key == ord('s'):
        path = "photo.jpg"
        if wh > 300 and hi > 300:
            dst = frame[y:y+h,x:x+w]
            cv2.imwrite(path,dst)
            name = fl.face_read()
            if name is "none":
                print("認識できません")
            else:
                ts.save(name)
            

cap.release()
cv2.destroyAllWindows()
