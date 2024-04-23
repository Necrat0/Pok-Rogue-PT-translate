import json

def create_translation_map(file_en, file_es):
    translation_map = {}
    with open(file_en, 'r', encoding='utf8') as f_en, open(file_es, 'r', encoding='utf8') as f_es:
        for line_en, line_es in zip(f_en, f_es):
            translation_map[line_en.strip().replace('’', "'").replace('\\n', ' ')] = line_es.strip().replace('\\n', ' ').replace('  ', ' ')
    return translation_map

name9_en = "move9_name_en.txt"
name9_es = "move9_name_es.txt"
desc9_en = "move9_desc_en.txt"
desc9_es = "move9_desc_es.txt"
desc8_en = "move8_desc_en.txt"
desc8_es = "move8_desc_es.txt"
gwazaname_en = "gwazaname_en.txt"
gwazaname_es = "gwazaname_es.txt"
gwazainfo_en = "gwazainfo_en.txt"
gwazainfo_es = "gwazainfo_es.txt"
desc7_en = "move7_desc_en.txt"
desc7_es = "move7_desc_es.txt"

name9_map = create_translation_map(name9_en, name9_es)
desc9_map = create_translation_map(desc9_en, desc9_es)
# ----------------- #
desc8_map = create_translation_map(desc8_en, desc8_es)

with open(gwazaname_en, 'r', encoding='utf8') as file_en, open(gwazaname_es, 'r', encoding='utf8') as file_es:
    for line_en, line_es in zip(file_en, file_es):
        name9_map[line_en.strip().replace('’', "'").replace('\\n', ' ')] = line_es.strip().replace('\\n', ' ').replace('  ', ' ')

with open(gwazainfo_en, 'r', encoding='utf8') as file_en, open(gwazainfo_es, 'r', encoding='utf8') as file_es:
    for line_en, line_es in zip(file_en, file_es):
        desc8_map[line_en.strip().replace('’', "'").replace('\\n', ' ')] = line_es.strip().replace('\\n', ' ').replace('  ', ' ')
# ----------------- #
desc7_map = create_translation_map(desc7_en, desc7_es)
# ----------------- #

inputFile = "moves_en.json"
outputFile = "moves_es.json"
# Load the JSON data
with open(inputFile, 'r', encoding='utf8') as file:
    json_data = json.load(file)

# Translate the JSON data with Gen 9 data
for key in json_data:
    json_data[key]['name'] = name9_map.get(json_data[key]['name'], json_data[key]['name'])
    json_data[key]['effect'] = desc9_map.get(json_data[key]['effect'], json_data[key]['effect'])

# Translate the remaining data with Gen 8 data
for key in json_data:
    json_data[key]['effect'] = desc8_map.get(json_data[key]['effect'], json_data[key]['effect'])

# Translate the remaining data with Gen 7 data
for key in json_data:
    json_data[key]['effect'] = desc7_map.get(json_data[key]['effect'], json_data[key]['effect'])

# Write the translated JSON data to a file
with open(outputFile, 'w', encoding='utf8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=2)