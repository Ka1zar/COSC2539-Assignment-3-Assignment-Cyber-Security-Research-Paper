import cv2
import hashlib

# Step 1: Load the image
image_path = "C:/Users/Nguye/OneDrive/Documents/IRL/COSC2539 Security new/AS3/cocoapi-master/cocoapi-master/PythonAPI/Hash test/manjpg.jpg"  # Replace with your image file
image = cv2.imread(image_path)

# Step 2: Generate a hash for the original image
def generate_hash(image):
    # Convert the image to bytes
    image_bytes = image.tobytes()
    # Use SHA-256 to generate a hash
    return hashlib.sha256(image_bytes).hexdigest()

original_hash = generate_hash(image)
print(f"Original Hash: {original_hash}")

# Step 3: Simulate an image change (alter a pixel)
modified_image = image.copy()
modified_image[0, 0] = [255, 255, 255]  # Change the top-left pixel to white

# Save the modified image
modified_image_path = "C:/Users/Nguye/OneDrive/Documents/IRL/COSC2539 Security new/AS3/cocoapi-master/cocoapi-master/PythonAPI/Hash test/modified_image.jpg"
cv2.imwrite(modified_image_path, modified_image)
print(f"Modified image saved to: {modified_image_path}")

# Step 4: Generate a hash for the modified image
modified_hash = generate_hash(modified_image)
print(f"Modified Hash: {modified_hash}")

# Step 5: Compare hashes
if original_hash == modified_hash:
    print("The image has not been altered.")
else:
    print("The image has been altered!")
