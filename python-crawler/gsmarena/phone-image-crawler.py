import requests
import re
from bs4 import BeautifulSoup
import json
import time

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
raw_data_dict = []

for brand in suffix_dict:
    try:
        print ("===", brand, "===")
        raw_data_dict = []
        for suffix in suffix_dict[brand]:
            r = requests.get(base_url+suffix)
            soup = BeautifulSoup(r.text, "html5lib")

            phone_details = {
                'model': soup.find_all("h1", {"data-spec": "modelname"})[0].find_all(text=True)[0],
                'image': soup.find_all("div", {"class": "specs-photo-main"})[0].find_all("img")[0]['src']
            }
            print ("Crawling:", phone_details['model'])
            raw_data_dict.append(phone_details)
    except:
        print ("Error, try again in 10 seconds.")
        time.sleep(10)

with open("phone-data-photo.json", "w") as output_file:
    json.dump(raw_data_dict, output_file)
