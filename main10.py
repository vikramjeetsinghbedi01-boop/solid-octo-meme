import cv2 
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('C://Users//DELL//OneDrive//Pictures//Documents//Desktop//AI//Intro_to_Computer_Vision___OpenCV_asset-e753 (2)//example.jpg')
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

(h, w) = image.shape[:2]
centre = (w//2, h//2)
M = cv2.getRotationMatrix2D(centre, 45, 1.0)
rotated = cv2.warpAffine(image, w, (h, m))

rotated_rgb = cv2.cvtColor(rotated, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
brighter = cv2.add(image,brightness_matrix)

brighter_rgb = cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)
plt.imshow(brighter-rgb)
plt.title("Brighter Image")
plt.show()
