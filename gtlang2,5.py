# -*- coding: utf-8 -*-

from ast import Try
import json
from re import I

tier = {
    'Electric Motor': 'Elektrikli Motor',
    'Electric Piston': 'Elektrikli Piston',
    'Electric Pump': 'Elektrikli Pompa',
    'Conveyor Module': 'Konveyör Modülü',
    'Robot Arm': 'Robot Kol',
    'Emitter': 'Yayıcı',
    'Sensor': 'Sensör',
    'Field Generator': 'Alan Oluşturucu'
}

trvword = {
    '(ULV)',    # Ultra Low Voltage - 8
    '(LV)',     # Low Voltage - 32
    '(MV)',     # Medium Voltage - 128
    '(HV)',     # High Voltage - 512
    '(EV)',     # Extreme Voltage - 2048
    '(IV)',     # Insane Voltage - 8192
    '(LuV)',    # Ludicrous Voltage - 32768
    '(ZPM)',    # ZPM Voltage - 131072
    '(UV)',     # Ultimate Voltage - 524288
    '(UHV)',    # Highly Ultimate Voltage - 2097152
    '(UEV)',    # Extremely Ultimate Voltage - 8388608
    '(UIV)',    # Insanely Ultimate Voltage - 33554432
    '(UMV)',    # Mega Ultimate Voltage - 134217728
    '(UXV)',    # Extended Mega Ultimate Voltage - 536870912
    '(MAX)'     # Maximum Voltage - 2147483647
}

def main():
    with open('GregTech.lang', 'r', encoding="utf-8") as f:
        lines = f.read().splitlines()
    properties = []
    rest = []
    in_languagefile_category = True
    found_material = False
    count = 0
    for line in lines:
        if not in_languagefile_category:
            if line.startswith("languagefile {"):
                in_languagefile_category = True
            continue

        # in_languagefile_category == True
        if line.startswith("}"):
            break
        split = line.split("=", 1)
        key = split[0]
        s_key = f"gt-lang|{key}"
        try:
            value = split[1]
        except:
            value = "31haha"
            
        for item in tier:
            if item in value:
                for machine in trvword:
                    if machine in value and item + " " + machine == value:
                        count = count + 1
                        properties.append({
                            'key': s_key,
                            'original': value,
                            'translation': tier[item] + " " + machine,
                            'stage': 5,
                            'context': s_key + '=' + value,
                        })
    print(count)
            

    with open('gtlang.txt', mode="wt", encoding="utf-8") as f:
        for line in properties:
            f.write(line['context'] + '\n')

    with open('GregTech.lang.json', mode="wt", encoding="utf-8") as f:
        json.dump(properties, f, ensure_ascii=False, indent=2)

    with open('rest.txt', mode="wt", encoding="utf-8") as f:
        for line in rest:
            f.write(line + '\n')

if __name__ == '__main__':
    main()