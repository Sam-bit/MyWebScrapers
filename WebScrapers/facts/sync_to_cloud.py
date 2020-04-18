from datetime import datetime

import requests
API_ENDPOINT = "http://http://nonstopstudioz.epizy.com//push.php"
def push_db_to_cloud(conn):
    cur = conn.cursor()
    cur.execute('SELECT * FROM articles where sync_date is null')
    rows = cur.fetchall()
    for row in rows:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        row_id = row[0]
        row_article_url = row[1]
        row_article_title = row[2]
        row_article_date = row[3]
        row_article_content = row[4]
        row_article_checked_by = row[5]
        row_article_site_name = row[6]
        row_sync_date = now
        data = {'push_id': row_id,
                'push_article_url' : row_article_url,
                'push_article_title' : row_article_title,
                'push_article_date' : row_article_date,
                'push_article_content' : row_article_content,
                'push_article_checked_by' : row_article_checked_by,
                'push_article_site_name' : row_article_site_name,
                'push_sync_date' : now
                }
        print('pushing '+str(row_id))
        r = requests.post(url=API_ENDPOINT, data=data)
        print(r)
        conn.execute("""UPDATE articles SET sync_date = '?' WHERE id = '?'""", (now, row_id,))

