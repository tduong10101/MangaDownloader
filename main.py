import BeautifulSoup as bs
import urllib
import requests
import time
import os

address = "http://mangafox.me/manga/hana_haru/c001/1.html"
url = requests.get(address)
soup = bs.BeautifulSoup(url.content)
list = []
for o in soup.find("select",attrs={"class":"m"}):
    list.append(o)
list = [x for x in list if x != "\n" and x !=" " and "Comments" not in x]
# TODO tidy up the code
# TODO create UI
# TODO read main manga page and pull out how many chapter available
# TODO function to choose download multiple chapters - number of chapter / all
print len(list)
print list
for i in range(1,len(list)+1):
    link = "{}{}.html".format(address[:-6],i)
    split = (address.split("/"))
    chap = split[-2]
    name = split[-3]
    page = i

    filename = "{} {} {}".format(name,chap,page)
    #urllib.urlretrieve(link, "test.jpg")
    print link
    print filename

    dir = os.path.dirname(__file__)

    dir =  "{}/{}/{}".format(dir, name, chap)

    if not os.path.exists(dir):
        os.makedirs(dir)
    dir = "{}/{}.jpg".format(dir,page)
    print dir
    url = requests.get(link)
    soup = bs.BeautifulSoup(url.content)
    img = soup.find("img",attrs={"id":"image"})

    urllib.urlretrieve(img['src'], dir)

#link = "http://h.mfcdn.net/store/manga/25133/001.0/compressed/d000.jpg?token=bf1ccec29786275fb5e6664a766e38db&ttl=1494482400"
#urllib.urlretrieve(link,"test.jpg")
