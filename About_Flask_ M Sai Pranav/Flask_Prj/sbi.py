from urllib.request import urlopen
from bs4 import BeautifulSoup
import json, time
start_007 = time.time()

sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#lifestyle-card-tab']
card_names=["SBI Card ELITE","Doctor'sSBI Card (in association with IMA)","SBI Card ELITE Advantage","Doctor's SBI Card"]
html_1=urlopen(sbiurl[0])
soup_1=BeautifulSoup(html_1, 'lxml')

learnmore_url=[]
address =soup_1.find('article', id="lifestyle")
for lis in address.find_all('a'):
        #print(lis.get('href'))
        txt=lis.get('href')
        check = 'https:'
        if(txt.startswith(check)):
            learnmore_url.append( txt );

links=[]
for i in range(len(learnmore_url)):
    if(i%2==0):
        links.append(learnmore_url[i])


welcome=[]
for i in range(0,4,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcome.append(lis.get_text().replace('\u00a0',''))


rewards=[]
for i in range(0,4,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        rewards.append(lis.get_text().replace("\u00a0",""))


fees=[]
for i in range(0,4,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('ul',class_="fee-list")
    for lis in address.find_all('li')[1:2]:
        #print(lis.get_text())
        fees.append(lis.get_text().replace("\u00a0",""))


global_acceptence=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[22:23]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[22:23]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\u2019",""))

add_oncards=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[30:31]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[29:30]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[30:31]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[29:30]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u2019","").replace("\u00a0",""))


emi=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[42:43]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[41:42]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[42:43]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[41:42]:
    #print(lis.get_text())
    emi.append(lis.get_text())


extended_credit=[]
for i in range(0,4,1):
    html_1=urlopen(links[0])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[5:6]:
        #print(lis.get_text())
        extended_credit.append(lis.get_text().replace("\u2019",""))

cash_advance=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[8:9]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[8:9]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())



cash_advancefee=[]
for i in range(0,4,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[13:14]:
        #print(lis.get_text())
        cash_advancefee.append(lis.get_text())



img=[]
image=[]
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',class_="grid-outer cards-data")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img.append(lis.get('data-original'))
image=img[::2]


apply_url=[]
address = soup_1.find('article', id="lifestyle")
for lis in address.find_all('a'):
        txt=lis.get('href')
        check = '/en/eapply/eapplyform.page?path=personal/credit-cards/lifestyle/'
        if(txt.startswith(check)):
            apply_url.append("https://www.sbicard.com"+txt)

demo=[]
for i in range(0,3,1):
    if(i==2):
        demo.append('')
    else:
        demo.append(apply_url[i])
demo.append(apply_url[2])



key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
lif=[]
for i in range(0,4,1):
    x={
        key[0]:format(((i * 0.01) + 1), '.2f'),
        key[1]:card_names[i],
        key[2]: "welcome",
        key[3]: welcome[i],
        key[4]: "rewards",
        key[5]:  rewards[i],
        key[6]: "fees",
        key[7]: fees[i],
        "details": [
            "Global Acceptance:"+global_acceptence[i],
            "Add-on Cards:"+add_oncards[i],
            "Balance Transfer on EMI:"+emi[i],
            "Extended Credit:"+extended_credit[i],
            "Cash Advance:"+cash_advance[i],
            "Cash Advance Fee:"+cash_advancefee[i]
        ],
        key[8]:image[i],
        key[9]:links[i],
        key[10]:demo[i].replace(" ","")
    }
    lif.append(x)



sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#reward-card-tab']
card_names=["SBI card PRIME","OLA Money SBI Card","Appollo SBI Card","SBI card PRIME Advantage","Paytm SBI Card SELECT","Paytm SBI Card"]
html_1=urlopen(sbiurl[0])
soup_1=BeautifulSoup(html_1, 'lxml')

learnmore_url=[]
address =soup_1.find('article', id="reward")
for lis in address.find_all('a'):
        #print(lis.get('href'))
        txt=lis.get('href')
        check = 'https:'
        if(txt.startswith(check)):
            learnmore_url.append( txt );

links=[]
for i in range(len(learnmore_url)):
    if(i%2==0):
        links.append(learnmore_url[i])

welcome=[]
for i in range(0,4,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcome.append(lis.get_text().replace("\u00a0",""))
for i in range(6,8,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcome.append(lis.get_text().replace("\u00a0",""))



rewards=[]
for i in range(0,4,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        rewards.append(lis.get_text())
for i in range(6,8,1):
    html_1=urlopen(links[i])
    soup_1=BeautifulSoup(html_1,'lxml')
    address=soup_1.find('div',class_="grid col-2")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        rewards.append(lis.get_text())

fees=[]
for i in range(0,4,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('ul',class_="fee-list")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        fees.append(lis.get_text().replace("\n","").replace("\u00a0",""))
for i in range(6,8,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('ul',class_="fee-list")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        fees.append(lis.get_text().replace("\n","").replace("\u00a0",""))



global_acceptence=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text())

html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[1:2]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text())

html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text())

html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text())

html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text())

html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text())

add_oncards=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[4:5]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[31:32]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[22:23]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0",""))



emi=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[31:32]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[17:18]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[31:32]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[36:37]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[27:28]:
    #print(lis.get_text())
    emi.append(lis.get_text())

extended_credit=[]
for i in range(0,3,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[5:6]:
        #print(lis.get_text())
        extended_credit.append(lis.get_text().replace("\u2019",""))

html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[5:6]:
    #print(lis.get_text())
    extended_credit.append(lis.get_text().replace("\u2019",""))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[5:6]:
    #print(lis.get_text())
    extended_credit.append(lis.get_text().replace("\u2019",""))






cash_advance=[]
for i in range(0,3,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[9:10]:
        cash_advance.append(lis.get_text())


html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())


cash_advancefee=[]
for i in range(0,3,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[13:14]:
        #print(lis.get_text())
        cash_advancefee.append(lis.get_text())


html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())

#card image
img_url=[]
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/rewards/sbi-card-prime.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/ola-money-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/rewards/apollo-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/rewards/sbi-card-prime-advantage.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/paytm-sbi-card-select.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/paytm-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))


apply_url=[]
address = soup_1.find('article', id="reward")
for lis in address.find_all('a'):
        txt=lis.get('href')
        check = '/en/eapply/eapplyform.page?path=personal/credit-cards/rewards/'
        if(txt.startswith(check)):
            apply_url.append("https://www.sbicard.com"+txt)
            #print("https://www.sbicard.com"+txt)

apply_demo=[]
for i in range(0,1,1):
    if(i==0):
        apply_demo.append('')

key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
final1=[]
x={
    key[0]:str(1.04),
    key[1]:card_names[0],
    key[2]: "welcome",
    key[3]: welcome[0],
    key[4]: "rewards",
    key[5]:  rewards[0],
    key[6]: "fees",
    key[7]: fees[0],
    "details": [
        "Global Acceptance:"+global_acceptence[0],
        "Add-on Cards:"+add_oncards[0],
        "Balance Transfer on EMI:"+emi[0],
        "Extended Credit:"+extended_credit[0],
        "Cash Advance:"+cash_advance[0],
        "Cash Advance Fee:"+cash_advancefee[0]
    ],
    key[8]:img_url[0],
    key[9]:learnmore_url[0],
    key[10]:apply_url[0].replace(" ",""),
}
lif.append(x)

key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
final2=[]
for i in range(0,1,1):
    x1={
        key[0]:str(1.05),
        key[1]:card_names[1],
        key[2]: "welcome",
        key[3]: welcome[1],
        key[4]: "rewards",
        key[5]:  rewards[1],
        key[6]: "fees",
        key[7]: fees[1],
        "details": [
            "Global Acceptance:"+global_acceptence[1],
            "Add-on Cards:"+add_oncards[1],
            "Balance Transfer on EMI:"+emi[1],
            "Extended Credit:"+extended_credit[1],
            "Cash Advance:"+cash_advance[1],
            "Cash Advance Fee:"+cash_advancefee[1]
        ],
        key[8]:img_url[1],
        key[9]:learnmore_url[3],
        key[10]:apply_demo[0].replace(" ",""),
    }
    lif.append(x1)


key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
final3=[]
for i in range(0,1,1):
    x2={
        key[0]:str(1.06),
        key[1]:card_names[2],
        key[2]: "welcome",
        key[3]: welcome[2],
        key[4]: "rewards",
        key[5]:  rewards[2],
        key[6]: "fees",
        key[7]: fees[2],
        "details": [
            "Global Acceptance:"+global_acceptence[2],
            "Add-on Cards:"+add_oncards[2],
            "Balance Transfer on EMI:"+emi[2],
            "Extended Credit:"+extended_credit[2],
            "Cash Advance:"+cash_advance[2],
            "Cash Advance Fee:"+cash_advancefee[2]
        ],
        key[8]:img_url[2],
        key[9]:learnmore_url[4],
        key[10]:apply_url[1].replace(" ","")
    }
    lif.append(x2)


key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
final4=[]
for i in range(0,1,1):
    x3={
        key[0]:str(1.07),
        key[1]:card_names[3],
        key[2]: "welcome",
        key[3]: welcome[3],
        key[4]: "rewards",
        key[5]:  rewards[3],
        key[6]: "fees",
        key[7]: fees[3],
        "details": [
            "Global Acceptance:"+global_acceptence[3],
            "Add-on Cards:"+add_oncards[3],
            "Balance Transfer on EMI:"+emi[3],
            "Extended Credit:"+extended_credit[3],
            "Cash Advance:"+cash_advance[3],
            "Cash Advance Fee:"+cash_advancefee[3]
        ],
        key[8]:img_url[3],
        key[9]:learnmore_url[6],
        key[10]:apply_demo[0].replace(" ",""),
    }
    lif.append(x3)



sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#reward-card-tab']
card_namestata=["Tata Platinum Card","Tata Titanium Card"]
html_1=urlopen(sbiurl[0])
soup_1=BeautifulSoup(html_1, 'lxml')


learnmore_urltata=[]
address =soup_1.find('article', id="reward")
for lis in address.find_all('a'):
        #print(lis.get('href'))
        txt=lis.get('href')
        check = 'https:'
        if(txt.startswith(check)):
            learnmore_urltata.append( txt );
    #Rewards.append(lis.get_text())
links=[]
for i in range(len(learnmore_urltata)):
    if(i%2==0):
        links.append(learnmore_urltata[i])


    tata_url=[]
for i in range(0,1,1):
    html_1=urlopen(links[4])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('article', id="premium")
    for lis in address.find_all('a'):
        txt=lis.get('href')
        check = 'https:'
        if(txt.startswith(check)):
            #print(txt)
            tata_url.append(txt);


welcometata=[]
for i in range(0,2,1):
    html_1=urlopen(tata_url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcometata.append(lis.get_text())



rewardstata=[]
for i in range(0,2,1):
    html_1=urlopen(tata_url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        rewardstata.append(lis.get_text())



feestata=[]
for i in range(0,2,1):
    html_1=urlopen(tata_url[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[1:2]:
        #print(lis.get_text())
        feestata.append(lis.get_text())


global_acceptencetata=[]
html_1=urlopen(tata_url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[8:9]:
    #print(lis.get_text())
    global_acceptencetata.append(lis.get_text())


html_1=urlopen(tata_url[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[8:9]:
    #print(lis.get_text())
    global_acceptencetata.append(lis.get_text())


add_oncardstata=[]
html_1=urlopen(tata_url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncardstata.append(lis.get_text())
html_1=urlopen(tata_url[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncardstata.append(lis.get_text())


emitata=[]
html_1=urlopen(tata_url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    emitata.append(lis.get_text())
html_1=urlopen(tata_url[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    emitata.append(lis.get_text())


extended_credittata=[]
html_1=urlopen(tata_url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[5:6]:
    #print(lis.get_text())
    extended_credittata.append(lis.get_text())
html_1=urlopen(tata_url[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[5:6]:
    #print(lis.get_text())
    extended_credittata.append(lis.get_text())


cash_advancetata=[]
html_1=urlopen(tata_url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advancetata.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(tata_url[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advancetata.append(lis.get_text().replace("\u00a0",""))


cash_advancefeetata=[]
html_1=urlopen(tata_url[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefeetata.append(lis.get_text())
html_1=urlopen(tata_url[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefeetata.append(lis.get_text())


url=[]
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('article',id="premium")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    url.append(lis.get('data-original'))
img_urltata=[]
for i in range(len(url)):
    if(i%2==0):
        img_urltata.append(url[i])

apply_urltata=[]
address = soup_1.find('article', id="premium")
for lis in address.find_all('a'):
        txt=lis.get('href')
        check = '/tata-en/eapply/eapplyform.page?path=personal/credit-cards/premium-cards/'
        if(txt.startswith(check)):
            apply_urltata.append("https://www.tatacard.com"+txt)
            #print("https://www.tatacard.com"+txt)



key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
finaltata=[]
for i in range(0,2,1):
    x={
        key[0]:str(1.07+(i*0.01)+0.01),
        key[1]:card_namestata[i],
        key[2]: "welcome",
        key[3]: welcometata[i],
        key[4]: "rewards",
        key[5]:  rewardstata[i],
        key[6]: "fees",
        key[7]: feestata[i],
        "details": [
            "Global Acceptance:"+global_acceptencetata[i],
            "Add-on Cards:"+add_oncardstata[i],
            "Balance Transfer on EMI:"+emitata[i],
            "Extended Credit:"+extended_credittata[i],
            "Cash Advance:"+cash_advancetata[i],
            "Cash Advance Fee:"+cash_advancefeetata[i]
        ],
        key[8]:img_urltata[i],
        key[9]:learnmore_urltata[i],
        key[10]:apply_urltata[i].replace(" ","")
    }
    lif.append(x)


key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
final5=[]
for i in range(0,1,1):
    x4={
        key[0]:format(1.10, '.2f'),
        key[1]:card_names[4],
        key[2]: "welcome",
        key[3]: welcome[4],
        key[4]: "rewards",
        key[5]:  rewards[4],
        key[6]: "fees",
        key[7]: fees[4],
        "details": [
            "Global Acceptance:"+global_acceptence[4],
            "Add-on Cards:"+add_oncards[4],
            "Balance Transfer on EMI:"+emi[4],
            "Extended Credit:"+extended_credit[4],
            "Cash Advance:"+cash_advance[4],
            "Cash Advance Fee:"+cash_advancefee[4]
        ],
        key[8]:img_url[4],
        key[9]:learnmore_url[12],
        key[10]:apply_demo[0].replace(" ",""),

    }
    lif.append(x4)


key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]

x5={
        key[0]:str(1.11),
        key[1]:card_names[5],
        key[2]: "welcome",
        key[3]: welcome[5],
        key[4]: "rewards",
        key[5]:  rewards[5],
        key[6]: "fees",
        key[7]: fees[5],
        "details": [
            "Global Acceptance:"+global_acceptence[5],
            "Add-on Cards:"+add_oncards[5],
            "Balance Transfer on EMI:"+emi[5],
            "Extended Credit:"+extended_credit[4],
            "Cash Advance:"+cash_advance[4],
            "Cash Advance Fee:"+cash_advancefee[4]
        ],
        key[8]:img_url[5],
        key[9]:learnmore_url[14],
        key[10]:apply_demo[0].replace(" ",""),
    }
lif.append(x5)




sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab']
identity=["shopping"]


html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address=soup_1.find('article', id='shopping')
name=[]
des=[]
for lis in address.find_all('h4')[:14]:
    #print(lis.get_text())
    name.append(lis.get_text())



sbiurl=["https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab"]
html_1= urlopen(sbiurl[0])
soup_1= BeautifulSoup(html_1, 'lxml')
links_=[]
address = soup_1.find('article', id="shopping")
for lis in address.find_all('a'):
    #print(lis.get('href'))
    txt=lis.get('href')
    check = 'https:'
    if(txt.startswith(check)):
        links_.append(txt);
links=[]
for i in range(len(links_)):
    if(i%2==0):
        links.append(links_[i])


welcome=[]
for i in range(0,19,1):
    html_1=urlopen(links_[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcome.append(lis.get_text())


Rewards=[]
for i in range(0,19,1):
    html_1=urlopen(links_[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2")
    for lis in address.find_all('li')[:2]:
        #print(lis.get_text())
        Rewards.append(lis.get_text())


Fee=[]
for i in range(0,16,1):
    html_1=urlopen(links_[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', id="feature-2-tab")
    for lis in address.find_all('li')[1:2]:
        #print(lis.get_text())
        Fee.append(lis.get_text().replace("\n",""))

img_url=[]
html_1=urlopen("https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab")
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('article',id="shopping")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))

img_url=img_url[::2]


sbiurl=["https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab"]
apply_link=[]

html_1=urlopen(sbiurl[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('article',id="shopping")
for lis in address.find_all('a'):
    #print(lis.get('href'))
    txt=lis.get('href')
    check = '/en/'
    if(txt.startswith(check)):
        apply_link.append("https://www.sbicard.com"+txt);
    else:
        print('')


sbiurl=["https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab"]
l_url=[]
html_1=urlopen(sbiurl[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('article',id="shopping")
for lis in address.find_all('a'):
    #print(lis.get('href'))
    txt=lis.get('href')
    check = 'https:'
    if(txt.startswith(check)):
        l_url.append(txt);
learn_more_url=[]
for i in range(len(l_url))[:32]:
    if(i%2==0):
        learn_more_url.append(l_url[i])


global_acceptance=[]
html_1=urlopen(learn_more_url[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[22:23]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:11]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[2])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:11]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[3])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[4])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[23:24]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[5])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[23:24]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[6])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[23:24]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[7])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[8])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[9])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[10])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[7:8]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[11])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[12])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[26:27]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[13])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[30:31]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[14])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[26:27]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[15])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[1:2]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())


add_oncards=[]
html_1=urlopen(learn_more_url[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[20:21]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[2])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[3])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[15:16]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[4])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[5])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[6])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[15:16]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[7])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[15:16]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[8])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[15:16]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[9])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[10])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[11])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[12])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[13])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[14])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
html_1=urlopen(learn_more_url[15])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())


cash_advance=[]
for i in range(0,15,1):
    html_1=urlopen(learn_more_url[i])
    soup_1= BeautifulSoup(html_1, 'lxml')
    address= soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[9:10]:
        #print(lis.get_text())
        cash_advance.append(lis.get_text())



cash_advance_fee=[]
for i in range(0,15,1):
    html_1=urlopen(learn_more_url[i])
    soup_1= BeautifulSoup(html_1, 'lxml')
    address= soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[13:14]:
        #print(lis.get_text())
        cash_advance_fee.append(lis.get_text())



key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
shop=[]
for i in range(0,14,1):
    x2={
        key[0]: format(1.11+(i*0.01)+0.01, '.2f'),
        key[1]: name[i],
        key[2]: "Welcome_offer",
        key[3]: welcome[i],
        key[4]: "Rewards",
        key[5]: Rewards[i].replace('\u00a0',''),
        key[6]: "Fee",
        key[7]: Fee[i],
        "details": [
            "Global Acceptance :"+global_acceptance[i].replace('\u00a0','').replace('\u2019',''),
            #"Add-on cards :"+add_oncards[i],
            "Cash Advance :"+cash_advance[i].replace('\u00a0','').replace('\u2019',''),
            "Cash Advance Fee :"+cash_advance_fee[i].replace('\u00a0','').replace('\u2019','')
        ],
        key[8]: img_url[i],
        key[9]: learn_more_url[i],
        key[10]:apply_link[i].replace(" ",""),
    }
    lif.append(x2)




sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab']

html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address=soup_1.find('article', id='shopping')
name=[]
des=[]
for lis in address.find_all('h4')[14:18]:
    #print(lis.get_text())
    name.append(lis.get_text())
for lis in address.find_all('h4')[19:20]:
    #print(lis.get_text())
    name.append(lis.get_text())



sbiurl=["https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab"]
html_1= urlopen(sbiurl[0])
soup_1= BeautifulSoup(html_1, 'lxml')
links_=[]
address = soup_1.find('article', id="shopping")
for lis in address.find_all('a')[42:53]:
    #print(lis.get('href'))
    txt=lis.get('href')
    check = 'https:'
    if(txt.startswith(check)):
        links_.append(txt);
links=[]
for i in range(len(links_)):
    if(i%2==0):
        links.append(links_[i])


rwds=[]
for i in range(1,5,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2 clear-left")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        rwds.append(lis.get_text().replace("\u00a0",""))



Rewards=[]
html_1=urlopen("https://www.sbicard.com/en/personal/credit-cards/shopping/sbi-card-unnati.page")
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div', class_="grid col-2")
for lis in address.find_all('li')[:1]:
    #print(lis.get_text())
    Rewards.append(lis.get_text().replace("\u00a0",""))
for i in range(1,5,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2 clear-left")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        Rewards.append(lis.get_text().replace("\u00a0",""))


Fee=[]
for i in range(0,5,1):
    html_1=urlopen(links_[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', id="feature-2-tab")
    for lis in address.find_all('li')[1:2]:
        #print(lis.get_text())
        Fee.append(lis.get_text().replace("\n",""))


img_url=[]
html_1=urlopen("https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab")
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('article',id="shopping")
for lis in address.find_all('img')[28:38]:
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))

img_url=img_url[::2]


sbiurl=["https://www.sbicard.com/en/personal/credit-cards.page#shopping-card-tab"]
l_url=[]
html_1=urlopen(sbiurl[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('article',id="shopping")
for lis in address.find_all('a')[43:57]:
    #print(lis.get('href'))
    txt=lis.get('href')
    check = 'https:'
    if(txt.startswith(check)):
        l_url.append(txt);
learn_more_url=[]
for i in range(len(l_url)):
    if(i%2==0):
        learn_more_url.append(l_url[i])


global_acceptance=[]
html_1=urlopen(learn_more_url[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[1:2]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[2])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[3])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[3:4]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(learn_more_url[4])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[3:4]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())


add_oncards=[]
html_1=urlopen(learn_more_url[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
add_oncards=[]
html_1=urlopen(learn_more_url[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
add_oncards=[]
html_1=urlopen(learn_more_url[2])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
add_oncards=[]
html_1=urlopen(learn_more_url[3])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[5:6]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())
add_oncards=[]
html_1=urlopen(learn_more_url[4])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[5:6]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text())


cash_advance=[]
for i in range(0,5,1):
    html_1=urlopen(learn_more_url[i])
    soup_1= BeautifulSoup(html_1, 'lxml')
    address= soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[9:10]:
        #print(lis.get_text())
        cash_advance.append(lis.get_text())


cash_advance_fee=[]
for i in range(0,5,1):
    html_1=urlopen(learn_more_url[i])
    soup_1= BeautifulSoup(html_1, 'lxml')
    address= soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[13:14]:
        #print(lis.get_text())
        cash_advance_fee.append(lis.get_text())


key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]

for i in range(0,5,1):
    x2={
        key[0]: format(1.25+(i*0.01)+0.01, '.2f'),
        key[1]: name[i],
        key[2]: "Welcome_offer",
        key[3]: "N/A",
        key[4]: "Rewards",
        key[5]: Rewards[i],
        key[6]: "Fee",
        key[7]: Fee[i],
        "details": [
            "Global Acceptance :"+global_acceptance[i].replace('\n',''),
            #"Add-on cards :"+add_oncards[i],
            "Cash Advance :"+cash_advance[i].replace('\n',''),
            "Cash Advance Fee :"+cash_advance_fee[i].replace('\n','')
        ],
        key[8]: img_url[i],
        key[9]: learn_more_url[i],
        key[10]: '',
    }
    lif.append(x2)





sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#travel---fuel-card-tab']
card_names=["BPCL SBI Card OCTANE","IRCTC SBI Card Premier","IRCTC SBI Card (on RuPay platform)","Club Vistara SBI Card PRIME","Club Vistara SBI Card","Etihad Guest SBI Premier Card","Etihad Guest SBI Card","BPCL SBI Card","Yatra SBI Card","Air India SBI Signature Card","Air India SBI Platinum Card","Chennai Metro SBI Card","Mumbai Metro SBI Card","Delhi Metro SBI Card","IRCTC SBI Platinum Card"]
html_1=urlopen(sbiurl[0])
soup_1=BeautifulSoup(html_1, 'lxml')

learnmore_url=[]
address =soup_1.find('article', id="travel---fuel")
for lis in address.find_all('a'):
        #print(lis.get('href'))
        txt=lis.get('href')
        check = 'https:'
        if(txt.startswith(check)):
            learnmore_url.append( txt );
    #Rewards.append(lis.get_text())
links=[]
for i in range(len(learnmore_url)):
    if(i%2==0):
        links.append(learnmore_url[i])


welcome=[]
for i in range(0,15,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcome.append(lis.get_text().replace("\u20b9","").replace("\u00a0",""))



rewards=[]
for i in range(0,15,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        rewards.append(lis.get_text().replace("\u00a0",""))


fees=[]
for i in range(0,15,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('ul',class_="fee-list")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        fees.append(lis.get_text().replace("\n"," ").replace("\u00a0"," "))



global_acceptence=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[7:8]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[22:23]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[21:22]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[14:15]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[14:15]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text())
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[15:16]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[15:16]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[3:4]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[5:6]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[20:21]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0"," "))


add_oncards=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[23:24]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[20:21]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[20:21]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[8:9]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[12:13]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[8:9]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[1:2]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[1:2]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[23:24]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0"," "))


emi=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[15:16]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[26:27]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019",""))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[44:45]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[44:45]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[17:18]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[14:15]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[22:23]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[25:26]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[14:15]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[14:15]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    emi.append(lis.get_text().replace("\u2019"," "))



extended_credit=[]
for i in range(0,15,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[5:6]:
        #print(lis.get_text())
        extended_credit.append(lis.get_text().replace("\u2019","").replace("\n"," "))


cash_advance=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())
    html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text().replace("\n"," "))



cash_advancefee=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[11:12]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
cash_advancefee=[]
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advancefee.append(lis.get_text())

#card image
img_url=[]
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/bpcl-sbi-card-octane.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/irctc-premier-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/irctc-rupay-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/irctc-premier-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/irctc-rupay-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/club-vistara-sbi-card-prime.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/club-vistara-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/etihad-guest-sbi-premier-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/etihad-guest-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/bpcl-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/yatra-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/air-india-sbi-signature-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/air-india-sbi-platinum-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/chennai-metro-sbi-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/mumbai-metro-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/delhi-metro-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/travel/irctc-sbi-platinum-card.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))



apply_url=[]
address = soup_1.find('article', id="travel---fuel")
for lis in address.find_all('a'):
        txt=lis.get('href')
        check = '/en/eapply/eapplyform.page?path=personal/credit-cards/travel/'
        check1='/en/eapply/eapplyform.page?path=personal/credit-cards/fuel/'
        if(txt.startswith(check)):
            apply_url.append("https://www.sbicard.com"+txt)
            #print("https://www.sbicard.com"+txt)
        if(txt.startswith(check1)):
            #print("https://www.sbicard.com"+txt)
            apply_url.append("https://www.sbicard.com"+txt)


key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
travel=[]
for i in range(0,15,1):
    x={
        key[0]:format(1.30+(i*0.01)+0.01, '.2f'),
        key[1]:card_names[i],
        key[2]: "welcome",
        key[3]: welcome[i],
        key[4]: "rewards",
        key[5]:  rewards[i],
        key[6]: "fees",
        key[7]: fees[i],
        "details": [
            "Global Acceptance:"+global_acceptence[i],
            "Add-on Cards:"+add_oncards[i],
            "Balance Transfer on EMI:"+emi[i],
            "Extended Credit:"+extended_credit[i],
            "Cash Advance:"+cash_advance[i],
            #"Cash Advance Fee:"+cash_advancefee[i]
        ],
        key[8]:img_url[i],
        key[9]:learnmore_url[i],
        key[10]:apply_url[i].replace(" ","")
    }
    lif.append(x)




sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#banking-partnership-card-tab']
card_names=["UCO Bank SBI Card ELITE","UCO Bank SBI Card PRIME","UCO Bank SimplySAVE SBI Card","Central Bank of India SBI Elite Card","Central Bank of India SBI Card Prime","Central Bank Of India SimplySave SBI Card","City Union Bank SBI Card PRIME","City Union Bank SimplySAVE SBI Card","Allahabad Bank SBI Card ELITE","Allahabad Bank SBI Card PRIME","Allahabad Bank SimplySAVE SBI Card","Karnataka Bank SBI Platinum Credit Card","Karnataka Bank SBI SimplySAVE Card","South Indian Bank SBI Platinum Credit Card","South Indian Bank Simply Save SBI Card","Federal Bank SBI Platinum Credit Card","Federal Bank SBI Credit Card","KVB SBI Signature Card","Karur Vysya Bank - SBI Platinum Credit Card","Karur Vysya Bank - SBI Card","Bank of Maharashtra - SBI Platinum Credit Card","Bank Of Maharashtra - SBI Card"]
html_1=urlopen(sbiurl[0])
soup_1=BeautifulSoup(html_1, 'lxml')


learnmore_url=[]
address =soup_1.find('article', id="banking-partnership")
for lis in address.find_all('a'):
        #print(lis.get('href'))
        txt=lis.get('href')
        check = 'https:'
        if(txt.startswith(check)):
            learnmore_url.append( txt );
    #Rewards.append(lis.get_text())
links=[]
for i in range(len(learnmore_url)):
    if(i%2==0):
        links.append(learnmore_url[i])



welcome=[]
for i in range(0,22,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcome.append(lis.get_text().replace("\u20b9",""))




rewards=[]
for i in range(0,22,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        rewards.append(lis.get_text().replace("\u00a0","").replace("\u20b9",""))



fees=[]
for i in range(0,22,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('ul',class_="fee-list")
    for lis in address.find_all('li')[1:2]:
        #print(lis.get_text())
        fees.append(lis.get_text().replace("\u00a0",""))


global_acceptence=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[18:19]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\u2019s","").replace("\n",""))
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\u2019","").replace("\n",""))
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[18:19]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[38:39]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\u2019","").replace("\n",""))
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[1:2]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[38:39]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[1:2]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0",""))
html_1=urlopen(links[15])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[38:39]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\u2019","").replace("\n",""))
html_1=urlopen(links[16])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[7:8]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[17])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[36:37]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[18])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[34:35]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[19])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[7:8]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\u2019","").replace("\n",""))
html_1=urlopen(links[20])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[34:35]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[21])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[7:8]:
    #print(lis.get_text())
    global_acceptence.append(lis.get_text().replace("\u00a0","").replace("\u2019","").replace("\n",""))


add_oncards=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[27:28]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[18:19]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u2019","").replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u2019","").replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[32:33]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[19:20]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[40:41]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u2019","").replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[4:5]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[40:41]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[4:5]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[15])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[40:41]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u2019","").replace("\u00a0","").replace("\n","").replace("\n",""))
html_1=urlopen(links[16])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[17])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[38:39]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[18])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[36:37]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[19])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u2019","").replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[20])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[36:37]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u00a0","").replace("\n",""))
html_1=urlopen(links[21])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[10:11]:
    #print(lis.get_text())
    add_oncards.append(lis.get_text().replace("\u2019","").replace("\u00a0","").replace("\n",""))


emi=[]
html_1=urlopen(links[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[39:40]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[1])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[31:32]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[2])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[26:27]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[3])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[44:45]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[4])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[31:32]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[5])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[23:24]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[6])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[31:32]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[7])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[43:44]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[8])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[44:45]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[9])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[31:32]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[10])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[23:24]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[11])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[25:26]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[12])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[18:19]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[13])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[25:26]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[14])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[18:19]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[15])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[25:26]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[16])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[24:25]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[17])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[22:23]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[18])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[20:21]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[19])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[24:25]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[20])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[20:21]:
    #print(lis.get_text())
    emi.append(lis.get_text())
html_1=urlopen(links[21])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[25:26]:
    #print(lis.get_text())
    emi.append(lis.get_text())



extended_credit=[]
for i in range(0,22,1):
    html_1=urlopen(links[0])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[5:6]:
        #print(lis.get_text())
        extended_credit.append(lis.get_text().replace("\u2019",""))


cash_advance=[]
for i in range(0,22,1):
    html_1=urlopen(links[0])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[9:10]:
        #print(lis.get_text())
        cash_advance.append(lis.get_text())


cash_advancefee=[]
for i in range(0,22,1):
    html_1=urlopen(links[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div',id="feature-2-tab")
    for lis in address.find_all('li')[13:14]:
        #print(lis.get_text())
        cash_advancefee.append(lis.get_text().replace("\u00a0",""))


img=[]
html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address = soup_1.find('article',id="banking-partnership")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img.append(lis.get('data-original'))
image=img[::2]


apply_url=[]
address = soup_1.find('article', id="banking-partnership")
for lis in address.find_all('a'):
    txt=lis.get('href')
    check = '/en/eapply/eapplyform.page?path=personal/credit-cards/banking-partnership/'
    if(txt.startswith(check)):
        apply_url.append("https://www.sbicard.com"+txt)
        #print("https://www.sbicard.com"+txt)




apply_link=[]
x=[11,13,14,15,16]
for i in range(0,22,1):
        if(i==x[0]):
            apply_link.append(apply_url[0])
        if(i==x[1]):
            apply_link.append(apply_url[1])
        if(i==x[2]):
            apply_link.append(apply_url[2])
        if(i==x[3]):
            apply_link.append(apply_url[3])
        if(i==x[4]):
            apply_link.append(apply_url[4])
        else:
            apply_link.append(" ")




key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
part=[]
for i in range(0,22,1):
    x={
        key[0]:format(1.45+(i*0.01)+0.01, '.2f'),
        key[1]:card_names[i],
        key[2]: "welcome",
        key[3]: welcome[i],
        key[4]: "rewards",
        key[5]:  rewards[i],
        key[6]: "fees",
        key[7]: fees[i],
        "details": [
            "Global Acceptance:"+global_acceptence[i],
            "Add-on Cards:"+add_oncards[i],
            "Extended Credit:"+extended_credit[i],
            #"Balance Transfer on EMI:"+emi[i],
            "Cash Advance:"+cash_advance[i],
            "Cash Advance Fee:"+cash_advancefee[i]
        ],
        key[8]:image[i],
        key[9]:links[i],
        key[10]:apply_link[i].replace(" ",""),
    }
    lif.append(x)





sbiurl=['https://www.sbicard.com/en/personal/credit-cards.page#business']
identity=["business"]

html_1=urlopen(sbiurl[0])
soup_1 = BeautifulSoup(html_1, 'lxml')
address=soup_1.find('article', id='business')
cards=[]
des=[]
for lis in address.find_all('h4'):
    #print(lis.get_text())
    cards.append(lis.get_text())

cards_name=[]
for i in range(len(cards)):
    if(i%2!=0):
        cards_name.append(cards[i])


for lis in address.find_all('li'):
    #print(lis.get_text())
    des.append(lis.get_text())


sbiurl=["https://www.sbicard.com/en/personal/credit-cards.page#business"]
html_1= urlopen(sbiurl[0])
soup_1= BeautifulSoup(html_1, 'lxml')
links_=[]
address = soup_1.find('article', id="business")
for lis in address.find_all('a'):
    #print(lis.get('href'))
    txt=lis.get('href')
    check = 'https:'
    if(txt.startswith(check)):
        links_.append(txt);
links=[]
for i in range(len(links_)):
    if(i%2==0):
        links.append(links_[i])


welcome=[]
for i in range(0,2,1):
    html_1=urlopen(links_[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="primary-view")
    for lis in address.find_all('li')[:1]:
        #print(lis.get_text())
        welcome.append(lis.get_text())


Rewards=[]
for i in range(0,2,1):
    html_1=urlopen(links_[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', class_="grid col-2")
    for lis in address.find_all('li')[1:2]:
        #print(lis.get_text())
        Rewards.append(lis.get_text())

Fee=[]
for i in range(0,2,1):
    html_1=urlopen(links_[i])
    soup_1 = BeautifulSoup(html_1, 'lxml')
    address = soup_1.find('div', id="feature-2-tab")
    for lis in address.find_all('li')[1:2]:
        #print(lis.get_text())
        Fee.append(lis.get_text())

global_acceptance=[]
html_1=urlopen(links[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())
html_1=urlopen(links[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[16:17]:
    #print(lis.get_text())
    global_acceptance.append(lis.get_text())


easy_bill=[]
html_1=urlopen(links[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[25:26]:
    #print(lis.get_text())
    easy_bill.append(lis.get_text())
html_1=urlopen(links[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-1-tab")
for lis in address.find_all('li')[28:29]:
    #print(lis.get_text())
    easy_bill.append(lis.get_text())


cash_advance=[]
html_1=urlopen(links[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())
html_1=urlopen(links[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[9:10]:
    #print(lis.get_text())
    cash_advance.append(lis.get_text())

cash_advance_fee=[]
html_1=urlopen(links[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advance_fee.append(lis.get_text())
html_1=urlopen(links[1])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('div',id="feature-2-tab")
for lis in address.find_all('li')[13:14]:
    #print(lis.get_text())
    cash_advance_fee.append(lis.get_text())

sbiurl=["https://www.sbicard.com/en/personal/credit-cards.page"]
img_url=[]
html_1=urlopen(sbiurl[0])
soup_1= BeautifulSoup(html_1, 'lxml')
address= soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/business/sbi-card-prime-business.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))
address= soup_1.find('a',href="https://www.sbicard.com/en/personal/credit-cards/business/sbi-card-elite-business.page")
for lis in address.find_all('img'):
    #print(lis.get('data-original'))
    img_url.append(lis.get('data-original'))

key=["key","name","summary1_title","summary1_desc","summary2_title","summary2_desc","summary3_title","summary3_desc","image_url","learn_more_url","apply_link"]
business=[]
for i in range(0,2,1):
    x2={
        key[0]: format(1.67+(i*0.01)+0.01, '.2f'),
        key[1]: cards[i],
        key[2]: "Welcome_offer",
        key[3]: welcome[i],
        key[4]: "Rewards",
        key[5]: Rewards[i],
        key[6]: "Fee",
        key[7]: Fee[i],
        "details": [
            "Global Acceptance :"+global_acceptance[i].replace('\u00a0',''),
            "easy_bill :"+easy_bill[i].replace('\u00a0',''),
            "Cash Advance :"+cash_advance[i].replace('\u00a0',''),
            "Cash Advance Fee :"+cash_advance_fee[i].replace('\u00a0','')
        ],
        key[8]: img_url[i],
        key[9]: links[i],
        key[10]: ''
    }
    lif.append(x2)
print(lif)


man={
    "cards_information":lif
}

y = json.dumps(man, indent = 2)
with open("sbi.json", "w") as outfile:
    outfile.write(y)


end_007 = time.time()

print(f"Runtime of the program is {end_007 - start_007}")


