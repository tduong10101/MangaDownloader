import BeautifulSoup as bs
import urllib
import requests

address = "http://mangafox.me/manga/hana_haru/c001/1.html"
url = requests.get(address)
soup = bs.BeautifulSoup(url.content)
list = []
for o in soup.find("select",attrs={"class":"m"}):
    list.append(o)
list = [x for x in list if x != "\n" and x !=" " and "Comments" not in x]

print len(list)
print list
#link = "http://h.mfcdn.net/store/manga/25133/001.0/compressed/d000.jpg?token=bf1ccec29786275fb5e6664a766e38db&ttl=1494482400"
#urllib.urlretrieve(link,"test.jpg")
