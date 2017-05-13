# TODO tidy up the code
# TODO create UI
# TODO read main manga page and pull out how many chapter available
# TODO function to choose download multiple chapters - number of chapter / all
import os
import urllib

import BeautifulSoup as bs
import requests

address = "http://mangafox.me/manga/hetalia_world_stars/"


class MangaFox:
    def __init__(self, link=None, name=None):
        self.baseurl = "http://mangafox.me/manga/"
        if link is None and name is None:
            raise ValueError("Please input link or name of the manga you would like to download!")
        elif name is not None:
            addr = "{}{}".format(self.baseurl, name)
            print addr
            self.link = addr

        else:
            if ("http://mangafox.me/manga/" not in link):
                raise ValueError(("Input link {} is not a mangafox page!").format(link))
            self.link = link

        soup = self.get_soup(self.link)
        if "Search for  Manga at Manga Fox" in soup.find("title"):
            raise ValueError("Unable to find {} manga".format(name))
        elif "Manga Index - Manga Fox!" in soup.find("title"):
            raise ValueError("Unable to find {} manga".format(name))

    def get_soup(self, link):
        url = requests.get(link)
        soup = bs.BeautifulSoup(url.content)
        return soup

    def get_chapters(addr):
        url = requests.get(addr)
        soup = bs.BeautifulSoup(url.content)
        list = []
        ul = soup.find("ul", attrs={"class": "chlist"})
        for a in ul.findAll("a", attrs={"class": "tips"}):
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
        subfolder = "/".join(split[4:-1])

        dir = os.path.dirname(__file__)
        dir = "{}/{}".format(dir, subfolder)
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
