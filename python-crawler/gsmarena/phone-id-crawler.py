import requests
import re
from bs4 import BeautifulSoup

base_url = "https://www.gsmarena.com/makers.php3"
manufacturer_id_list = []

r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html5lib")
for i in soup.table.find_all('a'):
    manufacturer_id_list.append([i.findAll(text=True)[0], i.get('href').strip()])

print ("=== Manufacturer ID Retrieved ===")

base_url = "https://www.gsmarena.com/"

with open("phone-url-list.txt", "w") as output_file:
    for name, suffix in manufacturer_id_list:
        print ("===", name, "===")
        output_file.write(">"+name+"\n")

        r = requests.get(base_url+suffix)
        soup = BeautifulSoup(r.text, "html5lib")
        for i in soup.find(id='review-body').find_all('a'):
            # print (i.get('href').strip())
            output_file.write(i.get('href').strip()+"\n")

print ("=== Phone ID Retrieved ===")
