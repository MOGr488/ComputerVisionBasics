import numpy as np
import argparse
import cv2
from matplotlib import pyplot as plt


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

eq = cv2.equalizeHist(image)

cv2.imshow("Histogram Equalization", np.hstack([image, eq]))




# cv2.calcHist(images,channels,mask,histSize,ranges)
hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()


histo = cv2.calcHist([eq], [0], None, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram with Equalization")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
plt.plot(histo)
plt.xlim([0, 256])
plt.show()


