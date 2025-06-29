import cv2

# Load the image
image = cv2.imread('thisen.png')

# Convert to gray scale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_gray = 255 - gray_image

# Blur the inverted image
blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

# Invert the blurred image
inverted_blur = 255 - blurred

# Create the pencil sketch
pencil_sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

# Save and show the result
cv2.imwrite('pencil_sketch.jpg', pencil_sketch)
cv2.imshow('Pencil Sketch', pencil_sketch)
cv2.waitKey(0)
cv2.destroyAllWindows()
