from facts.db import insert_article, check_if_url_exists
from facts.utils import *
_FactCheckedBy = 'Snopes.com'
def readEachArticle(url,conn):
    soup = getUTF8Soup(url)
    title = soup.find('h1',class_="title")
    authorname = soup.find('a',class_="author").text
    #contents = soup.find('div',class_='content').find_all(['ul','li','p','em'],recursive=False)
    textcontent = ""
    if soup.find('div', class_='subtitle') is not None:
        textcontent = textcontent + soup.find('div', class_='subtitle').text
    #for content in contents:
    #    textcontent = textcontent + content.text.replace("\xa0", "").replace('\n','')
    updateddate = soup.find('span',class_="date date-published").text
    fact_verdict = ''
    if soup.find('div', class_='claim-review-block') is not None:
        fact_verdict = soup.find('div', class_='claim-review-block').find_all('span', class_='value')[-1].text
    article = (unicodetoascii(url),
               unicodetoascii(title.text),
               format_date(unicodetoascii(updateddate),'%d %B %Y'),
               unicodetoascii(textcontent),
               unicodetoascii(authorname),
                fact_verdict,
               _FactCheckedBy
               )
    print(article)
    #insert_article(conn,article)

def snopes_fetch(conn):
    i = 1
    while True:
        url = 'https://www.snopes.com/fact-check/page/%d/'% i
        soup = getUTF8Soup(url)
        if not soup.find('article'):
            break
        else:
            for article in soup.find_all('article',class_ ="media-wrapper"):
                record_found = check_if_url_exists(conn,article.find('a')['href'])
                if not record_found:
                    readEachArticle(article.find('a')['href'], conn)

        i = i + 1
