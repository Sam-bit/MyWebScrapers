import urllib

import bs4
import cfscrape
import requests
import itertools

def permutation_with_repeats(seq, key):
    for _ in  itertools.product(seq, repeat=key):
        yield ''.join(_)
seq = list('abcdefghijklmnopqrstuvwzyz')
key = 2
a = permutation_with_repeats(seq, key)  # seq and key of arbitrary size > 0
plist =[x for x in a]
for i in range(1000, 9999):
    for j in range(len(plist)):
        url = 'https://prnt.sc/%s' % plist[j]+str(i)
        scraper = cfscrape.create_scraper()
        page = scraper.get(url)
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        imgpath = soup.find('img',class_='no-click screenshot-image')['src']
        name =soup.find('img',class_='no-click screenshot-image')['image-id']
        urllib.request.urlretrieve(imgpath,name + '.jpg')