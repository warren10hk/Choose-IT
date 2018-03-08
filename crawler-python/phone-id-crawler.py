import requests
import re

base_url = "http://www.ringhk.com/index_phone_brandlist.php"

r = requests.get(base_url)
manufacturer_id_list = re.findall("brandID=(\d*)", r.text)

print "=== Manufacturer ID Retrieved ==="

base_url = "http://www.ringhk.com/index_phone_brandlist2.php?brandID="

for mid in manufacturer_id_list:
    r = requests.get(base_url+mid)
    phone_id_list = re.findall("index_phone_spec.php\?id=(\d*)", r.text)
    print list(set(phone_id_list))

print "=== Phone ID Retrieved ==="