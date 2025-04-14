import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('tester.png')

# Check if image was loaded successfully
if image is None:
    print("Error: Could not read the image file")
    print("Please check if the file exists and is in the correct format")
    exit(1)

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the image
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')
plt.show()
