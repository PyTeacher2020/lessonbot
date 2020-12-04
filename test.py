from bs4 import BeautifulSoup as bs
import requests

def fcbook():
    r = requests.get("https://www.facebook.com/ProgresstechUA/")
    soup = bs(r.text, "html.parser")
    podsp = soup.find_all('div', class_="_4bl9")
    num_list = []

    podsp_p=podsp[2]
    subs=podsp_p.get_text()
    for word in subs:
        if word.isnumeric():
            num_list.append(word)
    #убираем скобки списка и выводим цифру
    subscribers=''.join(num_list)
    return subscribers

def inst():
    r = requests.get("https://www.instagram.com/progresstech.ua/?hl=ru")
    soup = bs(r.text, "html.parser")
    podpis = soup.find('meta',property="og:description")
    podp=podpis["content"]
    podpp=podp.split()
    ret = podpp[0]
    return ret

def vk():
    print("try")

    r=requests.get("https://vk.com/progresstech_ukraine")
    soup = bs(r.text, "html.parser")
    print (soup)