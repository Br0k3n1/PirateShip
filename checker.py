from time import sleep
from selenium import webdriver
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from threading import Lock

###########
### DDS ###
###########

s_print_lock = Lock()
def s_print(*a, **b):
    """Thread safe print function"""
    with s_print_lock:
        print(*a, **b)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

def crackhub(game):
    URL = f"https://crackhub.site/?s={game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"rel":"bookmark"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"CrackHub: {target_URL}")

def scene_crackhub(game):
    URL = f"https://scene.crackhub.site/?s={game}"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL = soup.find("a",{"rel":"bookmark"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Scene CrackHub: {target_URL}")

# Selenium (make sure to include chrome_options.add_argument("--headless"))
def csrinru(game):
    URL = f"https://cs.rin.ru/forum/search.php?keywords={game}&terms=any&author=&sc=1&sf=titleonly&sk=t&sd=d&sr=topics&st=0&ch=300&t=0&submit=Search"
    driver.get(URL)
    sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    try:
        target_URL = soup.find("a",{"class":"topictitle"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":

        target_URL = target_URL[1:]
        target_URL = f"https://cs.rin.ru/forum{target_URL}"

        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"CSRINRU: {target_URL}")

def downloadha(game):
    URL = f"https://www.downloadha.com/?s={game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"rel":"bookmark"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"DownloadHa: {target_URL}")

def gload(game):
    URL = f"https://gload.to/?s={game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"style":"position: absolute; top: 0; right: 0; bottom: 0; left: 0; width: 100%; height: 100%;"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Gload: {target_URL}")

def ova(game):
    URL = f"https://www.ovagames.com/?s={game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"rel":"bookmark"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Ova: {target_URL}")

def rlsbb(game):
    URL = f"https://search.rlsbb.ru/?s={game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"rel":"bookmark"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"RLSBB: {target_URL}")

def scnlog(game):
    URL = f"https://scnlog.me/search/{game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"rel":"bookmark"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Scnlog: {target_URL}")

def steamrip(game):
    URL = f"https://steamrip.com/?s={game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"class":"all-over-thumb-link"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":

        target_URL = f"https://steamrip.com/{target_URL}"
        
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"SteamRip: {target_URL}")

###############
### Repacks ###
###############

def darck(game):
    URL = f"https://darckrepacks.com/search/?q={game}&quick=1"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"data-linktype":"link"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Darck: {target_URL}")

def elamigos(game):
    URL = 'https://elamigos.site/'
    target_URL = "No Pirate Avalible"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    games = soup.find_all("h3")
    for element in games:
        if game.lower() in element.text.lower():
            target_URL = element.a.get('href')
            break
    s_print(f"Elamigos: {target_URL}")

def fitgirl(game):
    URL = f'https://fitgirl-repacks.site/?s={game}'
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"rel":"bookmark"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"FitGirl: {target_URL}")

def gnarly(game):
    URL = f"https://www.gnarly-repacks.site/?s={game}"
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("h2",{"class":"loop-entry-title"}).a.get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Gnarly: {target_URL}")

def scooter(game):
    URL = f'https://scooter-repacks.site/?s={game}'
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"class":"continue-reading button bordered hide-on-mobile"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Scooter: {target_URL}")

############
### MISC ###
############

def online_fix(game):
    URL = f'https://online-fix.me/index.php?do=search&subaction=search&story={game}'
    target_URL = None
    r = requests.get(URL)
    soup = BeautifulSoup(r.content,"html.parser")
    try:
        target_URL =soup.find("a",{"class":"big-link"}).get('href')
    except:
        target_URL = "No Pirate Avalible"
    
    if target_URL != "No Pirate Avalible":
        words = game.split()
        is_word_in_url = True
        for word in words:
            if word not in target_URL:
                is_word_in_url = False
                break
        if not is_word_in_url:
            target_URL = f"{target_URL} (Likely Not Desired Game)"
    
    s_print(f"Online Fix: {target_URL}")