
import csv
import os
from facts.altnews import altnews_fetch
from facts.boomlive import boomlive_fetch
filename = 'facts.csv'
file_exists = os.path.isfile(filename)
file_is_empty = os.stat(filename).st_size == 0
csv_file = open('facts.csv', 'r+', encoding='utf-8', newline='')
fieldnames = ['article_url', 'article_title', 'article_date', 'article_content', 'article_checked_by',
              'article_site_name']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
if not file_exists or file_is_empty:
    writer.writeheader()

#altnews_fetch(csv_file,writer)
boomlive_fetch(csv_file,writer)

