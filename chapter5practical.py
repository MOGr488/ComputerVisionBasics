import numpy as np
import cv2

# Create a 300x300 black canvas
canvas =  np.zeros((300,300,3), dtype=np.uint8)

# Draw the chess board pattern
for i in range(0,300,50):
    for j in range(0,300,50):
        canvas[i:i+25, j:j+25] = (255,255,255)
        canvas[i+25:i+50, j+25:j+50] = (255,255,255)


# Show the chess board image
cv2.imshow("Chess Board", canvas)

# Wait for user to press any key before closing the window
cv2.waitKey(0)

# Close all open windows
cv2.destroyAllWindows()
