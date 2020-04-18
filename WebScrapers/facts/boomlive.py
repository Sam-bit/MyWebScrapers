from facts.db import insert_article, check_if_url_exists
from facts.utils import *
_FactCheckedBy = 'Boomlive.In'

def readEachArticle(url,thumbnail,conn):
    soup = getUTF8Soup(url)
    if soup.find("div",class_ = "bg-404") is not None or soup.find('h1',class_="entry-title title is-size-2-touch is-2 article-title is-custom-title") is None:
        return
    else:
        title = soup.find('h1',class_="entry-title title is-size-2-touch is-2 article-title is-custom-title")
        authorname = soup.find('a',class_=lambda value: value and value.startswith("author-link")).text if soup.find('a',class_=lambda value: value and value.startswith("author-link")) is not None else 'BoomLive Staff'
        textcontent = ''
        if soup.find_all('div', class_='single-post-summary common-p') is not None and len(
                soup.find_all('div', class_='single-post-summary common-p')) > 0:
            summarytag =soup.find_all('div',class_='single-post-summary common-p')[0]
            textcontent = textcontent + summarytag.find('div').text
        storytag = soup.find_all('div',class_ = 'story')
        for tag in storytag:
            contents = tag.find_all('p')
            for content in contents:
                textcontent = textcontent + content.text.replace('\n','').replace('\t','')
        updateddate = soup.find('span',class_="convert-to-localtime").attrs.get('data-datestring')
        fact_verdict = ''
        article_claim = ''
        if soup.find('div',class_='claim-review-block') is not None:
            fact_verdict = soup.find('div',class_= 'claim-review-block').find_all('span',class_ = 'value')[-1].text
            article_claim = soup.find('div',class_= 'claim-review-block').find_all('span',class_ = 'value')[0].text.replace('\n','').replace('\t','')
        article = (unicodetoascii(url),
                   unicodetoascii(title.text),
                   thumbnail,
                   unicodetoascii(updateddate[0:10]),
                   unicodetoascii(article_claim),
                   unicodetoascii(textcontent),
                   unicodetoascii(authorname),
                   fact_verdict,
                   _FactCheckedBy
                   )
        insert_article(conn, article)

def boomlive_fetch(conn):
    i = 1
    while True:
        url = 'https://www.boomlive.in/fake-news/%d'% i
        print(url)
        soup = getUTF8Soup(url)
        if not soup.find('div',class_ = 'category-articles-list listing-article-list'):
            break
        else:
            for article in soup.find_all('div',class_='card-wrapper horizontal-card'):
                article_url = urllib.parse.urljoin(base_url(url), article.find('a')['href'])
                record_found = check_if_url_exists(conn, article_url)
                if not record_found:
                    if article.find('a', class_='fa-post-thumbnail') is not None:
                        thumbnail = imageurl_to_base64(
                            article.find('a', class_='fa-post-thumbnail').find('img').attrs.get('src'))
                    else:
                        thumbnail = imageurl_to_base64(
                            article.find('div', class_='herald-post-thumbnail herald-format-icon-middle').find('a').find('img').attrs.get('src'))
                    readEachArticle(article_url,thumbnail, conn)

        i = i + 1