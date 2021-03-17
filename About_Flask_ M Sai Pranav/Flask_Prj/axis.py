from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, requests, re
from selenium import webdriver

axis_url = ["https://www.axisbank.com/retail/cards/credit-card"]

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


html = requests.get(axis_url[0])
soup = BeautifulSoup(html.content, 'lxml')

cards = []
desc =[]

welcome_offer = []
Rewards = []
Top_features = []

explore_more_url = []
apply_now_url =[]

url_d = "https://www.axisbank.com/AjaxService/GetCreditCardsProducts"

data = {"strcategory" : "[]", "strrewardtypes" :"[]"}
r = requests.post(url_d, data=data)

for entry in json.loads(r.json()[0]):
    cards.append(entry['Name'])

driver = webdriver.Chrome(executable_path="C:\\Users\\lenovo\\Downloads\\chromedriver.exe")
driver.get(axis_url[0])

soup_1 = BeautifulSoup(driver.page_source, 'lxml')


for d in soup_1.select('#ulCreditCard li li > span'):
    desc.append(d.get_text(' \n ',strip=True))


for l in range(0,len(desc),3):
    welcome_offer.append(desc[l].replace('\n',''))

for l in range(1,len(desc),3):
    Rewards.append(desc[l].replace('\n',''))

for l in range(2,len(desc),3):
    Top_features.append(desc[l].replace('\n',''))


links = []

for ls in soup_1.find_all('div', class_ = 'loanSubmit'):
    c=0
    for m in ls.find_all('a'):
        if m.get('href')[0] == '/':
            links.append('https://www.axisbank.com'+m.get('href'))
            c+=1
        else:
            links.append(m.get('href'))
            c+=1
    if c==1:
        links.append('')

a=0
b=1

for link in range(len(links)):
    try:
        explore_more_url.append(links[a])
        a+=2
    except:
        pass
    try:
        apply_now_url.append(links[b])
        b+=2
    except:
        pass


img_urls = []


for url in range(len(explore_more_url)):
    if url in [0,1,4,5,8,15,16,17,18]:
        page = requests.get(explore_more_url[url], headers=headers).text
        try:
            img_src_ = BeautifulSoup(page, "html.parser").select_one('.bannerWrapper img')["src"]
            img_urls.append(f"https://www.axisbank.com{img_src_}")
        except (KeyError, TypeError):
            continue

    elif url in [2,7,9,10,11,12,13,14,19,20,21,22,23,24]:
        img_urls.append("")
    elif url==3:
        driver.get(explore_more_url[url])
        soup_2 = BeautifulSoup(driver.page_source, 'lxml')
        img_urls.append(("https://www.axisbank.com" + soup_2.find('div', class_='front').find('img').get('src')))

    elif url==6:
        driver.get(explore_more_url[url])
        soup_2 = BeautifulSoup(driver.page_source, 'lxml')
        img_urls.append("https://www.axisbank.com" + soup_2.select('#knowCard .row')[0].find('img').get('src'))


fees = []

for x in range(len(explore_more_url)):
    if x in [3,6]:
        y = 'https://www.axisbank.com/service-charges-and-fees'
    elif x in [2,8,11,12,13,15,18,19,21,22]:
        y=explore_more_url[x]+"/fees-charges#menuTab"
    elif x in [24]:
        o = explore_more_url[x].split('/')
        o.pop(-1)
        y = "/".join(o)+"/fees-charges#menuTab"
    else:
        y = explore_more_url[x]+"/fees-and-charges#menuTab"

    driver.get(y)
    soup_3 = BeautifulSoup(driver.page_source, 'lxml')
    if x in [4]:
        fees.append(" ".join(soup_3.find('table', class_="tblData").find_all('tr')[0].get_text().split()))
        fees.append(" ".join(soup_3.find('table', class_="tblData").find_all('tr')[1].get_text().split()))
    elif x in [3,6]:
        if x==3:
            a = soup_3.find_all('table', class_='tblData k-table')[11]
            fees.append(" ".join(a.find_all('tr')[1].get_text().split()))
            fees.append(" ".join(a.find_all('tr')[2].get_text().split()))
        else:
            a = soup_3.find_all('table', class_='tblData k-table')[9]
            fees.append(" ".join(a.find_all('tr')[1].get_text().split()))
            fees.append(" ".join(a.find_all('tr')[2].get_text().split()))
    elif x in [11,12,13]:
        if x==11:
            fees.append(" ".join(soup_3.find('table', class_ = "tblData").find_all('tr')[1].get_text().split()[:5]))
            fees.append(" ".join(soup_3.find('table', class_ = "tblData").find_all('tr')[2].get_text().split()[:8]))
        elif x==12:
            u = soup_3.find('table', class_="tblData").find_all('tr')[1].get_text().split()[:7]
            del u[3:5]
            fees.append(" ".join(u))

            i = soup_3.find('table', class_="tblData").find_all('tr')[2].get_text().split()[:10]
            del i[6:8]
            fees.append((" ".join(i)))
        else:
            u = soup_3.find('table', class_="tblData").find_all('tr')[1].get_text().split()[:9]
            del u[3:7]
            fees.append((" ".join(u)))

            i = soup_3.find('table', class_="tblData").find_all('tr')[2].get_text().split()[:12]
            del i[6:10]
            fees.append(" ".join(i))

    elif x in [15]:
        fees.append(" ".join(soup_3.find('table', class_="tblData").find_all('tr')[1].get_text().split()[:6]))
        fees.append(" ".join(soup_3.find('table', class_ = "tblData").find_all('tr')[2].get_text().split()[:9]))

    else:
        fees.append(" ".join(soup_3.find('table', class_ = "tblData").find_all('tr')[1].get_text().split()))
        fees.append(" ".join(soup_3.find('table', class_ = "tblData").find_all('tr')[2].get_text().split()))



fees_final = []

for x in range(0,len(fees),2):
    fees_final.append((fees[x].replace('\u2013','')+" | "+fees[x+1].replace('\u2013','')))


details = []

for q in range(len(explore_more_url)):
    if q in [3,6]:
        if q==3:
            s = explore_more_url[q]
            driver.get(s)
            soup_4 = BeautifulSoup(driver.page_source, 'lxml')
            heading = []
            description = []
            for x in soup_4.select('.card-overlay-content'):
                if x.find('li') == None:
                    heading.append(x.get_text().replace('  ', '').replace('\n', ''))

                else:
                    l1 = []
                    for y in x.find_all('li'):
                        l1.append((y.get_text().replace('  ', '').replace('\n', '')))
                    description.append(" and ".join(l1).replace('\u201d','').replace('\u201c','').replace('\u2018','').replace('\u2019','').replace('\u2013','').replace('\t',''))
            temp = []
            for x in range(len(heading)):
                temp.append(f"{heading[x]} : {description[x]}")
            details.append(temp)
        else:
            s = explore_more_url[q]
            driver.get(s)
            soup_4 = BeautifulSoup(driver.page_source, 'lxml')
            heading = []
            desc = []

            for x in soup_4.select('.mgcrd-list .list-heading'):
                heading.append(x.get_text())

            for x in soup_4.select('.mgcrd-list'):
                if x.find('li') == None:
                    desc.append(x.find('p').get_text().replace('  ', '').replace('\n', '').replace('\u201d','').replace('\u201c','').replace('\u2018','').replace('\u2019','').replace('\u2013','').replace('\t',''))
                else:
                    l = []
                    for y in x.find_all('li'):
                        l.append(y.get_text())
                    desc.append(" and ".join(l).replace('  ', '').replace('\n', '').replace('\u201d','').replace('\u201c','').replace('\u2018','').replace('\u2019','').replace('\u2013','').replace('\t',''))

            temp = []
            for x in range(len(heading)):
                temp.append(f"{heading[x]} : {desc[x]}")
            details.append(temp)

    else:
        if q == 24:
            z = explore_more_url[q]+"#menuTab"
        else:
            z = explore_more_url[q]+"/features-benefits#menuTab"
        driver.get(z)
        soup_4 = BeautifulSoup(driver.page_source, 'lxml')
        det = []
        for x in soup_4.select('div.owl-stage div.owl-item'):
            try:
                a = x.find('h3').get_text().replace('/span>', '').replace("  ", "").replace('\n', '').replace('\xa0',
                                                                                                              '').replace('\u201d','').replace('\u201c','').replace('\u2018','').replace('\u2019','').replace('\u2013','').replace('\t','')
                l = []
                for y in x.find_all('li'):
                    l.append(y.get_text().replace('/span>', '').replace("  ", "").replace('\n', '').replace('\xa0', ''))
                if x.find_all('li') == []:
                    for m in x.find_all('p'):
                        l.append(
                            m.get_text().replace('/span>', '').replace("  ", "").replace('\n', '').replace('\xa0', ''))
                s = " and ".join(l).replace('\u201d','').replace('\u201c','').replace('\u2018','').replace('\u2019','').replace('\u2013','').replace('\t','')
                det.append(f"{a} : {s}")
            except:
                pass
        details.append(det)





key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "summary4_title", "summary4_desc","details", "image_url", "learn_more_url", "apply_link"]
final = []
for i in range(0, 25, 1):
    x = {
        key[0]: "{:.2f}".format((i * 0.01) + 6),
        key[1]: cards[i],
        key[2]: "Welcome offer",
        key[3]: welcome_offer[i],
        key[4]: "Rewards",
        key[5]: Rewards[i],
        key[6]: "Top Features",
        key[7]: Top_features[i],
        key[8]: "Fees",
        key[9]: fees_final[i],
        key[10]: details[i],
        key[11]: img_urls[i],
        key[12]: explore_more_url[i],
        key[13]: apply_now_url[i]

    }
    final.append(x)

man = {
    "cards_information": final

}

print(man)

import json
y = json.dumps(man,indent=2)
with open("axis.json", "w") as outfile:
    outfile.write(y)
