import cv2
image = cv2.imread('C://Users//DELL//OneDrive//Pictures//Documents//Desktop//AI//Intro_to_Computer_Vision___OpenCV_asset-e753 (2)//example.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resized_image = cv2.resize(gray_image,(224,224))
cv2.imshow('Processed Image', resized_image)
key = cv2.waitKey(0)
if key == ord('s'):
    cv2.imwrite('grayscale_resized_image')
    print("Image saved as grayscale_resized_image.jpg")
else:
    print("Image not saved")
cv2.destroyAllWindows()

print("Processed Image Dimensions: {resized_image.shape}")