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
        self.name = name
        self.link = link
        if link is None and name is None:
            raise ValueError("Please input link or name of the manga you would like to retrieve!")
        elif name is not None:
            self.addr = "{}{}".format(self.baseurl, name)
            print self.addr
            self.link = self.addr

        else:
            if ("http://mangafox.me/manga/" not in link):
                raise ValueError(("Input link {} is not a mangafox page!").format(link))
            self.name = link.split("/")[4]
        self.soup = self.get_soup(self.link)
        if "Search for  Manga at Manga Fox" in self.soup.find("title"):
            raise ValueError("Unable to find {} manga".format(self.name))
        elif "Manga Index - Manga Fox!" in self.soup.find("title"):
            raise ValueError("Unable to find manga from link".format(self.link))

        self.chapters = self.get_chapters()

    def get_soup(self, link):
        url = requests.get(link)
        soup = bs.BeautifulSoup(url.content)
        return soup

    def get_chapters(self):
        list = []
        ul = self.soup.findAll("ul", attrs={"class": "chlist"})
        for u in ul:
            for a in u.findAll("a", attrs={"class": "tips"}):
                list.insert(0, a['href'])
        return list

    def get_pages(self, chapter):
        chapterLink = "{}/c{}/".format(self.link, chapter)
        soup = self.get_soup(chapterLink)
        list = []

        select = soup.find("select", attrs={"class": "m"})
        length = len(select.findAll("option"))
        split = chapterLink.split("/")
        for i in range(1, length):
            split[-1] = "{}.html".format(i)
            pageLink = "/".join(split)
            list.append(pageLink)
        return list

    def make_dir(self, chapter):
        split = self.link.split("/")
        subfolder = "/".join(split[4:-1])

        dir = os.path.dirname(__file__)
        dir = "{}/{}".format(dir, subfolder)
        if not os.path.exists(dir):
            os.makedirs(dir)
            return dir
        else:
            return False

    def get_img(self, page):
        soup = self.get_soup(page)
        img = soup.find("img", attrs={"id": "image"})
        return img['src']

    def down_img(self, img, path):
        return urllib.urlretrieve(img, path)


def main():
    bleach = MangaFox(name='bleach')
    chaps = bleach.get_chapters()
    print chaps[0]
    print bleach.get_pages(100)
    print bleach.name
    print bleach.link


if __name__ == "__main__":
    main()

#link = "http://h.mfcdn.net/store/manga/25133/001.0/compressed/d000.jpg?token=bf1ccec29786275fb5e6664a766e38db&ttl=1494482400"
#urllib.urlretrieve(link,"test.jpg")
    # urllib.urlretrieve(img['src'], filepath)
    # filepath = self.make_dir(addr)
