import os

import cfscrape,bs4
_FactCheckedBy = 'Alt News.In'

scraper = cfscrape.create_scraper()

def readEachArticle(url,writer):
    scraper = cfscrape.create_scraper()
    page = scraper.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')
    title = soup.find('h1',class_="entry-title h1")
    authorname = soup.find('a',class_="herald-author-name").text
    print(title.text)
    contents = soup.find('div',class_='entry-content herald-entry-content').find_all(['ul','li','p','em'],recursive=False)
    textcontent = ""
    for content in contents:
        textcontent = textcontent + content.text.replace('\n','')
    updateddate = soup.find('span',class_="updated").text
    print(updateddate)
    writer.writerow({'article_url':repr(url),
                     'article_title':repr(title.text),
                     'article_date':repr(updateddate),
                     'article_content':repr(textcontent),
                     'article_checked_by':repr(authorname),
                     'article_site_name':'\''+_FactCheckedBy+'\''})


def altnews_fetch(csv_file,writer):
    i = 1
    while True:
        url = 'https://www.altnews.in/page/%d/'% i

        scraper = cfscrape.create_scraper()
        page = scraper.get(url)
        soup = bs4.BeautifulSoup(page.text, 'html.parser')
        if not soup.find('article'):
            break
        else:
            for article in soup.find_all('article'):
                print(article.find('a')['href'])
                csv_file.seek(0, os.SEEK_SET)
                line_found = any(article.find('a')['href'] in line for line in csv_file)
                if not line_found:
                    csv_file.seek(0, os.SEEK_END)
                    readEachArticle(article.find('a')['href'], writer)
                #for line in csv_file:
                #    if article.find('a')['href'] in line:
                #        break
                #else:
                #    readEachArticle(article.find('a')['href'],writer)
        i = i + 1
