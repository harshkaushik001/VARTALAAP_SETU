from PIL import Image
import os

img_path = os.path.join('images', 'a.png')  # Test with one file
if os.path.exists(img_path):
    img = Image.open(img_path)
    img.show()
else:
    print("Image not found:", img_path)
