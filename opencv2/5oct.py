import cv2 

"""image = cv2.imread("opencv2/RO-KO_image.jpg")

# resize : 
resized = cv2.resize(image,(800,1800)) 

# rotate : 
rotated = cv2.rotate(
    resized,
    cv2.ROTATE_90_CLOCKWISE
)

# flip :
flipped = cv2.flip(rotated,1)

cv2.imshow("original",image)
# cv2.imshow("final_image :",flipped)
cv2.imshow("resized",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

# blur , edge detection, canny edge detection,gaussian blur

image = cv2.imread("opencv2/gettyimages-2242831732-612x612.jpg")

# convert to grayscale

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

# apply gaussian blur : imgae smooting technique  ----> used  to reduce the noise and small unwanted details
# blur = cv2.GaussianBlur(gray,(9,9),0)  # ----> 9,9  ----> kernel size  0 ---> is  SD

# canny edge detection : 
"""
its alogorithm  used to detect boundaries of objects in an image
"""
# edges =cv2.Canny(blur,50,150)  # 100,200 ---> lower and upper threshold

# blurred : 
# blurred = cv2.blur(gray,(5,5))

# crop  : 

crop = image[100 :300 , 150:400]

cv2.imshow("original",image)
# cv2.imshow("gray",gray) 
# cv2.imshow("blur",blur)
# cv2.imshow("edges",edges)
# cv2.imshow("blurred",blurred)
cv2.imshow("crop",crop)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

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
# face_cascade = cv2.CascadeClassifier("opencv2/haarcascade_frontalface_default.xml")

# cap = cv2.VideoCapture(0)

"""
