# # -*- coding: utf-8 -*-
# """WorkBoB.ipynb
#
# Automatically generated by Colaboratory.
#
# Original file is located at
#     https://colab.research.google.com/drive/1GbwTfSf94p73rH-bPZP4JWRmW7XPyeW0
# """

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

url = ["https://www.bobfinancial.com/easy-card.jsp", "https://www.bobfinancial.com/select-card.jsp",
       "https://www.bobfinancial.com/premier-card.jsp", 'https://www.bobfinancial.com/prime.jsp']
class_files = ["tabcardpoints"]
card_names = ["Bank of Baroda Easy", "Bank of Baroda Select", "Bank of Baroda Premier", "Bank of Baroda Prime"]

Rewards = []
SplRewards = []
cashback = []
Fees = []
for i in range(0, 3, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="tabcardpoints")
    for lis in address.find_all('li')[:1]:
        Rewards.append(lis.get_text().replace("\n\u00a0", ""))

    for lis in address.find_all('li')[1:2]:
        SplRewards.append(lis.get_text().replace("\n\u00a0", ""))

    for lis in address.find_all('li')[2:3]:
        cashback.append(lis.get_text().replace("\n\u00a0", ""))

    for lis in address.find_all('li')[4:]:
        Fees.append(lis.get_text().replace("\n\u00a0", ""))

Life_time = []
Fuel_Surcharge_Waiver = []
redemption = []
emi = []
for i in range(0, 3, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="fullwidth cclandsec1")
    for lis in address.find_all('p')[2:3]:
        # print(lis.get_text())
        Life_time.append(lis.get_text().replace("\u00a0", ""))

    for lis in address.find_all('p')[3:4]:
        # print(lis.get_text())
        Fuel_Surcharge_Waiver.append(lis.get_text().replace("\u00a0", ""))

    for lis in address.find_all('p')[5:6]:
        # print(lis.get_text())
        redemption.append(lis.get_text().replace("\u00a0", ""))

    for lis in address.find_all('p')[6:]:
        # print(lis.get_text())
        emi.append(lis.get_text().replace("\u00a0", ""))

add_on1 = []
add_on2 = []
add_on3 = []
add_on4 = []
add_on5 = []
html_1 = urlopen(url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div', class_="fullwidth esycclandsec2")
for lis in address.find_all('p')[:1]:
    # print(lis.get_text())
    add_on1.append(lis.get_text().replace("\u00a0", ""))

for lis in address.find_all('p')[1:2]:
    # print(lis.get_text())
    add_on2.append(lis.get_text().replace("\u00a0", ""))

for lis in address.find_all('p')[2:3]:
    # print(lis.get_text())
    add_on3.append(lis.get_text().replace("\u00a0", ""))

for lis in address.find_all('p')[3:4]:
    # print(lis.get_text())
    add_on4.append(lis.get_text().replace("\u00a0", ""))

for lis in address.find_all('p')[4:]:
    # print(lis.get_text())
    add_on5.append(lis.get_text().replace("\u00a0", ""))

img_url = []
for i in range(0, 3, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="tabcardimg")
    for lis in address.find_all('img'):
        # print(lis.get('src'))
        img_url.append("https://www.bobfinancial.com/" + lis.get('src'))

apply_url = []
for i in range(0, 3, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="fullwidth prmrcrdsec3 text-center")
    for lis in address.find_all('a'):
        # print(lis.get('href'))
        apply_url.append(lis.get('href'))

eligibility = ["Minimun Annual Income - ₹3,60,000", "Minimun Annual Income - ₹4,80,000",
               "Minimun Annual Income - ₹7,20,000"]

key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "summary4_title", "summary4_desc", "image_url", "apply_link", "learn_more", "eligibility"]
final = []
for i in range(0, 3, 1):
    x = {
        key[0]: (i * 0.1) + 5,
        key[1]: card_names[i],
        key[2]: "Special_Rewards",
        key[3]: Rewards[i],
        key[4]: "Rewards",
        key[5]: SplRewards[i],
        key[6]: "Cashbacks/Complimentary",
        key[7]: cashback[i],
        key[8]: "Fees",
        key[9]: Fees[i],
        "details": [
            "Life_time: " + Life_time[i],
            "Fuel Surcharge Waiver*: " + Fuel_Surcharge_Waiver[i],
            "Multiple redemption options: " + redemption[i],
            "Easy EMI option: " + emi[i],
            "Free Add-on card: " + add_on1[0],
            "In-built insurance cover: " + add_on2[0],
            "Zero liability on lost card: " + add_on3[0],
            "Interest free credit facility: " + add_on4[0],
            "Revolving credit facility: " + add_on5[0]
        ],
        key[10]: img_url[i],
        key[11]: apply_url[i],
        key[12]: url[i],
        key[13]: eligibility[i].replace("\u20b9", "")

    }
    final.append(x)

###############################prime##########################################
Rewards1 = []
cashback1 = []
Fees1 = []
html_1 = urlopen(url[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div', class_="tabcardpoints")
for lis in address.find_all('li')[:1]:
    #  print(lis.get_text())
    Rewards1.append(lis.get_text().replace("\n\u00a0", ""))

for lis in address.find_all('li')[1:2]:
    #  print(lis.get_text())
    cashback1.append(lis.get_text().replace("\n\u00a0", ""))

for lis in address.find_all('li')[3:]:
    # print(lis.get_text())
    Fees1.append(lis.get_text().replace("\n\u00a0", ""))

Fuel_Surcharge_Waiver1 = []
redemption1 = []
emi1 = []
html_1 = urlopen(url[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div', class_="fullwidth cclandsec1")

for lis in address.find_all('p')[3:4]:
    #  print(lis.get_text())
    Fuel_Surcharge_Waiver1.append(lis.get_text().replace("\u00a0", ""))

for lis in address.find_all('p')[5:6]:
    # print(lis.get_text())
    redemption1.append(lis.get_text().replace("\u00a0", ""))

for lis in address.find_all('p')[6:]:
    # print(lis.get_text())
    emi1.append(lis.get_text().replace("\u00a0", ""))

image1 = []
apply1 = ["creditcard-application-form.jsp"]
imageadd = soup_1.find('div', class_="tabcardimg")
for lis in imageadd.find_all('img'):
    # print(lis.get('src'))
    image1.append("https://www.bobfinancial.com/" + lis.get('src'))

key = ["key", "name", "summary1_title", "summary1_desc", "summary3_title", "summary3_desc", "summary4_title",
       "summary4_desc", "image_url", "apply_link", "learn_more"]
x1 = {
    key[0]: 5.3,
    key[1]: card_names[3],
    key[2]: "Special_Rewards",
    key[3]: Rewards1[0],
    key[4]: "Cashbacks/Complimentary",
    key[5]: cashback1[0],
    key[6]: "Fees",
    key[7]: Fees1[0],
    "details": [
        "Fuel Surcharge Waiver*: " + Fuel_Surcharge_Waiver1[0],
        "Multiple redemption options: " + redemption1[0],
        "Easy EMI option: " + emi1[0],
        "Free Add-on card: " + add_on1[0],
        "In-built insurance cover: " + add_on2[0],
        "Zero liability on lost card: " + add_on3[0],
        "Interest free credit facility: " + add_on4[0],
        "Revolving credit facility: " + add_on5[0]
    ],
    key[8]: image1[0],
    key[9]: apply1[0],
    key[10]: url[3]
}
final.append(x1)

url = ["https://www.bobfinancial.com/eterna.jsp", "https://www.bobfinancial.com/icai-exclusive.jsp",
       "https://www.bobfinancial.com/icsi-diamond.jsp", 'https://www.bobfinancial.com/cma-one.jsp']
class_files = ["tabcardpoints"]
card_names = ["Bank of Baroda ETERNA", "Bank of Baroda ICAI Exclusive", "Bank of Baroda ICSI DIAMOND",
              "Bank of Baroda CMA ONE"]

welcome_offer = []
rewards = []
fees = []
for i in range(0, 4, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', id="eterna-sec3")
    for lis in address.find_all('p')[2:3]:
        # print(lis.get_text())
        welcome_offer.append(lis.get_text())

    for lis in address.find_all('p')[6:7]:
        # print(lis.get_text())
        rewards.append(lis.get_text())

    man = soup_1.find('table')
    for row in man.findAll("td")[4:5]:
        # print(row.get_text())
        fees.append(row.get_text())

emi = []
addon = []
lost = []
html_1 = urlopen(url[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div', id="eterna-sec3")
for lis in address.find_all('p')[8:9]:
    # print(lis.get_text())
    emi.append(lis.get_text())

for lis in address.find_all('p')[10:11]:
    # print(lis.get_text())
    addon.append(lis.get_text())

for lis in address.find_all('p')[14:15]:
    # print(lis.get_text())
    lost.append(lis.get_text())

comple = []
html_1 = urlopen(url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
build = soup_1.find('div', id="eterna-sec3")
for lis in build.find_all('p')[14:15]:
    # print(lis.get_text())
    comple.append(lis.get_text())

for i in range(1, 4, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    build = soup_1.find('div', id="eterna-sec3")

    for lis in build.find_all('p')[12:13]:
        # print(lis.get_text())
        comple.append(lis.get_text())

img = []
apply = []
for i in range(0, 4, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    imgg = soup_1.find('div', id="eterna-sec3")

    for lis in imgg.find_all('img'):
        # print(lis.get('src'))
        img.append("https://www.bobfinancial.com/" + lis.get('src'))

    app = soup_1.find('div', class_="fullwidth eterna-sec4")
    for lis in app.find_all('a'):
        # print(lis.get('href'))
        apply.append(lis.get('href'))

elig = []
for i in range(0, 4, 1):
    html_1 = urlopen(url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="flip-card-back")
    for lis in address.find_all('p')[3:4]:
        # print(lis.get_text())
        elig.append(lis.get_text())

key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "image_url", "apply_link", "learn_more", "eligibility"]

for i in range(0, 4, 1):
    x2 = {
        key[0]: round(5.3 + (0.1 * (i + 1)), 2),
        key[1]: card_names[i],
        key[2]: "Welcome_offer",
        key[3]: welcome_offer[i],
        key[4]: "Rewards",
        key[5]: rewards[i].replace("\u20b9", ""),
        key[6]: "Fees",
        key[7]: fees[i],
        "details": [
            "Easy EMI option: " + emi[0],
            "Free Add-on card: " + addon[0],
            "Zero liability on lost card: " + lost[0],
            "In-built insurance cover: " + comple[i].replace("\u20b9", "")
        ],
        key[8]: img[i],
        key[9]: apply[i],
        key[10]: url[i],
        key[11]: elig[i].replace("\u20b9", "")

    }
    final.append(x2)


man = {
    "cards_information": final

}

print(man)


import json

y = json.dumps(man,indent=2)
with open("bob.json", "w") as outfile:
    outfile.write(y)




