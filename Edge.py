import cv2
import numpy as np
import matplotlib.pyplot as plt


def display_image(title, image):
    "Utility function to display an image."
    plt.figure(figsize=(8, 8))
    if len(image.shape) ==2:
        plt.imshow(image, cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()


def interactive_edge_detection(image_path):
    "Interactive activity for edge detection and  filtering."
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found!")
        return
   
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    display_image("Original Grayscale Image", gray_image)


    print("Select an option:!")
    print("1. Sobel Edge Detection")
    print("2.Canny Edge Detection")
    print("3. Laplacian Edge Detection")
    print("4. Gaussian Smoothing")
    print("5. Median Filtering")
    print("6. Exit")


    while True:
        choice = input("Enter your choice (1-6):")


        if choice == "1":


            soblex = cv2.SObel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobely = cv2.SObel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
            combined_sobel = cv2.bitwise_or(soblex.astype(np.uint8), sobely.astype)
            display_image("Sobel Edge Detection", combined_sobel)
       
        elif choice == "2":
        # Canny Edge Detection
            print("Adjust thresholds for Canny (default: 100 and 200)")
            lower_thresh = int(input("Enter lower threshold: "))
            upper_thresh = int(input("Enter upper threshold: "))
            edges = cv2.Canny(gray_image, lower_thresh, upper_thresh)
            display_image("Canny Edge Detection", edges)


        elif choice == "3":
        # Laplacian Edge Detection
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            display_image("Laplacian Edge Detection", np.abs(laplacian).astype(np.uint8))


        elif choice == "4":
        # Gaussian Smoothing
            print("Adjust kernel size for Gaussian blur (must be a positive odd number, default: 5)")
            try:
                kernel_size = int(input("Enter kernel size (odd number): "))
                if kernel_size <= 0 or kernel_size % 2 == 0:
                    print("Invalid kernel size! Must be a positive odd number. Using default (5).")
                    kernel_size = 5
            except ValueError:
                print("Invalid input! Using default kernel size (5).")
                kernel_size = 5
            blurred = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
            display_image("Gaussian Smoothed Image", blurred)


        elif choice == "5":
        # Median Filtering
            print("Adjust kernel size for Median filtering (must be odd, default: 5)")
            kernel_size = int(input("Enter kernel size (odd number): "))
            median_filtered = cv2.medianBlur(image, kernel_size)
            display_image("Median Filtered Image", median_filtered)


        elif choice == "6":
            print("Exiting...")
            break


        else:
            print("Invalid choice. Please select a number between 1 and 6.")


# Provide the path to an image for the activity
interactive_edge_detection('C://Users//DELL//Downloads//Image_annotation-template_AIEPCM2L3A1-8d3f//example.jpg')

