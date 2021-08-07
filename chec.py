import pytesseract
from PIL import Image
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from tabulate import tabulate

#import selenium.webdriver
stuff=pytesseract.image_to_string(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))
#stuff=pytesseract.image_to_boxes(Image.open(r'C:\Users\jadej\OneDrive\Pictures\okokok.jpg'))

def func(str):
    return map[str]
stuffs=""
f=len(stuff)-1
for i in range(f):
    #print(stuff[i])
    if(stuff[i]=='\n'):
        print('hit')
        stuffs+=''
    else:
        stuffs+=stuff[i]

print(stuffs.split(','))
stuffs=stuffs.split(',')
map={}

options = Options()
options.page_load_strategy = 'eager'
driver = Chrome(options=options)


#driver.implicitly_wait(6)
for items in stuffs:
    driver.get("https://www.cosdna.com/eng/stuff.php")
    #print("h0")

    searchbar = driver.find_element(By.NAME,'q')

    #print("h1")

    searchbar.clear()
    searchbar.send_keys(items)
    #print(searchbar)
    #print("h2")

    x=driver.find_elements(with_tag_name('a').below(searchbar))
    #for i in x:
    #    print(i)
    #print(len(x))
    driver.find_element(By.TAG_NAME, 'button').click()

    #print("h3")

    searchbar = driver.find_element(By.NAME, 'q')
    x=driver.find_elements(with_tag_name('a').below(searchbar))

    driver.execute_script("arguments[0].scrollIntoView(true);", x[0])
    driver.execute_script("arguments[0].click();", x[0])

    try:
        searchbar = driver.find_element(By.NAME, 'q')
    except Exception as e:
        #print(items,' not found.')
        map[items]=-1
        print(items,' ',-1)
        continue

    x=driver.find_elements(with_tag_name('a').below(searchbar))

    #print("hp")
    #print(x[0].text)
    max=-1
    for i in x[0].text:
        if(i.isdigit()):
            max=int(i)
    map[items]=max
    print(items,' ',max)
    #print(map)
    #print("he")
    #print("h3 over")

stuffs.sort(key=func)
print('\n\n\n\n\n\nCOMPLETE TABLE')
print('________ _____')

data=[]
for i in stuffs:
    data.append([i,map[i]])

print(tabulate(data, headers=['Ingrediant name', 'safety rating']))


driver.quit()
