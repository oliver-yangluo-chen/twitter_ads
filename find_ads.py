import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
from bs4 import BeautifulSoup
from lxml import etree
from csv import writer

from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.chrome.service import Service 
import chromedriver_autoinstaller 
chromedriver_autoinstaller.install() 

from login import login

username = "j48072035"
password = "JimboTronWhoo"

driver = login(username, password)



#driver.set_window_size(1, 1000)

ads = []

def get_account(soup):
    account = soup.find('a', attrs={'role':'link', 'class':'css-175oi2r r-1wbh5a2 r-dnmrzs r-1ny4l3l r-1loqt21'})
    return account['href']

def list_to_str(ans):
    if isinstance(ans, list): return ans[0]
    if isinstance(ans, str): return ans
    return "UNKONWN TYPE: " + str(type(ans))

def get_text(soup):
    try:
        if soup.name == 'span' and " ".join(soup['class']) == 'css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3': #text
            ans = soup.contents
            return list_to_str(ans)
    except: print("UNKONWN TEXT")
    try:
        if soup.name == 'div' and " ".join(soup['class']) == 'css-175oi2r r-xoduu5': #@
            ans = soup.find('a', attrs={'class':'css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21'})['href']
            return list_to_str(ans)
    except: print("UNKNOWN @")
    try:
        if soup.name == 'img': #emoji
            ans = soup['alt']
            return list_to_str(ans)
    except: print("UNKNOWN EMOJI")
    try:
        if soup.name == 'span' and " ".join(soup['class']) == 'r-18u37iz': #hashtag
            ans = soup.find('a', attrs={'dir':'ltr'})['href']
            return list_to_str(ans)
    except: print("UNKNOWN #")
    try:
        if soup.name == 'a' and " ".join(soup['class']) == 'css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-1loqt21': #link
            ans = soup['href']
            return list_to_str(ans)
    except: print("UNKONWN LINK")
    return "???"


'''
css-146c3p1                                      r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe  r-16dba41 r-bnwqim
css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim
'''

def get_content(soup): #also include links?
    content = soup.find('div', attrs={'class':'css-146c3p1 r-8akbws r-krxsd3 r-dnmrzs r-1udh08x r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim'})
    if not content: content = soup.find('div', attrs={'class':'css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-bnwqim'})
    if not content: return None
    paragraphs = content.find_all()

    return "".join([get_text(p) for p in paragraphs])

def get_website(soup):
    website = soup.find('a', attrs={'class':'css-175oi2r r-1udh08x r-13qz1uu r-o7ynqc r-6416eg r-1ny4l3l r-1loqt21', 'role':'link', 'rel':'noopener noreferrer nofollow'})
    if website: return website['href']

def is_ad(soup):
    if soup.find('span', string='Ad') == None: return False
    return True

prev = ''
while True:
    time.sleep(0.025)
    driver.execute_script('window.scrollBy(0, 100);')

    try:
        #this also works for ads, just make more specific by looking for "ad" element
        p = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.XPATH, '//div[@class="css-175oi2r r-1igl3o0 r-qklmqi r-1adg3ll r-1ny4l3l"]')))
    except: continue


    try:
        soup = BeautifulSoup(p.get_attribute('innerHTML'), 'html.parser')

        if str(soup) == prev: continue
        #if not is_ad(soup): continue

        acc = get_account(soup)
        content = get_content(soup)
        website = get_website(soup)

        print("POST: ", acc, content, website)

        # stuff = [acc, content, website]

        # with open('ads.csv', 'a') as f:
        #     writer_object = writer(f)
        #     writer_object.writerow(stuff)
        #     f.close()

        prev = str(soup)
    except: pass


while True: pass
