import tesserocr
from PIL import Image

image = Image.open('img.jpg')
result = tesserocr.image_to_text(image)

print(result)
