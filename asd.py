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

print(stuff.split(','))

map={}

options = Options()
options.page_load_strategy = 'eager'
driver = Chrome(options=options)
driver.get("https://www.cosdna.com/eng/stuff.php")
#driver.implicitly_wait(6)
print("h0")

searchbar = driver.find_element(By.NAME,'q')

print("h1")

searchbar.clear()
searchbar.send_keys('asdasdasdasd')
print(searchbar)
print("h2")

x=driver.find_elements(with_tag_name('a').below(searchbar))
for i in x:
    print(i)
print(len(x))
driver.find_element(By.TAG_NAME, 'button').click()

print("h3")

searchbar = driver.find_element(By.NAME, 'q')
x=driver.find_elements(with_tag_name('a').below(searchbar))
for i in x:
    print(i.text)


print(len(x))

driver.execute_script("arguments[0].scrollIntoView(true);", x[0])
driver.execute_script("arguments[0].click();", x[0])
searchbar = driver.find_element(By.NAME, 'q')
x=driver.find_elements(with_tag_name('a').below(searchbar))

print("hp")
print(x[0].text)
max=-1
for i in x[0].text:
    if(i.isdigit()):
        max=int(i)
map['asdasdasdasd']=max
print(map)
print("he")
print("h3 over")
#driver.quit()
