from PIL import Image

# Number of images to combine
num_images = 603

# Dimensions of each image
image_width = 1
image_height = 603

# Create a new blank image with the combined size
combined_image = Image.new('RGBA', (num_images, image_height))

# Loop through each image and paste it into the combined image
for i in range(num_images):
    # Open the current image
    img = Image.open(f'pil_{i}.png')
    
    # Calculate the x-coordinate where this image will be pasted
    x = i * image_width
    
    # Paste the current image into the combined image
    combined_image.paste(img, (x, 0))

# Save the combined image
combined_image.save('combined_image.png')
