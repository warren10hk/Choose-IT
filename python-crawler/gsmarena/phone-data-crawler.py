import requests
import re
from bs4 import BeautifulSoup
import json

suffix_dict = {}

with open("phone-url-list.txt", "r") as input_file:
    brand = ""
    for line in input_file:
        if line[0] == ">":
            brand = line[1:].strip()
            suffix_dict[brand] = []
        else:
            suffix_dict[brand].append(line.strip())

base_url = "https://www.gsmarena.com/"
raw_data_dict = {}

for brand in suffix_dict:
    print ("===", brand, "===")
    raw_data_dict[brand] = []
    for suffix in suffix_dict[brand]:
        phone_details = {}
        r = requests.get(base_url+suffix)
        soup = BeautifulSoup(r.text, "html5lib")
        spec_list = soup.find_all(id="specs-list")[0]
        for item in spec_list.find_all('tr'):
            try:
                attribute = item.find_all("td", {"class": "ttl"})[0].find_all(text=True)[0]
                phone_details[attribute] = item.find_all("td", {"class": "nfo"})[0].find_all(text=True)
            except:
                pass
        phone_details['brand'] = brand
        phone_details['model'] = soup.find_all("h1", {"data-spec": "modelname"})[0].find_all(text=True)[0]
        print ("Crawling:", phone_details['model'])
        raw_data_dict[brand].append(phone_details)

with open("phone-data-raw.json", "w") as output_file:
    json.dump(raw_data_dict, output_file)
