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