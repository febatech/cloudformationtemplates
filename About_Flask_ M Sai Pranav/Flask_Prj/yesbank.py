# Execute the following in the Terminal

# pip install requests
# pip install bs4
# pip install lxml
# pip install selenium
# pip install urllib

import requests, json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

#website url
weburl = 'https://apply.yesbank.in/'

#Get url html
r = requests.get(weburl)

#Get the respected Div's
soup = BeautifulSoup(r.text, features="lxml")
first_cards = soup.find("div",{"id":"tab-1"}).find_all("div",{"class":"slide"})
premia_cards = soup.find("div",{"id":"tab-2"}).find_all("div",{"class":"slide"})
business_cards = soup.find("div",{"id":"tab-3"}).find_all("div",{"class":"slide"})

#Combine all cards div blocks to one
cards = []
cards.extend(first_cards)
cards.extend(premia_cards)
cards.extend(business_cards)

Rewards = []
benefits = []
specials = []
fees = ['', '']
eligibility = []
details = []

#Benefits of all cards appended to benefits list
for x in soup.select(".mtb10+ center p"):
  benefits.append(x.get_text().strip().split('.')[0])

#Rewards of all cards appended to Rewards list
for x in soup.select('li:nth-child(2)')[1:3]:
  Rewards.append(x.get_text())
for x in soup.select('#landing_page_points-10 li:nth-child(4)'):
  Rewards.append(x.get_text())
for x in soup.select('#landing_page_points-3 li:nth-child(5) , #landing_page_points-5 li:nth-child(5)'):
  Rewards.append(x.get_text())
for x in soup.select('#landing_page_points-1 li:nth-child(5)'):
  Rewards.append(x.get_text())
for x in soup.select('#landing_page_points-2 li:nth-child(6) , #landing_page_points-4 li:nth-child(6)'):
  Rewards.append(x.get_text())
for x in soup.select('li:nth-child(5)')[-2::1]:
  Rewards.append(x.get_text())

# Specials of all cards appended to specials list
for x in soup.select('li:nth-child(9)')[:4]:
  specials.append(x.get_text())
for x in soup.select('#landing_page_points-3 li:nth-child(4),#landing_page_points-1 li:nth-child(4)'):
  specials.append(x.get_text())
for x in soup.select('#landing_page_points-2 li:nth-child(3) , #landing_page_points-4 li:nth-child(3)'):
  specials.append(x.get_text())
for x in soup.select('li:nth-child(9)')[4:]:
  specials.append(x.get_text())

#Fees of all cards appended to fees list
for x in soup.select('li:nth-child(1)')[3:]:
  fees.append(x.get_text())

# eligibility of all cards appended to eligibility list
for x in soup.select('li:nth-child(3)')[1:7]:
  eligibility.append(x.get_text().split(':')[1])
for x in soup.select('#landing_page_points-2 li:nth-child(2) , #landing_page_points-4 li:nth-child(2)'):
  eligibility.append(x.get_text().split(':')[1])
for x in soup.select('li:nth-child(3)')[9:]:
  eligibility.append(x.get_text().split(':')[1])

# List of learn more urls, will be used to fetch details from these links
learn_more_ig = []

for x in cards:
  a_tags = x.find_all("a")
  learn_more_ig.append(a_tags[2]["href"])



#details
for x in range(len(learn_more_ig)):
    options = Options()
    options.headless = True
    options.set_preference("dom.webdriver.enabled", False)
    # Install Mozilla Firefox browser
    # Download a geckodriver from this https://github.com/mozilla/geckodriver/releases
    # executable path must be the path of the geckodriver.exe file
    driver = webdriver.Firefox(options=options, executable_path="C:\\Users\\lenovo\\Downloads\\geckodriver.exe")
    driver.get(learn_more_ig[x])

    d = []
    d0 = []
    d1 = []

    if x == 0 or x == 1 or x == 2 or x == 3 or x == 4 or x == 5 or x == 6 or x == 7:

        element = WebDriverWait(driver, 10).until(
            EC.title_contains('YES'))
        soup_1 = BeautifulSoup(driver.page_source, 'lxml')

        if x == 0 or x == 1:

          for x in soup_1.select(
                  'li:nth-child(8) u , li:nth-child(7) u , ul~ p+ ul u , li:nth-child(6) u , li:nth-child(5) u')[:4]:
            d0.append(x.get_text())
          l = []
          counter = 0
          for x in soup_1.select(
                  'ul~ ul ul li:nth-child(3) p , ul~ p+ ul ul li:nth-child(2) p , ul~ p+ ul ul li:nth-child(1) p , li:nth-child(6) li:nth-child(3) p , p+ ul li:nth-child(6) li:nth-child(2) p , p+ ul li:nth-child(6) li:nth-child(1) p , li:nth-child(5) li:nth-child(3) p , li:nth-child(5) li:nth-child(2) p , p+ ul li:nth-child(5) li:nth-child(1) p'):
            l.append(x.get_text())
            counter += 1
            if counter == 3 or counter == 6 or counter == 9 or counter == 12 or counter == 15:
              d1.append(', '.join(l).replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))
              l.clear()
          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")
          details.append(d)

        elif x == 2:
          for x in soup_1.select(
                  'u strong , ul+ ul li:nth-child(3) u , ul:nth-child(1) li:nth-child(1) u , p~ ul+ ul li+ li u'):
            d0.append(x.get_text())
          l = []
          counter = 0
          for x in soup_1.select(
                  'ol li:nth-child(2) p , ol li:nth-child(1) p , ul+ ul li:nth-child(3) li p , .accData div li:nth-child(1) li:nth-child(2) p , ul:nth-child(1) li:nth-child(1) li:nth-child(1) p , p~ ul+ ul li+ li li p'):
            l.append(x.get_text())
            counter += 1
            if counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter == 10:
              d1.append(', '.join(l).replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))
              l.clear()
          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")
          details.append(d)

        elif x == 3:
          for x in soup_1.select(
                  'u strong , li:nth-child(6) u , ul:nth-child(7) li:nth-child(1) u , ul:nth-child(3) li:nth-child(5) u , ul:nth-child(3) li:nth-child(4) u'):
            d0.append(x.get_text())
          l = []
          counter = 0
          for x in soup_1.select(
                  'ol li:nth-child(4) p , ol li:nth-child(3) p , li:nth-child(6) li p , li:nth-child(1) li:nth-child(3) p , ul:nth-child(7) li:nth-child(1) li:nth-child(1) p , li:nth-child(5) li:nth-child(2) p , ul:nth-child(3) li:nth-child(5) li:nth-child(1) p , .introText~ ul li:nth-child(4) li:nth-child(2) p , ul:nth-child(3) > li:nth-child(4) li:nth-child(1) p'):
            l.append(x.get_text())
            counter += 1
            if counter == 2 or counter == 4 or counter == 6 or counter == 8 or counter == 10:
              d1.append(', '.join(l).replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))
              l.clear()
          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")
          details.append(d)

        elif x == 4:
          for x in soup_1.select('.bannerSlide #null , .accData u')[1:-1]:
            d0.append(x.get_text())
          for x in soup_1.select('ol li:nth-child(1) p , li li:nth-child(1) p')[1:]:
            d1.append(x.get_text().replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))

          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")
          details.append(d)

        elif x ==5:
          for x in soup_1.select('.keys div'):
            d0.append(x.get_text())
          for x in soup_1.select('.keys p'):
            if x.get_text() != '\n' and x.get_text() != '':
              d1.append(x.get_text().replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))
          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")
          details.append(d)

        elif x == 6 or x == 7:
          for x in soup_1.select('.accData u')[:-1]:
            d0.append(x.get_text())
          for x in soup_1.select('ol li:nth-child(6) p , li li:nth-child(1) p')[1:]:
            if x.get_text() != '\n' and x.get_text() != '':
              d1.append(x.get_text().replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))
          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")
          details.append(d)

        driver.quit()

    elif x == 8 or x == 9:

        element = WebDriverWait(driver, 10).until(
            EC.title_contains('Yes'))
        soup_1 = BeautifulSoup(driver.page_source, 'lxml')

        if x == 8:

          for x in soup_1.select(
                  'u strong , ul:nth-child(21) p > strong , ul:nth-child(19) strong , ul:nth-child(17) strong , ul:nth-child(15) li+ li strong , ul:nth-child(13) strong , ul:nth-child(10) strong , ul:nth-child(7) strong')[
                   :13]:
            d0.append(x.get_text().replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))

          for x in soup_1.select(
                  'ol li:nth-child(5) p , ul:nth-child(21) ul li:nth-child(1) p , ul:nth-child(19) ul p , ul:nth-child(17) ul li:nth-child(1) p , ul:nth-child(15) ul li:nth-child(1) p , ul:nth-child(13) ul li:nth-child(1) p , ul:nth-child(10) ul p , ul:nth-child(7) > li li:nth-child(1) p'):
            if x.get_text()[0] != "A":
              d1.append(x.get_text().replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))

          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")

          details.append(d)

        elif x == 9:
          for x in soup_1.select('li p > strong')[:14]:
            d0.append(x.get_text().replace(':', '').replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))

          for x in soup_1.select('.introText~ ul ul li:nth-child(1) p'):
            if x.get_text()[0] != "A":
              d1.append(x.get_text().replace('\u00ae','').replace('\u2122','').replace('\u2013','').replace('\u2018',''))

          for x in range(len(d0)):
            d.append(f"{d0[x]} : {d1[x]}")

          details.append(d)

        driver.quit()

# To contain list of dictionaries of each card
dict_list = []
start = 9  # start number of key ; every other card will be updated by +0.1
for id, card in enumerate(cards):
  dict_card = {}

  # key
  dict_card["key"] = start + id * (1e-1)
  # Name
  dict_card["name"] = card.h2.text

  dict_card["summary1_title"] = "Rewards"
  dict_card["summary1_desc"] = Rewards[id]

  dict_card["summary2_title"] = "Benefits"
  dict_card["summary2_desc"] = benefits[id]

  dict_card["summary3_title"] = "Specials"
  dict_card["summary3_desc"] = specials[id]

  dict_card["summary4_title"] = "Fees"
  dict_card["summary4_desc"] = fees[id]

  dict_card["summary5_title"] = "Eligibility"
  dict_card["summary5_desc"] = eligibility[id]

  dict_card["details"] = details[id]

  # Image_url
  dict_card["image_url"] = "https://apply.yesbank.in/" + card.img["src"]
  a_tags = card.find_all("a")

  # learn_more_url
  dict_card["learn_more_url"] = a_tags[2]["href"]

  # apply_link
  dict_card["apply_link"] = "https://apply.yesbank.in" + a_tags[0]["href"]
  dict_list.append(dict_card)


final_dict = dict({"cards_information": dict_list})

print(final_dict)

# Creates a json file
with open("yesbank.json", "w") as outfile:
    final = json.dumps(final_dict,indent=2)
    outfile.write(final)


