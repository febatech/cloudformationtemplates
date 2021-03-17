from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, requests

hdfc_url = ['https://www.hdfcbank.com/personal/pay/cards/credit-cards']
identity = ["bp-area c-template-hdfc-2-7-3--area col-xs-12 col-sm-8 col-md-7 col-lg-7 large-side-scroll-fix clearfix"]

# execute pip install lxml in the terminal
html = requests.get(hdfc_url[0])
soup = BeautifulSoup(html.content, 'lxml')
address = soup.find('div', attrs={"class": identity[0]})

cards = []  # list of all CARDS
desc = []

for lis in address.find_all('span', attrs={"class": "card-name"}):
    # print(lis.get_text())
    cards.append(lis.get_text())

for lis in address.find_all('li'):
    if lis.get_text() != '':
        desc.append(lis.get_text())

print(desc)

knowMore = []
km = soup.find_all('a', string='KNOW MORE')
counter = 1
for i in km:
    if counter % 2 == 0:
        knowMore.append(f"https://www.hdfcbank.com{i['href']}"+"/fees-and-charges")
    else:
        pass
    counter += 1
print(knowMore)

applyOnline = []
a0 = soup.find_all('div', {'class': 'cardparent'})
for x in a0:
    a1 = x.find_all('div', {'class': 'btnParent'})
    for y in a1:
        z = y.find_all('a', string='APPLY ONLINE')
        if (len(z) > 0):
            counter = 1
            for q in z:

                if counter % 2 == 0:
                    applyOnline.append(q['href'])
                else:
                    pass
                counter += 1

        else:
              applyOnline.append('  ')
#
print(applyOnline)

keypoints = []
nullData = ["Get 1% surcharge waiver and save upto Rs. 250 in every billing cycle  (Min transaction of Rs. 400)",
            "Fuel surcharge waived off on fuel transactions of Rs. 400 to Rs. 5000, maximum waiver of Rs.250 per statement cycle.",
            "Welcome Benefit: 1000 Reward Points, Renewal Benefit: 1000 reward points",
            "Spend Rs. 1,50,000 on your JetPrivilege HDFC Bank Select / Titanium Credit Card within 12 months of the Card setup date or within 12 months of Card renewal date and get the renewal fee for the next year waived off*"]
nullCounter = 0
point = soup.find_all('div', {'class': 'offer-dtl mB10'})
for x in point:
    pointList = x.find_all("li")
    if (len(pointList) >= 3):
        for y in pointList[:3]:
            keypoints.append(y.text)
    else:
        for y in pointList[:2]:
            keypoints.append(y.text)

        keypoints.append(nullData[nullCounter])
        nullCounter += 1

rewards = []
offers = []
voucher = []
for x in range(0, len(keypoints)):
    if ((x + 1) % 3 == 1):
        rewards.append(keypoints[x].replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0',''))
    elif ((x + 1) % 3 == 2):
        offers.append(keypoints[x].replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0',''))
    else:
        voucher.append(keypoints[x].replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0',''))

img = []

for x in address.find_all('img', attrs={"class": "img-responsive lazy"}):
    img.append("https://www.hdfcbank.com"+x.get("src"))
    # print(x)
print(img)

fee = []

for link in range(len(knowMore)):
    html_1 = requests.get(knowMore[link])
    soup_1 = BeautifulSoup(html_1.content, 'lxml')

    #
    if link in [1,2,3,4,5,9,10,16,17,18,19,20,21,22]:
        for lis in soup_1.select(".right-section li:nth-child(1)"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))

    if link in [0, 11, 12, 13, 14, 15, 25, 28, 29, 33, 34]:
        for lis in soup_1.select(".right-section p:nth-child(1)"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))

    if link in [7,8,23,27,30,31,38,41,42]:
        for lis in soup_1.select(".content-body:nth-child(1) p:nth-child(1)"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))

    if link in [37,39]:
        for lis in soup_1.select(".content-body+ .content-body p:nth-child(1)"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))

    if link in [35,36,26]:
        for lis in soup_1.select(".content-body:nth-child(1) p"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))

    if link in [6,32]:
        for lis in soup_1.select("ul+ p"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))

    if link in [40]:
        for lis in soup_1.select(".content-body:nth-child(1) .right-section > p"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))

    if link in [24]:
        for lis in soup_1.select(".right-section ul:nth-child(1) li:nth-child(1)"):
            print(lis.get_text())
            fee.append(lis.get_text().replace('\n',"").replace('\u2013','').replace('\u20b9','').replace('\u00a0','').replace('\u2019',''))






print(fee)
#




key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc","summary4_title","summary4_desc","details", "image_url", "learn_more_url","apply_link"]

final = []
for i in range(0, 43, 1):
    x = {
        key[0]: format(((i * 0.01) + 7), '.2f'),
        key[1]: cards[i],
        key[2]: "Rewards",
        key[3]: rewards[i],
        key[4]: "offers",
        key[5]: offers[i],
        key[6]: "voucher",
        key[7]: voucher[i],
        key[8]: "Fees",
        key[9]: fee[i],
        key[10]: [
            "Rewards : " + rewards[i],
            "Waivers : " + offers[i],
            "Offers : " + voucher[i]
        ],
        key[11]: img[i],
        key[12]: knowMore[i],
        key[13]: applyOnline[i]

    }
    final.append(x)

man = {
    "cards_information": final

}

print(man)

import json
y = json.dumps(man,indent=2)
with open("hdfc.json", "w") as outfile:
    outfile.write(y)