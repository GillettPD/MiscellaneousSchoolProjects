import re

with open("C:\\Users\\pdoug\\Downloads\\kotiria_narrative.txt", "r", encoding="utf-8") as f:
    txt = f.read()
    separated = re.split(r'(\([0-9]+\))', txt)

final = []
for i, entry in enumerate(separated):
    if re.search('clf', entry):
        final.append(separated[i-1])
        final.append(entry)
        

with open("C:\\Users\\pdoug\\Downloads\\kotiria_narrative_scraped.txt", "w", encoding="utf-8") as ff:
    for entry in final:
        ff.write(entry)