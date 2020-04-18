from facts.db import insert_article, check_if_url_exists
from facts.utils import *

_FactCheckedBy = 'Alt News.In'
#def readEachArticle(url,thumbnail,conn):
def readEachArticle(url):
    soup = getUTF8Soup(url)
    title = soup.find('h1',class_="entry-title h1")
    if soup.find('a',class_="herald-author-name") is not None:
        authorname = soup.find('a',class_="herald-author-name").text
    else:
        authorname = soup.find('span',class_="fn").find('a').text
    contentdiv = soup.find('div',class_='entry-content herald-entry-content')
    if url == 'https://www.altnews.in/old-video-of-maratha-protest-shared-as-angry-public-in-assam-chasing-police-after-nrc/':
        contents = contentdiv.find('div', attrs={'dir': 'ltr'}).find('div', attrs={'dir': 'ltr'}).find('div', attrs={
            'dir': 'ltr'}).find_all(['ul', 'li', 'p', 'em'], recursive=False)
        article_claim = contents[0].text.replace("\xa0", " ").replace('\n', ' ')
        # pcontent = contentdiv.find('div', attrs={'dir': 'ltr'}).find('div', attrs={'dir': 'ltr'}).find('div', attrs={
        #     'dir': 'ltr'}).find('p',class_='Tweet-text e-entry-title')
        textcontent = ""
        for content in contents[1:]:
            textcontent = textcontent + content.text.replace("\xa0", " ").replace('\n', ' ')

        # textcontent = textcontent + pcontent.text.replace("\xa0", " ").replace('\n', ' ')
    elif url == 'https://www.altnews.in/pm-modi-spends-rs-80-lakh-a-month-on-make-up-madame-tussauds-video-viral-with-false-claim/':
        article_claim = contentdiv.find('div', class_="_437j").find('div').find('div').find('div').find(
            ['ul', 'li', 'p', 'em']).text.replace("\xa0", "").replace('\n', '')
        article_claim = article_claim + contentdiv.find('div', class_="_437j").find('div').find('div').find('div').text.replace("\xa0", "").replace('\n', '')
        textcontent = ""
        contentdivs = contentdiv.find_all('div',recursive=False)[2:4]
        for content in contentdivs:
            textcontents_allp = content.find_all(['ul', 'li', 'p', 'em'])
            for texts in textcontents_allp:
                textcontent = textcontent + texts.text.replace("\xa0", " ").replace('\n', ' ')
    elif url == 'https://www.altnews.in/video-of-man-selling-relief-material-at-grocery-shop-is-from-pakistan/':
        article_claim = contentdiv.find('p', recursive=False).text.replace("\xa0", " ").replace('\n', ' ')
        print(article_claim)
        contentdivs = contentdiv.find_all('div',recursive=False)
        textcontent = ""

        for content in contentdivs[1:2]:
            print(content)
            textcontents_allp = content.find_all(['ul', 'li', 'p', 'em'])
            for texts in textcontents_allp:
                textcontent = textcontent + texts.text.replace("\xa0", " ").replace('\n', ' ')
    else:
        contents = contentdiv.find_all(['ul', 'li', 'p', 'em'], recursive=False)
        article_claim = contents[0].text.replace("\xa0", " ").replace('\n', ' ')
        textcontent = ""
        for content in contents[1:]:
            textcontent = textcontent + content.text.replace("\xa0", " ").replace('\n',' ')
    # if contentdiv.find_all(['ul','li','p','em'],recursive=False) != []:
    #     contents = contentdiv.find_all(['ul', 'li', 'p', 'em'], recursive=False)
    # elif contentdiv.find('div',attrs={'dir':'ltr'}).find('div',attrs={'dir':'ltr'}).find('div',attrs={'dir':'ltr'}).find_all(['ul','li','p','em'],recursive=False) is not None:
    #     #https://www.altnews.in/old-video-of-maratha-protest-shared-as-angry-public-in-assam-chasing-police-after-nrc/
    #     contents = contentdiv.find('div',attrs={'dir':'ltr'}).find('div',attrs={'dir':'ltr'}).find('div',attrs={'dir':'ltr'}).find_all(['ul','li','p','em'],recursive=False)
    # else:
    #     #https://www.altnews.in/pm-modi-spends-rs-80-lakh-a-month-on-make-up-madame-tussauds-video-viral-with-false-claim/
    #     contents = contentdiv.find('div',class_="_437j").find('div').find('div').find('div').find_all(['ul', 'li', 'p', 'em'], recursive=False)
    #  article_claim = contents[0].text.replace("\xa0", "").replace('\n','')
    #
    # textcontent = ""
    # for content in contents[1:]:
    #     textcontent = textcontent + content.text.replace("\xa0", "").replace('\n','')
    updateddate = soup.find('span',class_="updated").text
    updateddatetrimmed = updateddate.split()[0].replace('st','').replace('th','').replace('nd','').replace('rd','')+" "+updateddate.split()[1]+" "+updateddate.split()[2]
    article = (unicodetoascii(url),
               unicodetoascii(title.text),
               #thumbnail,
               format_date(updateddatetrimmed,'%d %B %Y'),
               unicodetoascii(article_claim),
               unicodetoascii(textcontent),
               unicodetoascii(authorname),
               '',#any(x in title.text.lower() for x in ('no', 'false', 'did not','didn\'t'))==True then 'True' else ''
               _FactCheckedBy
               )
    print(article)
    #insert_article(conn,article)

readEachArticle('https://www.altnews.in/video-of-man-selling-relief-material-at-grocery-shop-is-from-pakistan/')
'''
def altnews_fetch(conn):
    i = 1
    while True:
        url = 'https://www.altnews.in/page/%d/'% i
        print(url)
        soup = getUTF8Soup(url)
        if not soup.find('article'):
            break
        else:
            for article in soup.find_all('article'):
                record_found = check_if_url_exists(conn,article.find('a')['href'])
                if not record_found:
                    if article.find('a', class_='fa-post-thumbnail') is not None:
                        thumbnail = imageurl_to_base64(
                            article.find('a', class_='fa-post-thumbnail').find('img').attrs.get('src'))
                    else:
                        thumbnail = imageurl_to_base64(
                            article.find('div', class_='herald-post-thumbnail herald-format-icon-middle').find('a').find('img').attrs.get('src'))
                    readEachArticle(article.find('a')['href'],thumbnail, conn)

        i = i + 1
        '''
