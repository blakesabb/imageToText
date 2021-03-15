"""
convert screenshot (of text) inside clipboard to text; places text in clipboard
"""
import clipboard
from PIL import ImageGrab
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#img = cv2.imread(r'C:\Users\blake\OneDrive\Desktop\pic.png')

image = ImageGrab.grabclipboard()
#print(image)
#image = image.save('reader.png', 'PNG')
#image.save()
image.save('paste.png', 'PNG')
imgReader = cv2.imread(r'C:\Users\blake\OneDrive\Documents\Programming\Python\Test\paste.png')
text = pytesseract.image_to_string(imgReader)

splitText = text.replace("\n", '')

print(splitText)

