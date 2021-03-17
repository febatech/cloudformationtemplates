# Execute the following in the Terminal

# pip install requests
# pip install bs4
# pip install lxml
# pip install selenium
# pip install urllib

'''Install the chrome driver from https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/
ensure chromebrowser and chromedriver version are in compatible'''


from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, requests, re, sys
from selenium import webdriver

# Webiste url
AMEXurl = ['https://www.americanexpress.com/in/credit-cards/all-cards/?sourcecode=A0000FCRAA&cpid=100370494&dsparms=dc_pcrid_408453063287_kword_american%20express%20credit%20card_match_e&gclid=Cj0KCQiApY6BBhCsARIsAOI_GjaRsrXTdkvQeJWvKzFy_9BhDeBe2L2N668733FSHTHm96wrPGxkv7YaAl6qEALw_wcB&gclsrc=aw.ds']

# Class name to grab a particular section of the html code
identity = ['filmstrip_container']

driver = webdriver.Chrome(executable_path="C:\\Users\\lenovo\\Downloads\\chromedriver.exe") # Path of the chromedriver.exe file

# Titles of all the cards
cards = []


html_1 = urlopen(AMEXurl[0])

# soup_1 is the source code of the webpage
soup_1 = BeautifulSoup(html_1,'lxml')

# address is the particular section of the html code from that webpage
address = soup_1.find('div',attrs={"class" : identity[0]})

# Fetching titles
for x in address.find_all('span', class_ = 'filmstrip-name'):
        cards.append(x.get_text().replace("\xa0","").replace("\u00ae","").replace("\u2122",""))



r = requests.get(AMEXurl[0]).text
p = re.compile(r'imgurl":"(.*?)"')
img = p.findall(r)                                    # img links



link = 'https://www.americanexpress.com/in/credit-cards/payback-card/'
html = urlopen(link)
soup = BeautifulSoup(html,'lxml')

cards.append(soup.find('h1').get_text().replace('\xa0','').replace("\u00ae",""))

img.append(soup.find_all('img')[7].get('src'))

# Fetching learn_more and apply_now urls
for script in soup_1.find_all('script'):
    if script.contents and "intlUserSessionId" in script.contents[0]:
        json_raw = script.contents[0][script.contents[0].find('{'):]
        json_data = json.loads(json_raw)
        id = json_data["pageData"]["pageValues"]["intlUserSessionId"]

url2 = 'https://acquisition-1.americanexpress.com/api/acquisition/digital/v1/shop/us/cardshop-api/api/v1/intl/content/compare-cards/in/default'
r2 = requests.get(url2, params={'sessionId': id})
json_data = r2.json()

apply_now_url = []
learn_more_url = []

for entry in json_data:
    cta_group = entry["ctaGroup"][0]
    click_url = cta_group['clickUrl']

    if click_url[0] != 'c':
        apply_now_url.append(f"{click_url}")

    learn_more = entry['learnMore']['ctaGroup'][0]
    learn_more_url.append(f"{'https://americanexpress.com/in/'+learn_more['clickUrl']}")



# Arranging the learn_more and apply now urls
myorder = [4,5,0,3,2,1]
apply_now_url[:] = [apply_now_url[i] for i in myorder]


myorder = [5,-1,0,3,2,1,4,-2]
learn_more_url[:] = [learn_more_url[i] for i in myorder]


apply_now_url.extend(["",""])


welcome_offer = []
fees = []
RewardEarnRate = []
Rewards = []
eligibility = []
final_details = []

c=1
e=1
z=1

# Fetching welcome offer, fees, RewardEarnRate, Rewards, eligibility, and final_details
for link in range(len(learn_more_url)):
    if link not in [0,4]:
        html_3 = urlopen(learn_more_url[link])
        soup_3 = BeautifulSoup(html_3,'lxml')
        welcome_offer.append(soup_3.find('div', class_='card-detail__basic__welcome').get_text().replace('\xa0','').replace("\u00ae","").replace("\u2019","").replace("\u2018",""))
        fees.append(soup_3.find_all('div', class_ = 'description')[1].get_text())
        RewardEarnRate.append(soup_3.find_all('div', class_ = 'description')[2].get_text().replace('\xa0','').replace("\u00ae",""))
        if c<6:
            Rewards.append(soup_3.find('div', class_='containerStyle').get_text().replace('\xa0','').replace("\u00ae","").replace("\u2022",""))
            c+=1
        else:
            Rewards.append(soup_3.find('li', class_='card-detail__additional-feature').get_text().replace('\xa0','').replace("\u00ae","").replace("\u2022",""))

        if e<3:
            eligibility.append(soup_3.find_all('li', class_ = 'custom')[2].get_text())
            e+=1
        elif 2<e<6:
            eligibility.append(soup_3.find_all('li', class_='custom')[3].get_text())
            e += 1
        else:
            eligibility.append("")

        if z==1:
            a = 1
            details = []
            for span in soup_3.select(".why-amex__subtitle span"):
                # details.append(f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}{" EMI " if c==len(soup.select(".why-amex__subtitle span")) else ""}{span.find_next("span").find_next("span").get_text(strip=True)}')
                t = f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}{" EMI " if c == len(soup.select(".why-amex__subtitle span")) else ""}{span.find_next("span").find_next("span").get_text(strip=True)}'
                details.append(t.replace("\u00ae","").replace("\u00a0",""))
                a+=1
            z+=1
            final_details.append(details)


        elif z==2:
            b=1
            details = []
            for span in soup_3.select(".why-amex__subtitle span"):
                 # details.append(f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}{" EMI " if b==len(soup.select(".why-amex__subtitle span")) else ""}')
                 t = f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}{" EMI " if b==len(soup.select(".why-amex__subtitle span")) else ""}'
                 details.append(t.replace("\u00ae","").replace("\u00a0",""))
                 b+=1
            z+=1
            final_details.append(details)

        elif z==4:
            d=1
            details = []
            for span in soup_3.select(".why-amex__subtitle span"):
                 # details.append(f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}{" airport lounges " + span.find_next("span").find_next("span").get_text(strip=True) if d==3 else ""}')
                 t = f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}{" airport lounges " + span.find_next("span").find_next("span").get_text(strip=True) if d==3 else ""}'
                 details.append(t.replace("\u00ae","").replace("\u00a0",""))
                 d+=1
            z+=1
            final_details.append(details)

        else:
            details = []
            for span in soup_3.select(".why-amex__subtitle span"):
                # details.append(f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}')
                t = f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}'
                details.append(t.replace("\u00ae","").replace("\u00a0",""))
            z+=1
            final_details.append(details)

# Fetching welcome offer, fees, RewardEarnRate, Rewards, eligibility, and final_details for unique cards
for link in range(len(learn_more_url)):
    # amex platinum card
    if link == 0:
        driver.get(learn_more_url[link])
        w1,f1,rer1,r1,e1,d1 = ([],[],[],[],[],[[]])
        soup = BeautifulSoup(driver.page_source, 'lxml')

        wf = soup.find('div', class_='copy-text-modules__description___1Jiu4').get_text()
        w1.append(wf.replace('\xa0','').replace("\u00ae","").replace("\u2019","").replace("\u2018",""))

        f = soup.find('div', class_='copy-text-modules__annualFee___2mYyp').get_text()
        f1.append(f.replace('\u00a0',''))

        rer1.append("")

        r = soup.find('div', class_='index-modules__HighlightContainerStyle___2otVx').get_text()
        r1.append(r.replace('\xa0','').replace("\u00ae","").replace("\u2022",""))

        e = soup.find('div', class_="card-detail__eligibility__wrapper")
        ee = e.find_all('li', class_='custom')[5].get_text()
        e1.append(ee)

        for d in soup.select(".index-modules__benefitBlock___3NP1d"):
            t = f'{d.find("h3").get_text()} : {d.find("span").get_text()}'
            d1[0].append(t.replace('\xa0', '').replace("\u00ae","").replace("\u00a0",""))

        welcome_offer.insert(0,w1[0])
        fees.insert(0,f1[0])
        RewardEarnRate.insert(0,rer1[0])
        Rewards.insert(0,r1[0])
        eligibility.insert(0,e1[0])
        final_details.insert(0,d1[0])



    # gold card
    if link == 4:
        driver.get(learn_more_url[link])
        w2, f2, rer2, r2, e2, d2 = ([], [], [], [], [], [[]])
        soup = BeautifulSoup(driver.page_source, 'lxml')

        wf = soup.find('span', class_='bento-tooltip').get_text()
        w2.append(wf.replace('\xa0','').replace("\u00ae","").replace("\u2019","").replace("\u2018",""))

        f = soup.find('div', class_="card-detail__basic__repapr_desktop").get_text()
        f2.append(f.replace('\u00a0',''))

        ren = soup.select('.product-feature~ .product-feature+ .product-feature .description div')[0].get_text()
        rer2.append(ren.replace('\xa0','').replace("\u00ae",""))

        r = soup.select(
            '.containerStyle+ .containerStyle .long-form__list:nth-child(1) div , .width-50:nth-child(1) .long-form__list span')[
            0].get_text()
        r2.append(r.replace('\xa0','').replace("\u00ae","").replace("\u2022",""))

        e = soup.select('.custom:nth-child(5) span')[0].get_text()
        e2.append(e)

        for d in soup.select('.why-amex__col'):
            t = f'{d.find("h4").get_text()} : {d.find_all("span")[2].get_text() if soup.select(".why-amex__col")[3].find("a") == None else d.find_all("span")[2].get_text()}{d.find("a").get_text() if d.find("a") != None else ""}'
            d2[0].append(t.replace('\xa0', '').replace("\u00ae","").replace("\u00a0",""))

        welcome_offer.insert(4, w2[0])
        fees.insert(4, f2[0])
        RewardEarnRate.insert(4, rer2[0])
        Rewards.insert(4, r2[0])
        eligibility.insert(4, e2[0])
        final_details.insert(4, d2[0])





"""
Using the below code, keys and values will be fetched for each card, a dictionary will be created for each card and 
appended to the 'final' list one by one
"""

key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "summary4_title", "summary4_desc","summary5_title", "summary5_desc","details", "image_url", "learn_more_url", "apply_link", "details"]
final = []
for i in range(0, 8, 1):
    x = {
        key[0]: (i * 0.1) + 4,
        key[1]: cards[i],
        key[2]: "Welcome offer",
        key[3]: welcome_offer[i],
        key[4]: "RewardEarnRate",
        key[5]: RewardEarnRate[i],
        key[6]: "Rewards",
        key[7]: Rewards[i],
        key[8]: "Fees",
        key[9]: fees[i],
        key[10]: "Eligibility",
        key[11]: eligibility[i],
        key[12]: final_details[i],
        key[13]: img[i],
        key[14]: learn_more_url[i],
        key[15]: apply_now_url[i]

    }
    final.append(x)

man = {
    "cards_information": final

}

print(man)


# creating a json file
import json
y = json.dumps(man,indent=2)
with open("amex.json", "w") as outfile:
    outfile.write(y)













