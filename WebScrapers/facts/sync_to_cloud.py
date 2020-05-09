from datetime import datetime
import json
import requests
API_MAXDATE = "http://localhost//getmaxdate.php"
API_ENDPOINT = "http://localhost//pusharticle.php"
def push_db_to_cloud(conn):
    req = requests.get(API_MAXDATE)
    result = req.json()
    maxdate = result['MaxArticleDate'] if result['MaxArticleDate'] != '' else '1900-01-01 00:00:00'
    cur = conn.cursor()
    cur.execute('SELECT * FROM articles where article_date >= ?', maxdate)
    rows = cur.fetchall()
    for row in rows:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        row_article_url = row[1]
        row_article_title = row[2]
        row_article_thumbnail = row[3]
        row_article_date = row[4]
        row_article_subtitle = row[5]
        row_article_content = row[6]
        row_article_checked_by = row[7]
        row_article_verdict = row[8]
        row_article_alt_verdict = row[9]
        row_article_site_id = row[10]
        row_article_sync_date = now
        data = {'push_article_url' : row_article_url,
                'push_article_title' : row_article_title,
                'push_article_thumbnail' : row_article_thumbnail,
                'push_article_date' : row_article_date,
                'push_article_subtitle' : row_article_subtitle,
                'push_article_content' : row_article_content,
                'push_article_checked_by' : row_article_checked_by,
                'push_article_verdict' : row_article_verdict,
                'push_article_alt_verdict' : row_article_alt_verdict,
                'push_article_site_id' : row_article_site_id,
                'push_article_sync_date' : row_article_sync_date
                }
        print('pushing '+str(row_article_url))
        r = requests.post(url=API_ENDPOINT, data=data)
        print(r)
        conn.execute("""UPDATE articles SET article_sync_date = '?' WHERE article_url = '?'""", (now, row_article_url,))

