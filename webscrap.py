import requests
from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.airliftexpress.com/search/daal")

# resource https://www.geeksforgeeks.org/extract-all-the-urls-from-the-webpage-using-python/
# https://stackoverflow.com/questions/64474877/unable-to-scrape-products-price-from-amazon
# https://stackoverflow.com/questions/55268753/scraping-amazon-products-names


#url = 'https://www.airliftexpress.com/search/daal'
#reqs = requests.get(url)
#soup = BeautifulSoup(reqs.content, 'html.parser')
soup = BeautifulSoup(driver.page_source, 'html.parser')
 
# urls = []
# p = soup.find_all('div', class_= "_41d2b9f3")
# for link in p:
    # b = link.find_all('a')
    # for i in b:
        # print("https://www.olx.com.pk"+i.get('href'))
        
# p = soup.find_all('div', class_= "_52497c97")
# for link in p:
    # b = link.find_all('span')
    # for i in b:
        # print(i.text)
        
#for x in soup.find_all('div', class_='product-card ng-star-inserted'):

#links = soup.find_all('div', class_='product-card ng-star-inserted')
    #for link in x:
a = soup.find_all("a", class_= 'cursor-pointer')
for i in a:
    print(i.get("href"))
