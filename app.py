from PIL import Image
import numpy as np
image=Image.open("image.jpg")
pixels =np.array(image).astype(np.int64)
dim=pixels.shape
print("Image dimensions:", dim)
print("Pixel value at (0, 0):", pixels[0, 0])