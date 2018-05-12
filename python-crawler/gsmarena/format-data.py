import json
import re

new_data = []
with open("unformatted-data.json", "r") as input_file:
    data = json.loads(input_file.read())

for i in data:
    temp = {
        "brand": i["brand"],
        "model": i["model"],
        "announced": {
            "year": re.findall("\d{4}", i["Announced"])[0],
            "month": ""
        },
        "apperance": {
            "depth": i["Dimension (Depth)"],
            "height": i["Dimension (Height)"],
            "width": i["Dimension (Width)"],
            "weight": i["Weight"],
            "colors": i["Colors"].split(',')
        },
        "display": {
            "screen": i["Screen"],
            "size": i["Screen Size"],
            "ratio": i["Ratio"],
            "screen_to_body_ratio": i["Screen To Body Ratio"],
            "PPI": i["PPI"],
            "reslolution": [i["Resolution (Height)"], i["Resolution (width)"]]
        },
        "specification": {
            "CPU": i["Chipset"],
            "CPU_speed": i["CPU Speed"],
            "GPU": i["GPU"],
            "RAM": i["RAM"],
            "ROM": i["ROM"],
            "camera": {
                "front": {
                    "resolution": [i["Front Camera 1"], i["Front Camera 2"]],
                    "aperture": i["Front Camera f"]
                },
                "rear":  {
                    "resolution": [i["Rear Camera 1 Resolution"], i["Rear Camera 2"], i["Rear Camera 3"]],
                    "aperture": i["Rear Camera 1 f"]
                }
            },
            "battery": {
                "capacity": i["Battery Capacity"],
                "removable": i["Battery Removable"]
            },
            "radio": i["Radio"],
            "USB": i["USB"],
            "card_slot": {
                "micro_sd": i["Card Slot"],
                "max": i["microSD Max"],
                "dedicated": i["Dedicated SD Card Slot"]
            }
        },
        "connectivity": {
            "2G_bands": {
                "GSM": re.findall("\d+", i["2G bands"])
            },
            "3G_bands": {
                "HSDPA": re.findall("\d+", i["3G bands"])
            },
            "4G_bands": {
                "FD-LTE": re.findall("\((\d+)\)", i["4G bands"])
            },
            "SIM1": i["SIM 1"],
            "SIM2": i["SIM 2"],
            "dial_SIM": i["Dual Sim"],
            "hybrid_SIM": i["Hybrid SIM"],
            "WLAN": i["WLAN"],
            "GPS": "",
            "bluetooth": i["Bluetooth"],
            "NFC": i["NFC"],
            "3.5mm jack": i["3.5mm jack"],
            "Infrared port": i["Infrared port"]
        },
        "system": {
            "OS": i["OS"],
            "version": i["Version"]
        },
        "fingerprint": i["Fingerprint"]
    }
    try:
        temp["announced"]["month"] = re.findall("(January|February|March|April|May|June|July|August|September|October|November|December)", i["Announced"])[0]
    except:
        pass
    new_data.append(temp)

with open("formatted_data.json", "w") as output_file:
    json.dump(new_data, output_file)
    