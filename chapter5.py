import numpy as np
import cv2

# Building Canvas
canvas = np.zeros((300, 300, 3), dtype="uint8") # unsigned integer 8-bit

green = (0, 255, 0)
# Canvas, Starting point, Ending point, Line color
cv2.line(canvas, (0, 0), (300, 100), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

red = (0, 0, 255)
# Canvas, Starting point, Ending point, Line color, Line Thickness
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


# Rectangle
cv2.rectangle(canvas, (10, 10), (100, 60), green, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

blue = (255, 0, 0)
#  By specifying -1 as the thickness, our
#  rectangle is drawn as a solid blue.
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


canvas = np.zeros((300, 300, 3), dtype="uint8")
# Center of the circle
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)


for r in range(0, 100, 25):
    cv2.circle(canvas, (centerX, centerY), r, white, -1)


cv2.imshow("Canvas", canvas)
cv2.waitKey(0)


for i in range(0, 25):
    radius = np.random.randint(5, high = 200)
    color = np.random.randint(0, high = 256, size = (3,)).tolist()
    pt = np.random.randint(0, high = 300, size = (2,))

    cv2.circle(canvas, tuple(pt), radius, color, -1)

numbers = np.random.randint(0, high = 256, size = (3,)).tolist()

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
