import pytesseract
from PIL import Image


stuff=pytesseract.image_to_string(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))
#stuff=pytesseract.image_to_boxes(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))
print(stuff.split(','))
