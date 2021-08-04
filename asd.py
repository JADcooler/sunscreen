import pytesseract
from PIL import Image
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name
#import selenium.webdriver
stuff=pytesseract.image_to_string(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))
#stuff=pytesseract.image_to_boxes(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))
print(stuff.split(','))

driver = Chrome()
driver.get("https://www.cosdna.com/eng/stuff.php")
#driver.implicitly_wait(6)
print("h0")

searchbar = driver.find_element(By.NAME,'q')

print("h1")

searchbar.clear()
searchbar.send_keys('titanium')
print(searchbar)
print("h2")

x=driver.find_elements(with_tag_name('a').below(searchbar))
for i in x:
    print(i)
print(len(x))
driver.find_element(By.TAG_NAME, 'button').click()

print("h3")

searchbar = driver.find_element(By.NAME,'q')
x=driver.find_elements(with_tag_name('a').below(searchbar))
for i in x:
    print(i)
print(len(x))
x[0].click()
print("h3 over")
