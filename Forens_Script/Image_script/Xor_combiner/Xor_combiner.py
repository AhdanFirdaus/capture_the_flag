from PIL import Image
import numpy as np

# Load the two images
image1_path = 'layer1.png'
image2_path = 'layer2.png'

image1 = Image.open(image1_path)
image2 = Image.open(image2_path)

# Convert images to numpy arrays
img1_array = np.array(image1)
img2_array = np.array(image2)

# Ensure both images have the same size and shape
if img1_array.shape == img2_array.shape:
    # Perform XOR operation between the two images
    xor_result = np.bitwise_xor(img1_array, img2_array)

    # Convert result back to an image
    xor_image = Image.fromarray(xor_result)

    # Save XOR result image to file
    xor_image_path = 'xor_result.png'
    xor_image.save(xor_image_path)