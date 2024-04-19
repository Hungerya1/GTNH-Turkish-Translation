from ast import Try
import json
from re import I

tier = {
    'Low': 'Düşük',
    'Medium': 'Orta',
    'High': 'Yüksek',
    'Extreme': 'Ekstrem',
    'Insane': 'Çılgın',
    'Ludicruous': 'Absürt',
    'ZPM': 'ZPM',
    'Ultimate': 'Üstün',
    'Highly Ultimate': 'Ziyadesiyle Üstün',
    'Extremely Ultimate': 'Aşırı Üstün',
    'Insanely Ultimate': 'Çılgınca Üstün',
    'Mega Ultimate': 'Mega Üstün',
    'Extended Mega Ultimate': 'Genişletilmiş Mega Üstün',
    'Maximum': 'Maksimum'
}

trvword = {
    'Transformer': 'Transformatör',
    'Coil': 'Bobin',
    'Power Transformer': 'Güç Transformatörü',
    'Coil': 'Bobin',
    'Solar Panel (Needs cleaning with right click)': 'Güneş Paneli (Sağ tık ile temizlenmesi gerekir)',
    'Battery': 'Pil',
    'Tesla Transceiver': 'Tesla Alıcısı-Vericisi',
    'Buck Converter': 'Sıçrayan Dönüştürücü',
    'Locker': 'Dolap',
    'Energy Buffer': 'Enerji Tamponu',
    'Turbo Charger': 'Turbo Şarj Cihazı',
    'Battery Charger': 'Pil Şarj Cihazı',
    'Battery Buffer': 'Pil Tamponu',
    'Type Filter': 'Tip Filtresi',
    'Super Buffer': 'Süper Tampon',
    'Regulator': 'Regülatör',
    'Recipe Filter': 'Tarif Filtresi',
    'Item Distributor': 'Eşya Dağıtıcı',
    'Item Filter': 'Eşya Filtresi',
    'Chest Buffer': 'Sandık Tamponu',
    'Hi-Amp Transformer': 'Y-Amp Transformatör'
}

def is_1d(item):
    return not isinstance(item, list) or len(item) == 0

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
        fword = value.split(" Voltage", 1)

        if fword[0] in tier and len(fword) > 1:
            break
            if fword[1].replace(" ","",1) in trvword:
                count = count + 1
                kelime = "  "
                if "Voltage" in value:
                    kelime = " Gerilim "
                properties.append({
                    'key': s_key,
                    'original': value,
                    'translation': tier.get(fword[0], '') + kelime + trvword.get(fword[1].replace(" ","",1), ''),
                    'stage': 5,
                    'context': s_key + '=' + value,
                })
                found_material = True
            else:
                rest.append(s_key + '=' + value)
        else:
            rest.append(s_key + '=' + value)
        
        for item in tier:
            break
            if item in value:
                for machine in trvword:
                    if machine in value and "Voltage" not in value:
                        count = count + 1
                        properties.append({
                            'key': s_key,
                            'original': value,
                            'translation': item + " " +machine,
                            'stage': 5,
                            'context': s_key + '=' + value,
                        })
        if key == "    S:gt.blockores.16071.tooltip":
            print(value)
        if "tooltip" in key and len(value.split(" ")) == 1:
            count = count + 1
            properties.append({
                'key': s_key,
                'original': value,
                'translation': value,
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
