from selenium import webdriver
import time
from urllib.request import urlopen ,urlretrieve
import random

web_driver = webdriver.Chrome()
web_driver.get("https://www.google.com/search?biw=1366&bih=625&tbm=isch&sa=1&ei=fCwWXebIHMWvyAPMw6PQAQ&q=dhoni+face&oq=dhoni+face&gs_l=img.3..0l7.7845.8977..9432...0.0..0.239.825.0j3j2......0....1..gws-wiz-img.......0i67.nwRfq2wwhSU")
list_of_links=[]

links = web_driver.find_elements_by_class_name("rg_l")
print(len(links))
for link in links:
    try:
        list_of_links.append(link.get_attribute("href"))
    except Exception as e:
        print("not found")
        
time.sleep(2)
print(list_of_links)
web_driver.close()
    


def downloader(image_url):
    file_name = random.randrange(1,10000)
    full_file_name = str(file_name) + '.jpg'
    urlretrieve(image_url,full_file_name)


for url in list_of_links:
    downloader(url)
