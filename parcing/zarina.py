import re
import csv
import ssl
import urllib.request

#ssl._create_default_https_context = ssl._create_unverified_context

url = "https://msk.spravker.ru/avtoservisy-avtotehcentry/"
response = urllib.request.urlopen(url)
html_content = response.read().decode()

#with open('spravker_html.txt', 'w', encoding='utf-8') as file:
    #file.write(html_content)

#print(html_content)

nameorg = r'class="org-widget-header__title-link"[^>]*>([^<]+)' 
namee = re.findall(nameorg,html_content)

addresorg = r'org-widget-header__meta--location"[^>]*>\s*([^<]+?)\s*<'
addresss = re.findall(addresorg,html_content)

phoneorg = r'Телефон</span></dt>\s*<dd class="spec__value">([^<]+)</dd>'
phonee = re.findall(phoneorg,html_content)

workourorg = r'Часы работы</span></dt>\s*<dd class="spec__value">([^<]+)</dd>'
workourr = re.findall(workourorg,html_content)


with open('avto.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Название', 'Адрес', 'Телефон', 'Часы работы'])
    
    pup = min(len(namee), len(addresss), len(phonee), len(workourr))
    
    for i in range(pup):
        writer.writerow([
            namee[i],
            addresss[i],
            phonee[i],
            workourr[i]
        ])

min_len = min(len(namee), len(addresss), len(phonee), len(workourr))
for i in range( min_len):
    print(f"  Название: {namee[i]}")
    print(f"  Адрес: {addresss[i]}")
    print(f"  Телефон: {phonee[i]}")
    print(f"  Часы работы: {workourr[i]}")
    print("\n")
    
