from facts.db import create_connection
from facts.sync_to_cloud import push_db_to_cloud
from facts.altnews import altnews_fetch
from facts.boomlive import boomlive_fetch
from facts.snopes import snopes_fetch
conn = create_connection()

altnews_fetch(conn)
#boomlive_fetch(conn)
#snopes_fetch(conn)
#csv_to_json(filename)
#push_db_to_cloud(conn)