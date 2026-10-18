from PIL import Image
import numpy as np

image = Image.open("image.jpg")

pixels = np.array(image)

print("Dimension of the image is:", pixels.shape)

print("Pixel value at (0, 0) is:", pixels[0, 0])

# Take 3 × 3 matrices from the image
a = pixels[:3, :3, 0].astype(np.int64)   # Red channel
b = pixels[:3, :3, 1].astype(np.int64)   # Green channel

print("\nMatrix A:")
print(a)

print("\nMatrix B:")
print(b)

print("\nMatrix operations")

print("1. Matrix addition:")
print(a + b)

print("2. Matrix subtraction:")
print(a - b)

print("3. Element-wise multiplication:")
print(a * b)

print("4. Element-wise division:")
print(a / b)

print("5. Matrix multiplication:")
print(a @ b)

print("6. Matrix transpose:")
print(a.T)

print("7. Matrix inverse:")
try:
    print(np.linalg.inv(a))
except np.linalg.LinAlgError:
    print("Matrix is singular and cannot be inverted.")

print("8. Matrix determinant:")
print(np.linalg.det(a))

print("9. Matrix rank:")
print(np.linalg.matrix_rank(a))

print("10. Matrix trace:")
print(np.trace(a))