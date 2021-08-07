import pytesseract
from PIL import Image
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

#import selenium.webdriver
stuff=pytesseract.image_to_string(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))
#stuff=pytesseract.image_to_boxes(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))

def func(str):
    return map[str]
stuffs=""
f=len(stuff)-1
for i in range(f):
    print(stuff[i])
    if(stuff[i]=='\n'):
        print('hit')
        stuffs+=''
    else:
        stuffs+=stuff[i]

print(stuffs.split(','))
stuffs=stuffs.split(',')
