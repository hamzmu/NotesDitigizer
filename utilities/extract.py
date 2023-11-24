import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = r"C:\Users\muhha\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

img = Image.open('1.jpg')
text = pytesseract.image_to_string(img)
print(text)
