"""
| Function | Explanation |
| cv2.VideoCapture(0) | Opens the default webcam. |
| cap.read() | Captures one video frame. |
| cv2.cvtColor()  | Converts the frame from color to grayscale. |
| detectMultiScale() | Detects faces in the image. |
| cv2.rectangle() | Draws a rectangle around each detected face. |
| cv2.imshow() | Displays the video. |
| cv2.waitKey(1) | Waits briefly for a keyboard input. |
| cap.release() | Releases the webcam. |
| cv2.destroyAllWindows() | Closes OpenCV windows. |
"""

import cv2
import  os 
"""
cap = cv2.VideoCapture(0)

ret,previous_frame  = cap.read()

if not ret:
    print("camera not found")
    cap.release()
    exit()

previous_gray = cv2.cvtColor(previous_frame, cv2.COLOR_BGR2GRAY)

previous_gray = cv2.resize(previous_gray, (21,21),0)

while True:
    ret ,frame = cap.read()
    if not ret:
        break 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    gray = cv2.resize(gray, (21,21),0)
    
    # capture the consecutive frames
    difference = cv2.absdiff(previous_gray, gray)
    
    theshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    
    cv2.imshow("original", frame)
    cv2.imshow("motion detection :", theshold)
    
    previous_gray = gray
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
"""
face_cascade = cv2.CascadeClassifier("opencv2/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    if not ret :
        print("camera not found")
        break
    
    # convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #detect faces :
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    
    # draw rectangles around faces
    
    for  (x,y,w,h) in faces :
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    
    # display the frame
    cv2.imshow("face detection", frame)
    
    # wait key  : 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
cap.release()
cv2.destroyAllWindows()
    

