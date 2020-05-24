import re

from facts.db import insert_article, check_if_url_exists
from facts.sync_to_cloud import push_to_firebase
from facts.utils import *
_FactCheckedById = 2

def readEachArticle(url,thumbnail,conn):
#def readEachArticle(url):
    soup = getUTF8Soup(url)
    if soup.find("div",class_ = "bg-404") is not None or soup.find('h1',class_="entry-title title is-size-2-touch is-2 article-title is-custom-title") is None:
        return
    elif soup.find('div',class_ = 'row short-factcheck-snippet'):
        pass
    else:
        title = soup.find('h1',class_="entry-title title is-size-2-touch is-2 article-title is-custom-title")
        authorname = soup.find('a',class_=lambda value: value and value.startswith("author-link")).text if soup.find('a',class_=lambda value: value and value.startswith("author-link")) is not None else 'BoomLive Staff'
        fact_verdict = ''
        article_claim = soup.find("meta", property="og:description")["content"]
        # tag = soup.find('div', class_='story')
        # for content in tag.findAll('p'):
        #     textcontent = textcontent + (" ".join(content.strings)).replace('\n', ' ').replace('\t', ' ') + " "
        #updateddate = soup.find('span',class_="convert-to-localtime").attrs.get('data-datestring')
        published_time = soup.find("meta", property="article:published_time")["content"][0:19]
        if soup.find('div', class_='claim-review-block') is not None:
            fact_verdict = soup.find('div', class_='claim-review-block').find_all('span', class_='value')[-1].text
            #article_claim = soup.find('div', class_='claim-review-block').find_all('span', class_='value')[0].text.replace('\n', ' ').replace('\t', '')
        # textcontent = textcontent + tag.text.replace('\n', ' ').replace('\t', ' ')
        string = soup.prettify()
        bodypattern = '(?:"articleBody" : ")(.*?)(?:")'
        bodymatch = re.search(bodypattern, string)
        if bodymatch:
            textcontent = " ".join(re.sub("<.*?>", "", bodymatch.group(1)).replace('\n', ' ').replace('\t', '').split())
        else:
            textcontent = ''
        verdictpattern = '(?:"alternateName" : ")(.*?)(?:")'
        verdictmatch = re.search(verdictpattern, string)
        if verdictmatch and fact_verdict == '':
            fact_verdict = verdictmatch.group(1)
        article = (unicodetoascii(url),
                   unicodetoascii(title.text),
                   thumbnail,
                   format_date(published_time, "%Y-%m-%dT%H:%M:%S"),
                   unicodetoascii(article_claim),
                   unicodetoascii(textcontent),
                   unicodetoascii(authorname),
                   fact_verdict,
                   'False' if any(x in title.text.lower() for x in (
                   'no', 'false', 'did not', 'didn\'t', 'fake', 'old ', 'old,', 'cannot', 'can\'t', 'photoshop', 'hoax',
                   'misreport', 'mis-report', 'misquote', 'mislead', 'fox', 'plagiarise', 'shared as', 'doesnt',
                   'doesn\'t', 'shared with','wrong')) == True and fact_verdict == '' else '',
                   _FactCheckedById
                   )
        #print(article)
        insert_article(conn, article)
        #push_to_firebase(conn, url)
#readEachArticle('https://www.boomlive.in/fake-news/photos-of-mould-on-leather-goods-in-malaysian-store-viral-as-india-8072')
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
                    thumbnail = imageurl_to_base64(
                            article.find('figure', class_='card-image').find('a').find('img').attrs.get('data-src'))
                    readEachArticle(article_url,thumbnail, conn)
                else:
                    return
        i = i + 1