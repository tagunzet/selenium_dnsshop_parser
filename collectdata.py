import time
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
driver.set_window_position(-2000,0)
products = []
prices = []
final = []
num = 1
def urlsite():
    for num in range(6):
        if num == 0:
            continue
        url = f'https://www.dns-shop.ru/catalog/17a8950d16404e77/klaviatury/?p={num}'
        driver.get(url)
        time.sleep(3)
        parsingsite()
        time.sleep(3)
    #print(products)
    #print(prices)
    for i in range(len(products)):
        print(products[i] + prices[i])
    driver.quit()

def parsingsite():
    content = driver.page_source
    soup = BeautifulSoup(content, features='lxml')
    for item in soup.findAll('div', attrs={'class': 'products-list__content'}):
        # print(item)
        image2 = item.find_all('a', class_='catalog-product__name ui-link ui-link_black')
        # print(image2)
        for jj in image2:
            # print(str(jj))
            ag = jj.find("span")
            # print(ag)
            products.append(ag.text)
        czena = item.find_all('div', class_='product-buy__price')
        # print(czena)
        for i in czena:
            prices.append(str(i.text))
urlsite()
