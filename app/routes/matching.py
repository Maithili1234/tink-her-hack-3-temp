import cv2
import os
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim  # For SSIM
import numpy as np

# Paths to the images
image1_path = "C:/Users/maith/OneDrive/Pictures/skirt.jpg"
image2_path = "C:/Users/maith/OneDrive/Pictures/frock.jpg"  # Replace with your second image path

# Define the SSIM threshold
SSIM_THRESHOLD = 0.95  # Adjust based on your requirement (closer to 1 for stricter comparison)

# Check if files exist
if not os.path.exists(image1_path):
    print(f"Error: {image1_path} does not exist.")
elif not os.path.exists(image2_path):
    print(f"Error: {image2_path} does not exist.")
else:
    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Check if both images are loaded successfully
    if image1 is None or image2 is None:
        print("Error: Could not load one or both images. Check the file paths and formats.")
    else:
        # Convert images to grayscale for comparison
        gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

        # Ensure the images have the same size (resize if necessary)
        if gray1.shape != gray2.shape:
            gray2 = cv2.resize(gray2, (gray1.shape[1], gray1.shape[0]))

        # Calculate SSIM (Structural Similarity Index)
        score, diff = ssim(gray1, gray2, full=True)
        print(f"SSIM Score: {score:.4f}")  # Closer to 1 means more similar

        # Check if images are the same based on the threshold
        if score >= SSIM_THRESHOLD:
            print("The images are the same (similarity exceeds the threshold).")
        else:
            print("The images are different (similarity below the threshold).")

        # Optional: Visualize the difference
        diff = (diff * 255).astype("uint8")
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 3, 1)
        plt.title("Image 1")
        plt.imshow(cv2.cvtColor(image1, cv2.COLOR_BGR2RGB))
        plt.axis("off")
        plt.subplot(1, 3, 2)
        plt.title("Image 2")
        plt.imshow(cv2.cvtColor(image2, cv2.COLOR_BGR2RGB))
        plt.axis("off")
        plt.subplot(1, 3, 3)
        plt.title("Difference")
        plt.imshow(diff, cmap="gray")
        plt.axis("off")
        plt.show()
