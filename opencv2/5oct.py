import cv2 

image = cv2.imread("opencv2/RO-KO_image.jpg")

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
