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
import re, time

# Website url
IndusInd_url = "https://www.indusind.com/in/en/personal/cards/credit-card.html"

# Install the chrome driver from https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/
# executable path must be the path of chromedriver.exe file

driver = webdriver.Chrome(executable_path="C:\\Users\\lenovo\\Downloads\\chromedriver.exe")
driver.get(IndusInd_url)
time.sleep(3)

# the source code of the webpage is referred by the soup
soup = BeautifulSoup(driver.page_source, 'lxml')

# Titles of cards
cards = []

for x in soup.select("#display-product-cards .text-primary"):
    cards.append(x.get_text())

# image urls
img = []
for x in soup.find_all('img', class_ = 'rounded-1 w-100'):
    img.append("https://www.indusind.com" + x.get('src'))


start = len(img) - len(set(img))
img = img[start:]

# Know More urls
know_more = []

# Apply Now urls
apply_now = []

for x in soup.find_all('div', class_ = "d-flex justify-content-between align-items-center")[start:]:
    know_more.append("https://www.indusind.com"+x.find('a').get('href'))

for x in range(len(cards)):
    if x == 20:
        for y in soup.select(".btn-primary-option"):
            apply_now.append("https://www.indusind.com"+y.get('href'))
    else:
        apply_now.append("Please call 1860 267 7777 to apply for this Credit Card")

# List of eligibilities of all cards
eligibility = []

for x in range(len(know_more)):
    if x in [0,5,12,13,18,21]:
        driver.get(know_more[x])
        soup_1 = BeautifulSoup(driver.page_source, 'lxml')
        for x in soup_1.select('.border-right .card-body'):
            a = x.get_text().split('\n')
            eligibility.append(f"{a[-4]} | {a[-3]}".replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))
    else:
        eligibility.append("")

# List of description of all cards from where the rewards, welcome_offer, specials will be fetched
desc = []

# List of rewards, welcome offer, specials of all cards
Rewards = []
Welcome_Offer = []
Specials = []

c=0
for x in soup.find_all('ul', class_ = 'list-arrow-bullet pl-0 ml-0')[3:]:
    if c==0:
        for y in x.find_all('li')[:4]:
            if y.get_text() != "" :
                desc.append(y.get_text())
        c+=1
    else:
        for y in x.find_all('li')[:3]:
            desc.append(y.get_text())


for x in range(0,len(desc),3):
    Rewards.append(desc[x].replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))

for x in range(1,len(desc),3):
    Welcome_Offer.append(desc[x].replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))

for x in range(2,len(desc),3):
    Specials.append(desc[x].replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))



# List of fees of all cards
fees = []

for x in range(len(know_more)):
    if x in [0,2,18,21]:
        fees.append("")
    elif x in [1]:
        url = "https://www.indusind.com/in/en/microsites/crest/schedule-of-charges.html"
        driver.get(url)
        soup_2 = BeautifulSoup(driver.page_source, 'lxml')
        a = soup_2.select('td+ td , td+ td')[0].get_text()
        b = soup_2.select('td+ td , td+ td')[1].get_text()
        c = soup_2.select('td+ td , td+ td')[3].get_text().split('\n')[0]
        d = soup_2.select('td+ td , td+ td')[4].get_text().split('\n')[0]
        fees.append(f"{a} : {c}  |  {b} : {d}".replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))

    elif x in [3,4]:
        if x in [3]:
            fees.append("https://www.indusind.com/content/dam/indusind-corporate/offer-tnc/Heritage-MITC.pdf")
        else:
            fees.append("https://www.indusind.com/content/dam/indusind-corporate/offer-tnc/Legacy-MITC.pdf")

    elif x in [20]:
        url = "https://www.indusind.com/in/en/personal/cards/credit-card/duo-card.html"
        driver.get(url)
        soup_3 = BeautifulSoup(driver.page_source, 'lxml')
        for x in soup_3.select("#duo-plus .mt-3+ p"):
            a = x.get_text().split('\n')[0].replace('\xa0','')
            b = x.get_text().split('\n')[1].replace('\xa0','')
            fees.append(f"{a.replace('-',':')}  |  {b.replace('-',':')}".replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))

    else:
        fees.append("https://www.indusind.com/content/dam/indusind-corporate/schedule-of-charges/credit-cards/premium-MITC-2-07-2018.pdf")

# List of details of all cards
details = []

# List of links from where details will be fetched
det = ["https://indulge.indusind.com/content/Indulge/about-indulge.html","https://www.indusind.com/in/en/microsites/crest/crest-assistance.html","https://www.indusind.com/in/en/microsites/celesta/celesta-rewards.html", 'https://www.indusind.com/in/en/personal/cards/credit-card/pioneer-heritage-credit-card.html','https://www.indusind.com/in/en/personal/cards/credit-card/pioneer-legacy-credit-card.html#','https://www.indusind.com/in/en/personal/cards/credit-card/pinnacle-world-credit-card.html','https://www.indusind.com/in/en/personal/visa-lounge-access-program-list.html','https://www.indusind.com/in/en/microsites/nexxt.html','https://www.indusind.com/in/en/personal/cards/credit-card/platinum-master-credit-card.html','https://www.indusind.com/in/en/personal/cards/credit-card/platinum-select-credit-card.html','https://www.indusind.com/in/en/personal/cards/indusInd-bank-gift-card.html','https://www.indusind.com/in/en/personal/cards/credit-card/payback-credit-card.html#','https://www.indusind.com/in/en/personal/cards/credit-card/iconia-amex-credit-card.html#','https://www.indusind.com/in/en/personal/offers.html','https://www.indusind.com/in/en/personal/cards/credit-card/intermiles-odyssey-amex-credit-card.html#','https://www.intermiles.com/flights','https://www.indusind.com/in/en/personal/cards/credit-card/intermiles-voyage-amex-credit-card.html','https://www.indusind.com/in/en/personal/Terms-and-Conditions-Indusind-bank-golf-program.html','https://www.indusind.com/in/en/personal/cards/credit-card/signature-visa-credit-card.html#','https://www.indusind.com/in/en/personal/cards/credit-card/platinum-aura-visa-and-mastercard-credit-card.html#','https://www.indusind.com/in/en/personal/cards/credit-card/duo-card.html#','https://www.indusind.com/in/en/personal/cards/credit-card/iconia-credit-card.html#']

for i in range(len(det)):
    url = det[i]
    driver.get(url)
    time.sleep(3)

    soup_4 = BeautifulSoup(driver.page_source, 'lxml')
    if i == 0:
        d = []
        for x in soup_4.find_all('p', class_ = "goldentext"):
            a = f"{x.get_text()} : {x.find_next('p').get_text()}"

            # Replacing unnecessary stuff with a blank string

            d.append(a.replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))
        details.append(d)
    elif i == 1:
        d = []
        for x in soup_4.find_all('div', class_ = "services-content-wrap"):
            r = '\n'
            a = f"{x.get_text().replace(r, '')} : {x.find_next('div').get_text().replace(r, '')}"
            d.append(a.replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))
        details.append(d)
    # elif i == 2:
    #     d = []
    #     for x in soup_4.find_all('div', class_ = "content-inside-pages wow fadeInRight"):
    #         r='\n'
    #         a = f"{x.find('h3').get_text().replace(r,'')} : {x.find('p').get_text().replace(r,'')}{'' if x.find('ul') == None else x.find('ul').get_text().replace(r,'')}"
    #         d.append(a.replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013',''))
    #     details.append(d)
    elif i == 2:
        d = []
        d0 = []
        d1 = []
        for x in soup.select('.sub-heading'):
            d0.append(x.get_text())
        d2 = []
        for x in range(len(soup.select('li , .sub-heading+ p')[13:-4])):
            if x >= 2:
                d2.append(soup.select('li , .sub-heading+ p')[13:-4][x].get_text())
            else:
                d1.append(soup.select('li , .sub-heading+ p')[13:-4][x].get_text())

        d1.append(', '.join(d2))

        for x in range(len(d0)):
            d.append(f"{d0[x]}: {d1[x]}")
        details.append(d)
    elif i == 3:
        d = []
        for x in soup_4.select("p:nth-child(9) , p:nth-child(8) , #abc6 p:nth-child(7) , #abc6 p:nth-child(6) , #abc6 p:nth-child(5) , #abc6 p:nth-child(4)")[3:-9]:
            d.append(x.get_text().replace('-\n',' ').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)
    elif i == 4:
        d = []
        for x in soup_4.select('p:nth-child(14) , p:nth-child(12) , p:nth-child(10) , p:nth-child(8) , p:nth-child(6) , p:nth-child(16) , #benefits6 p:nth-child(4) , #benefits6 b')[20:-4:2]:
            r='\n'
            a = f"{x.get_text()}: {x.find_next().get_text().replace(r,'')}"
            d.append(a.replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)
    elif i == 5:
        d = []
        d1 = []
        for x in soup_4.select('h6+ p , #benefits2 h6')[3:5]:
            d1.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d.append((': ').join(d1).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in soup_4.select('#benefits2 li'):
            d.append(x.get_text().replace('\n', '').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)
    elif i == 6:
        d = []
        a = '\n'
        m = soup_4.select('p+ ul li , p b')[0:4]
        n = soup_4.select('p+ ul li , p b')[4:]
        d0 = []
        d1 = []
        d2 = []
        d3 = []
        for x in range(len(m)):
            if x == 0:
                d0.append(m[x].get_text())
            else:
                d1.append(m[x].get_text())
        d0.append(', '.join(d1).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d.append(': '.join(d0).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(n)):
            if x == 0:
                d2.append(n[x].get_text())
            else:
                d3.append(n[x].get_text())
        d2.append(', '.join(d3).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d.append(': '.join(d2).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)
    elif i == 7:
        d = []
        d0 = []
        for x in soup_4.select('.test h1'):
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d1 = []
        d2 = []
        for x in range(len(soup_4.select('#section04 p'))):
            if x == 0 or 1 or 2 or 3:
                d1.append(soup_4.select('#section04 p')[x].get_text())
            elif x == 4:
                d1.append(soup_4.select('#section04 p')[x].get_text())
            elif x == 5 or 6 or 7 or 8 or 9:
                d1.append(soup_4.select('#section04 p')[x].get_text())
            elif x == 10 or 11:
                d1.append(soup_4.select('#section04 p')[x].get_text())
            elif x == 12:
                d1.append(soup_4.select('#section04 p')[x].get_text())
            elif x == 13 or 14 or 15 or 16 or 17 or 18 or 19:
                d1.append(soup_4.select('#section04 p')[x].get_text())
            else:
                d1.append(soup_4.select('#section04 p')[x].get_text())

        d2.append(', '.join(d1[0:4]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d2.append(d1[4].replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d2.append(', '.join(d1[5:10]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d2.append(', '.join(d1[10:12]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d2.append(d1[12].replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d2.append(', '.join(d1[13:20]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d2.append(', '.join(d1[20:]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(f"{d0[x]} : {d2[x]}")
        details.append(d)
    elif i == 8:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select('#benefits8 b'):
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d2 = []
        for x in soup_4.select(
                '#benefits8 p:nth-child(11) , #benefits8 p:nth-child(9) , #benefits8 p:nth-child(8) , #benefits8 li , #benefits8 i , #benefits8 p:nth-child(3)'):
            d2.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        d1.append(', '.join(d2[0:4]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d1.append(', '.join(d2[5:]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(f"{d0[x]}: {d1[x]}")
        details.append(d)
    elif i == 9:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select(
                'p:nth-child(12) b , #platselectccbenefits2 p:nth-child(8) b , #platselectccbenefits2 p:nth-child(4) b'):
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        d2 = []
        for x in soup_4.select('#platselectccbenefits2 p:nth-child(9) , #platselectccbenefits2 li'):
            d2.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        d1.append(', '.join(d2[0:4]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d1.append(d2[4].replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        d1.append(', '.join(d2[5:]).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(f"{d0[x]}{'' if d0[x][-1] == ':' else ': '} {d1[x]}")
        details.append(d)
    elif i == 10:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select('#privileges .text-burgundy'):
            d0.append(x.get_text().replace('\n', '').replace('  ', '').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        for x in soup_4.select('#privileges p'):
            d1.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d1)):
            d.append(f"{d0[x]}: {d1[x]}")
        details.append(d)
    elif i == 11:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select('li b'):
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        q = soup_4.find('div', class_='tablert lead')
        for y in q.find_all('li'):
            z = y.get_text().split('\n')
            z.pop(0)
            d1.append(', '.join(z).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(f"{d0[x]}: {d1[x]}")
        details.append(d)
    elif i == 12:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select('p:nth-child(12) b , #benefits-new2 p:nth-child(8) b , #benefits-new2 p:nth-child(5) b'):
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        for x in soup_4.select('#benefits-new2 p:nth-child(9) , #benefits-new2 p:nth-child(6)'):
            d1.append(x.get_text().replace('\n', ', ').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        for x in soup_4.select('#benefits-new2 p:nth-child(12)'):
            q = x.get_text().split('\n')
            q.pop(0)
            d1.append(', '.join(q).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        for x in range(len(d0)):
            d.append(f"{d0[x]}{'' if d0[x][-1] == ':' else ': '} {d1[x]}")
        details.append(d)
    elif i == 13:
        d = []
        d0 = []
        d1 = []
        for x in soup_4.select('.card-title , .mb-3:nth-child(1) .text-bold')[4:]:
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        for x in soup_4.select('.ellip'):
            d1.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(f"{d0[x]}: {d1[x]}")
        details.append(d)
    elif i ==14:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select(
                'p:nth-child(17) b , p:nth-child(16) b , p:nth-child(15) b , p:nth-child(14) b , p:nth-child(13) b , p:nth-child(12) b , p:nth-child(11) b , p:nth-child(10) b , p:nth-child(9) b , p:nth-child(8) b , p:nth-child(7) b , #featuresID6 p:nth-child(6) b , p:nth-child(5) b , #featuresID6 p:nth-child(4) b')[
                 11:-1]:
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        for x in soup_4.select(
                'p:nth-child(17) , p:nth-child(16) , p:nth-child(15) , p:nth-child(14) , p:nth-child(13) , p:nth-child(12) , p:nth-child(11) , p:nth-child(10) , p:nth-child(9) , p:nth-child(8) , p:nth-child(7) , #featuresID6 p:nth-child(6) , #featuresID6 p:nth-child(5) , #featuresID6 p:nth-child(4)')[
                 22:-7]:
            d1.append(x.get_text().replace('\n', ' ').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(d1[x].replace(d0[x], d0[x] + ':'))
        details.append(d)
    elif i ==15:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select('.flights-h2-tag'):
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        for x in soup_4.select('.opshwList li:nth-child(1) , .flights-h2-tag+ p'):
            d1.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(f'{d0[x]}: {d1[x]}')
        details.append(d)
    elif i == 16:
        d = []
        d.append('https://www.indusind.com/content/dam/indusind-corporate/Other/welcomekit/voyage-benefit-guide.pdf')
        details.append(d)
    elif i == 17:
        d = []
        d0 = []
        d1 = []

        for x in soup_4.select('b'):
            d0.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in soup_4.select(
                'ul:nth-child(33) li+ li , ul:nth-child(30) li:nth-child(1) , ul:nth-child(27) li , ul:nth-child(24) li:nth-child(1) , ul:nth-child(21) li:nth-child(1) , ul:nth-child(16) li , ul:nth-child(12) li:nth-child(1) , ul:nth-child(5) li:nth-child(1)')[
                 1:]:
            d1.append(x.get_text().replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)

        for x in range(len(d0)):
            d.append(f"{d0[x]}: {d1[x]}")
        details.append(d)
    elif i == 18:
        d = []

        a = soup_4.select(
            '#abc3 p:nth-child(3) , p:nth-child(8) , p:nth-child(7) , #abc3 p:nth-child(6) , #abc3 p:nth-child(5) , #abc3 p:nth-child(4)')[
            2:-10]
        for x in range(len(a)):
            if x == 0:
                l = a[x].get_text().split('\n')
                l.pop(0)
                d.append(" ".join(l).replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
            else:
                d.append(a[x].get_text().replace('\n', " ").replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)
    elif i == 19:
        d = []

        for x in soup_4.select(
                '#benefits5 p:nth-child(7) , #benefits5 p:nth-child(6) , #benefits5 p:nth-child(5) , #benefits5 p:nth-child(4)'):
            d.append(x.get_text().replace('\n', ': ').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)
    elif i == 20:
        d = []
        for x in soup_4.select(
                'p:nth-child(8) , #benefits-sa4 p:nth-child(7) , p:nth-child(6) , #benefits-sa4 p:nth-child(5) , #benefits-sa4 p:nth-child(4)')[
                 4:]:
            d.append(x.get_text().replace('\n', ' ').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)
    elif i == 21:
        d = []
        for x in soup_4.select(
                '#benefits-new5 p:nth-child(10) , #benefits-new5 p:nth-child(9) , #benefits-new5 p:nth-child(8) , #benefits-new5 p:nth-child(7) , #benefits-new5 p:nth-child(6) , #benefits-new5 p:nth-child(5)'):
            d.append(x.get_text().replace('\n', ' ').replace('\xa0','').replace('\u20b9','').replace('\u00a0','').replace('\u2019','').replace('\u2018','').replace('\u2013','')
)
        details.append(d)

"""
Using the below code, keys and values will be fetched, a dictionary will be created for each card and 
appended to the 'final' list one by one
"""

key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "summary4_title", "summary4_desc","details", "image_url", "learn_more_url", "apply_link","eligibility"]
final = []
for i in range(len(cards)):
    x = {
        key[0]: "{:.2f}".format((i * 0.01) + 10),
        key[1]: cards[i],
        key[2]: "Welcome offer",
        key[3]: Welcome_Offer[i],
        key[4]: "Rewards",
        key[5]: Rewards[i],
        key[6]: "Specials",
        key[7]: Specials[i],
        key[8]: "Fees",
        key[9]: fees[i],
        key[10]: details[i],
        key[11]: img[i],
        key[12]: know_more[i],
        key[13]: apply_now[i],
        key[14]: eligibility[i]

    }
    final.append(x)

man = {
    "cards_information": final

}

print(man)

# creating a json file
import json
y = json.dumps(man,indent=2)
with open("indusind.json", "w") as outfile:
    outfile.write(y)

driver.close()