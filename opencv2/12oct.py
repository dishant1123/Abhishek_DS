

import cv2
import os
import time

# Load Haar Cascade XML file
xml_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "haarcascade_frontalface_default.xml"
)

face_cascade = cv2.CascadeClassifier(xml_path)

if face_cascade.empty():
    print("Error: Haar Cascade XML file not loaded.")
    raise SystemExit

# Try DirectShow first, then MSMF
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    cap.release()
    cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

if not cap.isOpened():
    print("Error: Webcam could not be opened.")
    raise SystemExit

# Allow the camera to initialize
time.sleep(2)

# Read frames until a valid frame is received
frame = None

for attempt in range(10):
    ret, frame = cap.read()

    if ret and frame is not None:
        break

    time.sleep(0.3)

if frame is None or not ret:
    print("Unable to capture frame.")
    cap.release()
    raise SystemExit

print("Camera started successfully. Press Q to exit.")

try:
    while True:
        ret, frame = cap.read()

        if not ret or frame is None:
            print("Unable to capture frame. Check your webcam.")
            break

        # Convert to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw rectangles
        for (x, y, w, h) in faces:
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                "Face Detected",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()

"""
| Function | Explanation |
| cv2.VideoCapture(0)` | Opens the default webcam. |
| cap.read()` | Captures one video frame. |
| cv2.cvtColor()` | Converts the frame from color to grayscale. |
| detectMultiScale()` | Detects faces in the image. |
| cv2.rectangle()` | Draws a rectangle around each detected face. |
| cv2.imshow()` | Displays the video. |
| `cv2.waitKey(1)` | Waits briefly for a keyboard input. |
| `cap.release()` | Releases the webcam. |
| `cv2.destroyAllWindows()` | Closes OpenCV windows. |
"""

# ex:2 
"""
import cv2

image = cv2.imread("opencv2/cat_2.jpeg")

cv2.rectangle(
    image,
    (100, 50),
    (300, 250),
    (0, 255, 0),
    2
)

cv2.imshow("Rectangle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()"""


"""import cv2

# Read image
img = cv2.imread("opencv2/example-of-2d-shapes.png")

if img is None:
    print("Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur to remove noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blur, 50, 150)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:

    area = cv2.contourArea(cnt)

    # Ignore small noise
    if area > 400:

        # Perimeter
        peri = cv2.arcLength(cnt, True)

        # Approximate shape
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        corners = len(approx)
        print(corners)
        x, y, w, h = cv2.boundingRect(approx) # x, y is the top-left corner of the bounding box

        if corners == 3:
            shape = "Triangle"
        elif corners == 4:
            shape = "Rectangle"
        elif corners == 5:
            shape = "Pentagon"
        else:
            shape = "Circle"



        # -------- DRAW SHAPE --------
        if corners > 6:
            (cx, cy), radius = cv2.minEnclosingCircle(cnt)
            center = (int(cx), int(cy))
            radius = int(radius)
            cv2.circle(img, center, radius, (0, 0, 255), 5)
            cv2.putText(img, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        else:
            cv2.drawContours(img, [approx], -1, (0, 0, 255), 5)
            cv2.putText(img, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

# Show final result
cv2.imshow("Shape Detection System", img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

