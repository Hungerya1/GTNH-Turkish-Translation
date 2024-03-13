import requests
import os
import sys
import json

#put "GregTech.lang" and this script in the same file


auth_key = "api_key" #your api key
target_language = "TR" #languange code

def translate_text(text):
    url = "https://api-free.deepl.com/v2/translate"
    payload = {
        "text": text,
        "target_lang": target_language,
        "auth_key": auth_key
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        translation = response.json()["translations"][0]["text"]
        return translation
    else:
        print("Error:", response.status_code)

def main():
    with open('GregTech.lang', 'r', encoding="utf-8") as f:
        lines = f.read().splitlines()
    properties = []
    rest = []
    for line in lines:
 
        if line.startswith("}"):
            break

        split = line.split("=", 1)
        if len(split) != 2:
            found_material = False
            continue
        key = split[0].replace('"context": "',"")
        s_key = f"gt-lang|{key}"
        value = split[1].replace('"','')
        if key.startswith("      S:Material"):
            properties.append({
                'key': s_key,
                'original': value,
                'translation': translate_text(value),
                'stage': 5,
                'context': s_key.replace("gt-lang|","") + '=' + value,
            })
        else:
            rest.append(s_key + '=' + value)

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