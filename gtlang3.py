from ast import Try
import json
from re import I

tier = {
    'ULV',    # Ultra Low Voltage - 8
    'LV',     # Low Voltage - 32
    'MV',     # Medium Voltage - 128
    'HV',     # High Voltage - 512
    'EV',     # Extreme Voltage - 2048
    'IV',     # Insane Voltage - 8192
    'LuV',    # Ludicrous Voltage - 32768
    'ZPM',    # ZPM Voltage - 131072
    'UV',     # Ultimate Voltage - 524288
    'UHV',    # Highly Ultimate Voltage - 2097152
    'UEV',    # Extremely Ultimate Voltage - 8388608
    'UIV',    # Insanely Ultimate Voltage - 33554432
    'UMV',    # Mega Ultimate Voltage - 134217728
    'UXV',    # Extended Mega Ultimate Voltage - 536870912
    'MAX'     # Maximum Voltage - 2147483647
}

AMP = {
    '4A' :'4A',
    '16A' :'16A',
    '64A' :'64A',
    '256A/t': '256A/t',
    '1,024A/t': '1.024A/t',
    '4,096A/t': '4.096A/t',
    '16,384A/t': '16.384A/t',
    '65,536A/t': '65.536A/t',
    '262,144A/t': '262.144A/t',
    '1,048,576A/t': '1.048.576A/t'
}

Machine = {
    'Laser Target Hatch' :'Lazer Hedef Kapağı',
    'Laser Source Hatch' :'Lazer Kaynak Kapağı',
    'Energy Hatch' :'Enerji Kapağı',
    'Dynamo Hatch' :'Dinamo Kapağı',
}

def main():
    with open('GregTech.lang', 'r', encoding="utf-8") as f:
        lines = f.read().splitlines()
    properties = []
    rest = []
    count = 0
    for line in lines:
        if line.startswith("}"):
            break
        split = line.split("=", 1)
        key = split[0]
        s_key = f"gt-lang|{key}"
        try:
            value = split[1]
        except:
            value = ":("
        fword = value.split(" Voltage", 1)
        
        for item in tier:
            if item in value:
                for amp in AMP:
                    if amp in value and "Voltage" not in value:
                        for machine in Machine:
                            if machine in value and value == item + " " +amp + " " + machine:
                                count = count + 1
                                properties.append({
                                    'key': s_key,
                                    'original': value,
                                    'translation': item + " " +AMP[amp] + " " + Machine[machine],
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
