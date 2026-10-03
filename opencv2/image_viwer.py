"""
1. read image : cv2.imread()
2. display image : cv2.imshow()
3. save image : cv2.imwrite()
4. wait for key : cv2.waitKey()
5. close windows : cv2.destroyAllWindows()
6. convert color to grayscale : cv2.cvtColor()
7. shape of image : image.shape
================================================================================

resize  the image : 

1. cv2.resize(image, (width, height))
2. maintain the  image  quality  : 
    3 methods : 
        | Method        | Use                           |
        | --------------| ----------------------------- |
        | INTER_NEAREST | Fast, low quality             |
        | INTER_LINEAR  | General resizing              |
        | INTER_CUBIC   | Better quality when enlarging |
        | INTER_AREA    | Good for reducing image size  |

3. bule , green , red :cv2.split()

"""

import cv2

# read image  : 

"""image = cv2.imread("open_cv2_image_view/cat_2.jpeg")

if image is  None:
    print("image is not found") 
else :
    # shape of image : 
    print(image.shape)
    hieght ,width,channel = image.shape
    print("image hieght : ",hieght)
    print("image width : ",width)
    print("image channel : ",channel)
    
    # convert grayscale :
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
   
    # save image :
    cv2.imwrite("open_cv2_image_view/cat_2_gray.jpeg", gray_scale)
    
    # show image :
    cv2.imshow("image", image)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
"""

# resize the image : 
"""image = cv2.imread("open_cv2_image_view/cat_2.jpeg")
if image is  None:
    print("image is not found") 
else :
    # shape of image : 
    print(image.shape)
    hieght ,width,channel = image.shape
    print("image hieght : ",hieght)
    print("image width : ",width)
    print("image channel : ",channel)
    
    # resize the image :
    resized_image = cv2.resize(image,(224,224),interpolation = cv2.INTER_CUBIC)
    
    # image quality :
    
    # save image :
    cv2.imwrite("open_cv2_image_view/cat_2_resize.jpeg", resized_image)
    
    # show image :
    cv2.imshow("image", resized_image)
    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows()
"""
# object detection :
