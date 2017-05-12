# TODO tidy up the code
# TODO create UI
# TODO read main manga page and pull out how many chapter available
# TODO function to choose download multiple chapters - number of chapter / all
import os
import urllib

import BeautifulSoup as bs
import requests

address = "http://mangafox.me/manga/hetalia_world_stars/"


def get_chapters(addr):
    url = requests.get(addr)
    soup = bs.BeautifulSoup(url.content)
    list = []
    ul = soup.find("ul", attrs={"class": "chlist"})
    for a in ul.findAll("a", attrs={"class": "tips"}):
        # clink = c.find("a",attrs={"class":"tips"})
        # print clc[]ink
        list.append(a['href'])
    return list


def get_pages(addr):
    url = requests.get(addr)
    soup = bs.BeautifulSoup(url.content)
    list = []

    select = soup.find("select", attrs={"class": "m"})
    length = len(select.findAll("option"))
    split = addr.split("/")
    lastSl = split[-1]
    print lastSl
    print length
    for i in range(1, length):
        pageLink = addr.replace(lastSl, "{}.html".format(i))
        list.append(pageLink)
    return list


def make_dir(addr):
    split = addr.split("/")
    chap = split[-2]
    name = split[-3]
    dir = os.path.dirname(__file__)
    dir = "{}/{}/{}".format(dir, name, chap)
    if not os.path.exists(dir):
        os.makedirs(dir)
        return dir
    else:
        return False


def down_img(addr, filepath):
    url = requests.get(addr)
    soup = bs.BeautifulSoup(url.content)
    img = soup.find("img", attrs={"id": "image"})
    return urllib.urlretrieve(img['src'], filepath)

#link = "http://h.mfcdn.net/store/manga/25133/001.0/compressed/d000.jpg?token=bf1ccec29786275fb5e6664a766e38db&ttl=1494482400"
#urllib.urlretrieve(link,"test.jpg")
