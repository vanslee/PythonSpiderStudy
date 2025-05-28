import tesserocr  
from PIL import Image  
image = Image.open('C:\\Users\\Wu\\Desktop\\spider_web_py3\\image.png')  
print(tesserocr.image_to_text(image))

