# Execute the following in the Terminal

# pip install requests
# pip install bs4
# pip install lxml
# pip install selenium
# pip install urllib


from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, requests, re, sys
from selenium import webdriver


# Website url
IDBIurl = 'https://www.idbibank.in/credit-card.asp'


html = urlopen(IDBIurl)

# soup is the source code of the webpage
soup = BeautifulSoup(html, 'lxml')

# Titles of all cards
cards = []

for x in soup.select('td td td td strong'):
    cards.append(x.get_text())

# Image urls
img = []

for x in soup.select('td:nth-child(2) tr:nth-child(2) img')[:5]:
    img.append('https://idbibank.in/'+x.get('src'))

# Learn More urls
learn_more = []

l = []

# Apply Links
apply_now =[]

for x in soup.find_all('a'):
    if str(x.get('href')).split('-')[0] in ['Royal', 'Euphoria', 'aspire', 'Imperium', 'Winnings']:

        if str(x.get('href')).split('-')[-1] != 'card.asp?apply=true':
            l.append("https://idbibank.in/" +x.get('href'))

        if str(x.get('href')).split('-')[-1] == 'card.asp?apply=true':
            apply_now.append("https://idbibank.in/" +x.get('href'))

learn_more = l[3:8]


welcome_offer = []
rewards = []
specials = []

fees = []
details = []

# Fetching the above fields(fees, details, welcome offer, rewards, specials) from the learn_more urls
for u in range(len(learn_more)):
    html = urlopen(learn_more[u])
    soup_1 = BeautifulSoup(html,'lxml')
    l1 = []
    l2 = []
    l3 = []

    for x in soup_1.select('#FB td+ td strong'):
        l1.append(x.get_text())

    for x in soup_1.select('#FB td+ td'):
        l2.append(re.sub('\W+', ' ', x.get_text()))

    for x in range(len(l2)):
        l3.append(l2[x].replace(l1[x], l1[x] + ':'))

    details.append(l3)

    f = soup_1.find('table', class_='mystyle content')

    g = f.find_all('td')[2].get_text().strip().replace("  ", " ")
    h = f.find_all('td')[3].get_text().strip().replace("  ", " ")

    i = f.find_all('td')[4].get_text().strip().replace("  ", " ")
    j = f.find_all('td')[5].get_text().strip().replace("  ", " ")

    s = f'{g}:{h}  |  {i}:{j}'

    fees.append(s.replace('\u2013','').replace('\u00a0',''))

    l20 = []
    if u==0:

        for x in soup_1.select('#FB td+ td'):
            l20.append(re.sub('\W+', ' ', x.get_text()))

        w = l20[0][352:429]

        r = l20[0][134:170]

        s = l20[0][437:486]

        welcome_offer.append(w)
        rewards.append(r)
        specials.append(s)

    elif u==1:

        for x in soup_1.select('#FB td+ td'):
            l20.append(re.sub('\W+', ' ', x.get_text()))

        w = l20[0][221:320]

        r = l20[0][346:452]

        s = l20[0][465:618]

        welcome_offer.append(w)
        rewards.append(r)
        specials.append(s)

    elif u==2:

        for x in soup_1.select('#FB td+ td'):
            l20.append(re.sub('\W+',' ', x.get_text()))

        w = l20[0][349:409]

        r = l20[0][133:209]

        s = l20[0][413:490]

        welcome_offer.append(w)
        rewards.append(r)
        specials.append(s)

    elif u==3:

        for x in soup_1.select('#FB td+ td'):
            l20.append(re.sub('\W+', ' ', x.get_text()))

        w = l20[2][352:395]

        r = l20[2][92:170]

        s = l20[2][395:]

        welcome_offer.append(w)
        rewards.append(r)
        specials.append(s)

    else:

        for x in soup_1.select('#FB td+ td'):
            l20.append(re.sub('\W+', ' ', x.get_text()))

        w = l20[0][298:420]

        r = l20[0][420:515]

        s = l20[0][516:565]

        welcome_offer.append(w)
        rewards.append(r)
        specials.append(s)

"""
Using the below code, keys and values will be fetched, a dictionary will be created for each card and 
appended to the 'final' list one by one
"""

key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "summary4_title", "summary4_desc","details", "image_url", "learn_more_url", "apply_link"]
final = []
for i in range(0, 5, 1):
    x = {
        key[0]: (i * 0.1) + 8,
        key[1]: cards[i].strip()+" Credit Card",
        key[2]: "Welcome offer",
        key[3]: welcome_offer[i],
        key[4]: "Rewards",
        key[5]: rewards[i],
        key[6]: "Specials",
        key[7]: specials[i],
        key[8]: "Fees",
        key[9]: fees[i],
        key[10]: details[i],
        key[11]: img[i],
        key[12]: learn_more[i],
        key[13]: apply_now[i]

    }
    final.append(x)

man = {
    "cards_information": final

}

print(man)

# creating a json file
import json
y = json.dumps(man,indent=2)
with open("idbi.json", "w") as outfile:
    outfile.write(y)






