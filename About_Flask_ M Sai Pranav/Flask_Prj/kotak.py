from urllib.request import urlopen
from bs4 import BeautifulSoup
import json


kotak_url=['https://www.kotak.com/en/personal-banking/cards/credit-cards.html']
identity=["cmp-item-list card-list m-grid dynamic-card-values list"]

# execute pip install lxml in the terminal
html = urlopen(kotak_url[0])
soup = BeautifulSoup(html, 'lxml')
address = soup.find('div',attrs={"class" : identity[0]})

cards = []                                              # list of all CARDS
desc= []                                                # list of all bullet lines


for lis in address.find_all('h4',attrs={"class" : "em-title share-comp-title"}):
    print(lis.get_text())
    cards.append(lis.get_text())


for lis in address.find_all('li'):
    if lis.get_text() != '':
        desc.append(lis.get_text().replace("\n", ""))


know_more=[]                                            # list of all know_more links unfiltered


for lis in address.find_all("div", attrs={"class" : "link-box"}):
    know_more.append(lis.find('a').get("href"))

know_more_new=[]                                        #  list of all know_more links filtered

for lis in know_more:
    s1=lis.split("/")
    for x in range(3):
        s1.pop(0)
    s1.insert(0, "www.kotak.com")
    s1.insert(0, "https:/")
    s2 = "/".join(s1)
    know_more_new.append(s2)

apply_now = []
w = address.find_all("div",class_="item-links")
for x in range(len(w)):
    if x in [6,7,13]:
        apply_now.append(" ")
    elif w[x].find("a").get("href")[0]=="/":
        a="https://www.kotak.com"+w[x].find("a").get("href")
        apply_now.append(a)
    else:
        apply_now.append(w[x].find("a").get("href"))

d = {"rewards" : [], "joining_gift" : [], "waiver" : [], "offers" : []}

for link in know_more_new:
    html_1 = urlopen(link)
    soup_1 = BeautifulSoup(html_1, 'lxml')
    f = soup_1.find('div', class_="saving-ac custom-bg-color")
    l = f.find_all("figcaption", class_="figure-caption")
    four_points= []
    for x in range(4):
        l_1 = l[x].find_all(['p','div'])
        for y in l_1:
            if y.get_text() != "" and y.get_text().isspace() != True:
                four_points.append(y.get_text().replace("\n", "").replace("\xa0", "").replace("\u2013","").replace("\u20b9",""))
    for x in range(len(four_points)):
        d[list(d)[x]].append(four_points[x])


img = []
imgd = []
imgm = []

for x in address.find_all('img'):
    img.append(x.get("data-src"))
img = list(filter(None, img))
# del img[1::2]
img = ["https://kotak.com" + s for s in img]
print(img)
for x in range(len(img)):
    if x%2==0:
        imgd.append(img[x])

    else:
        imgm.append(img[x])


fees = []
for x in address.find_all('span' ,class_ = 'custom-span'):
    print(x.get_text())
    fees.append(x.get_text().replace('\n',"").replace('\xa0',''))

f1=address.find_all('div', class_ = 'item-points em-desc share-comp-desc')[-1]
fees.append(f1.find('p').get_text().replace('\n',"").replace('\xa0',''))

fees_cut=fees[3:len(fees)-1]
fees_cut_new = []
for x in range(0,len(fees_cut),2):
    fees_cut_new.append(fees_cut[x] + "|" + fees_cut[x+1])

fees_final = fees[0:3] + fees_cut_new + fees[-1:-2:-1]           # final fees list

ignore = ["Privy League Signature Credit Card","Wealth Management Infinite Credit Card","Feast Gold Credit Card",
          "Fortune Gold Credit Card"]


key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "summary4_title", "summary4_desc","summary5_title", "summary5_desc","details", "image_url",
       "image_url_2", "learn_more_url","apply_link"]

final = []
for i in range(0, 20, 1):
    x = {
        key[0]: format(((i * 0.01) + 2), '.2f'),
        key[1]: cards[i],
        key[2]: "Rewards",
        key[3]: d['rewards'][i],
        key[4]: "Joining_Gift",
        key[5]: d['joining_gift'][i],
        key[6]: "Waivers",
        key[7]: d['waiver'][i],
        key[8]: "Offers",
        key[9]: d['offers'][i],
        key[10]: "Fees",
        key[11]: fees_final[i],
        key[12]: [
            "Rewards : " + d['rewards'][i],
            "Waivers : " + d['waiver'][i],
            "Offers : " + d['offers'][i]
        ],
        key[13]: imgd[i],
        key[14]: imgm[i],
        key[15]: know_more_new[i],
        key[16]: apply_now[i]

    }
    final.append(x)

man = {
    "cards_information": final

}

print(man)

import json
y = json.dumps(man,indent=2)
with open("kotak.json", "w") as outfile:
    outfile.write(y)