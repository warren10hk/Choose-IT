import json
import re

new_data = []
with open("formatted_data.json", "r") as input_file:
    data = json.loads(input_file.read())

for i in data:
    temp = {
        "Brand": i["brand"],
        "Model": i["model"],
        "Year": i["announced"]["year"],
        "Month": i["announced"]["month"],
        "Depth": i["apperance"]["depth"],
        "Height": i["apperance"]["height"],
        "Width": i["apperance"]["width"],
        "Weight": i["apperance"]["weight"],
        "Colors": ', '.join(i["apperance"]["colors"]),
        "Display_screen": i["display"]["screen"],
        "Screen_size": i["display"]["size"],
        "Screen_ratio": i["display"]["ratio"],
        "Screen_to_body_ratio": i["display"]["screen_to_body_ratio"],
        "Screen_ppi": i["display"]["PPI"],
        "Screen_resolution_x": i["display"]["reslolution"][0],
        "Screen_resolution_y": i["display"]["reslolution"][1],
        "Cpu": i["specification"]["CPU"],
        "Cpu_specification": i["specification"]["CPU_speed"],
        "Gpu": i["specification"]["GPU"],
        "Front_camera_resolution": ', '.join(map(str,i["specification"]["camera"]["front"]["resolution"])),
        "Front_camera_aperture": i["specification"]["camera"]["front"]["aperture"],
        "Rear_camera_resolution": ', '.join(map(str,i["specification"]["camera"]["rear"]["resolution"])),
        "Rear_camera_aperture": i["specification"]["camera"]["rear"]["aperture"],
        "Battery_Capacity": i["specification"]["battery"]["capacity"],
        "Removable_Battery": i["specification"]["battery"]["removable"],
        "Micro_sd": i["specification"]["card_slot"]["micro_sd"],
        "Sim_card": i["connectivity"]["SIM1"],
        "Dual_Sim_card": i["connectivity"]["dial_SIM"],
        "Hybrid_Sim_card": i["connectivity"]["hybrid_SIM"],
        "Radio": i["specification"]["radio"],
        "WLan": i["connectivity"]["WLAN"],
        "Gps": i["connectivity"]["GPS"],
        "Bluetooth": i["connectivity"]["bluetooth"],
        "NFC": i["connectivity"]["NFC"],
        "Infra_Red": i["connectivity"]["infrared_port"],
        "Operating_System": i["system"]["OS"],
        "Version": i["system"]["version"],
        "Fingerprint_Authentication": i["fingerprint"],
        
    }

    try:
        temp["Ram"] = ', '.join(map(str, i["specification"]["RAM"]))
    except TypeError:
        temp["Ram"] = i["specification"]["RAM"]
    
    try:
        temp["Rom"] = ', '.join(map(str, i["specification"]["ROM"]))
    except TypeError:
        temp["Rom"] = i["specification"]["ROM"]

    try:
        temp["Usb"] = i["connectivity"]["USB"]
    except:
        pass

    try:
        temp["2G_GSM"] = ', '.join(map(str,i["connectivity"]["2G_bands"]["GSM"]))
    except:
        pass

    try:
        temp["2G_CDMA"] = ', '.join(map(str,i["connectivity"]["2G_bands"]["CDMA"]))
    except:
        pass

    try:
        temp["3G_HSDPA"] = ', '.join(map(str,i["connectivity"]["3G_bands"]["HSDPA"]))
    except:
        pass
    
    try:
        temp["3G_CDMA"] = ', '.join(map(str,i["connectivity"]["3G_bands"]["CDMA"]))
    except:
        pass

    try:
        temp["4G_FDLTE"] = ', '.join(map(str,i["connectivity"]["4G_bands"]["FD-LTE"]))
    except:
        pass

    try:
        temp["4G_TDLTE"] = ', '.join(map(str,i["connectivity"]["4G_bands"]["TD-LTE"]))
    except:
        pass
    

    

    new_data.append(temp)

with open("formatted_data_new.json", "w") as output_file:
    json.dump(new_data, output_file)
    