import os
import urllib

import cfscrape,bs4
_FactCheckedBy = 'Boomlive.In'
def base_url(url, with_path=False):
    parsed = urllib.parse.urlparse(url)
    path = '/'.join(parsed.path.split('/')[:-1]) if with_path else ''
    parsed = parsed._replace(path=path)
    parsed = parsed._replace(params='')
    parsed = parsed._replace(query='')
    parsed = parsed._replace(fragment='')
    return parsed.geturl()
scraper = cfscrape.create_scraper()

def readEachArticle(url,writer=None):
    scraper = cfscrape.create_scraper()
    page = scraper.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    title = soup.find('h1',class_="entry-title title is-size-2-touch is-2 article-title is-custom-title")
    print(title.text)
    authorname = soup.find('a',class_=lambda value: value and value.startswith("author-link")).text
    print(authorname)
    textcontent = ''
    textcontent = textcontent + soup.find('div',class_='single-post-summary common-p').find('div').text
    contents = soup.find('div',class_='content details-content-story').find('div',class_ = 'story').find_all('p')
    for content in contents:
        textcontent = textcontent + content.text.replace('\n','')
    updateddate = soup.find('span',class_="convert-to-localtime").attrs.get('data-datestring')
    print(updateddate)
    print(textcontent)
readEachArticle('https://www.boomlive.in/fake-news/up-police-debunk-false-communal-claim-about-meat-thrown-at-a-temple-7180')
    #writer.writerow({'article_url':repr(url),
    #                 'article_title':repr(title.text),
    #                 'article_date':repr(updateddate),
    #                 'article_content':repr(textcontent),
    #                 'article_checked_by':repr(authorname),
    #                 'article_site_name':'\''+_FactCheckedBy+'\''})


#def boomlive_fetch(csv_file,writer):
#    i = 1
#    while True:
#        url = 'https://www.boomlive.in/fake-news/%d'% i
#
#        scraper = cfscrape.create_scraper()
#        page = scraper.get(url)
#        soup = bs4.BeautifulSoup(page.text, 'html.parser')
#        if not soup.find('div',class_ = 'category-articles-list listing-article-list'):
#            break
#        else:
#            for article in soup.find_all('div',class_='card-wrapper horizontal-card'):
#                article_url = urllib.parse.urljoin(base_url(url), article.find('a')['href'])
#                csv_file.seek(0, os.SEEK_SET)
#                line_found = any(article_url in line for line in csv_file)
#                if not line_found:
#                    csv_file.seek(0, os.SEEK_END)
#                    readEachArticle(article_url, writer)
#        i = i + 1
#