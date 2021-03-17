# Execute the following in the Terminal

# pip install requests
# pip install bs4
# pip install lxml
# pip install selenium
# pip install urllib
#
# Install the chrome driver from https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json,requests
from selenium import webdriver


# Website url
citiurl = ['https://www.online.citibank.co.in/credit-card']

# Class name to grab a particular section of the html code
identity = ['productsEqualHeight gtabs demo']

html_1 = urlopen(citiurl[0])

# soup_1 is the source code of that web page
soup_1 = BeautifulSoup(html_1,'lxml')

# address is the particular section of the html code from that webpage
address = soup_1.find('div', class_ = identity[0])

# Titles of all the cards
cards = []

# Description of all the cards
desc = []

for x in address.find_all('h2'):
    cards.append(x.get_text())

for x in address.find_all('span'):
    if x.get_text() != "":
        desc.append(x.get_text())

# Fetching welcome offer, bonus, specials from the description list
welcome_offer = []
Bonus = []
Specials = []

for x in range(len(desc)):
    if x%4==0:
        welcome_offer.append(desc[x].replace('\u20b9','') + " and " + desc[x+1].replace('\u20b9',''))

j=2
for x in range(2,len(desc)):
    if x==j:
        Bonus.append(desc[x].replace('\u20b9','').replace('\u2019',''))
        j+=4

j=3
for x in range(3,len(desc)):
    if x==j:
        Specials.append(desc[x].replace("\u20b9","").replace("\u2122",""))
        j+=4



# learn_more_url
learn_more_url = []
m=1
for x in address.find_all("a", class_= "greyBtn blueBtnnew"):
    if m!=4:
        learn_more_url.append(x.get('href'))
        m+=1
    else:
        learn_more_url.append("https://www.online.citibank.co.in/credit-card/travel/citi-premiermiles-card?eOfferCode=INCCCCTWAFCTPMLM")
        m+=1

# Primary Image urls
img_1 = []
for x in address.find_all("img"):
    img_1.append("online.citibank.co.in"+x.get("src"))

# Secondary Image urls
img_2 = []
for x in learn_more_url:

    wb = webdriver.Chrome(executable_path="C:\\Users\\lenovo\\Downloads\\chromedriver.exe")  # The path of chromedriver.exe file
    wb.get(x)
    soup = BeautifulSoup(wb.page_source, 'lxml')
    img_2.append(soup.find('div', class_="m-top-sm block-hero-art-2 display-image").find('img').get('src'))

# Apply now urls
apply_now_url = []
for x in address.find_all('a',class_= "blueBtn"):
    apply_now_url.append(x.get('href'))

# Fees of all cards
fees = []
for x in range(4):
    html = urlopen(apply_now_url[x])
    soup = BeautifulSoup(html, 'lxml')
    s1 = [(1,4), (2,3), (0,4), (4,4)]
    addr = soup.find_all('ul', class_ = 'interstate-light')[s1[x][0]]
    fees.append(addr.find_all('li')[s1[x][1]].get_text().replace("#", "").replace("\u20b9",""))

fees.append("")



for x in learn_more_url[-1:-2:-1]:
    html = urlopen(x)
    soup =BeautifulSoup(html, 'lxml')
    fees.append(soup.select(".showcase_1_v9_item:nth-child(1) p")[0].get_text().replace("^","").replace("\u20b9",""))

# details of all the cards
final_details = []


for url in learn_more_url:
    html = requests.get(url)
    soup = BeautifulSoup(html.content, 'lxml')
    data = []

    for span in soup.select('span.m-bottom-0.display-text.font-weight-bold'):
        data.append(f'{span.get_text(strip=True)}: {span.find_next("span").get_text(strip=True)}'.replace('\n','').replace('\u2013','').replace('\u20b9',''))


    final_details.append(data[1:])





"""
Using the below code, keys and values will be fetched for each card, a dictionary will be created for each card and 
appended to the 'final' list one by one
"""

key = ["key", "name", "summary1_title", "summary1_desc", "summary2_title", "summary2_desc", "summary3_title",
       "summary3_desc", "summary4_title", "summary4_desc","details", "image_url","image_url_2" ,"learn_more_url",
       "apply_link", ]


final = []
for i in range(0, 6, 1):
    x = {
        key[0]: (i * 0.1) + 3,
        key[1]: cards[i],
        key[2]: "Welcome offer",
        key[3]: welcome_offer[i],
        key[4]: "Bonus",
        key[5]: Bonus[i],
        key[6]: "Specials",
        key[7]: Specials[i],
        key[8]: "Fees",
        key[9]: fees[i],
        key[10]: final_details[i],
        key[11]: img_1[i],
        key[12]: img_2[i],
        key[13]: learn_more_url[i],
        key[14]: apply_now_url[i]

    }
    final.append(x)

man = {
    "cards_information": final

}

print(man)

# creating a json file
import json
y = json.dumps(man,indent=2)
with open("citi.json", "w") as outfile:
    outfile.write(y)
