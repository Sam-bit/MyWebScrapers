'''
@author : Sambit Samal
@copyright : 
'''
import cfscrape,bs4
from os.path import join
import urllib.parse
import urllib.request
url = 'https://www.pexels.com/search/windows%2010%20wallpaper/?page=1'
urllist = []
def base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

scraper = cfscrape.create_scraper()
page = scraper.get(url)
soup = bs4.BeautifulSoup(page.text, 'html.parser')
for a in soup.find_all('a',href=True):
    urllist.append(urllib.parse.urljoin(base_url(url),a['href']))
res = [i for i in urllist if 'page=' in i]
maxid =  max([int(i.split('=', 1)[1]) for i in res])
for pageid in range(1,maxid):
    subpageurl = 'https://www.pexels.com/search/windows%2010%20wallpaper/?page='+str(pageid)
    soup = bs4.BeautifulSoup(scraper.get(subpageurl).text,'html.parser')
    # print(1)
    articles=soup.find_all('article',class_='photo-item photo-item--overlay')
    # print(articles)
    for article in articles:
        if article.attrs.get('data-photo-modal-download-url') is not None:
            downloadurl = urllib.parse.urljoin(base_url(url),article.attrs.get('data-photo-modal-download-url'))
            title = article.attrs.get('data-photo-modal-image-alt')
            location = article.attrs.get('data-photo-modal-user-profile-location') if article.attrs.get('data-photo-modal-user-profile-location') is not None else ''
            urllib.request.urlretrieve(downloadurl,join("D:\Windows 10 Wallpaper",title+'_'+location+'.jpg'))
