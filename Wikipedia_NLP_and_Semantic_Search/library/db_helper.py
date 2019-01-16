import pandas as pd
import psycopg2 as pg2
from psycopg2.extras import RealDictCursor

def connect_to_db():
	con = pg2.connect(host='postgres', dbname='postgres', user='postgres')
	cur = con.cursor(cursor_factory=RealDictCursor)
	return con, cur

def query_to_dictionary(query, fetch_res=True):
	con, cur = connect_to_db()
	cur.execute(query)
	if fetch_res:
		results = cur.fetchall()
	else:
		results = None
	con.close()
	return results

def query_to_dataframe(query):
	return pd.DataFrame(query_to_dictionary(query))


def insert_category (id_no, name):
    '''
    grab category names and ids and push into the postsql db
    '''
    connect_to_db()
    con, cur = connect_to_db()
    query = '''
            BEGIN;
            INSERT INTO category VALUES ({}, '{}');
            COMMIT;
            '''.format(id_no, name)
    cur.execute(query)


def insert_page (id_no, title, text):
    '''
    grab page ids, titles, and text, and then push into the postsql db
    '''
    connect_to_db()
    con, cur = connect_to_db()
    query = '''
            BEGIN;
            INSERT INTO page VALUES ({}, '{}', '{}');
            COMMIT;
            '''.format(id_no, title, text)
    cur.execute(query)


def insert_category_page (page_id, category_cid):
    connect_to_db()
    con, cur = connect_to_db()
    query = '''
	    BEGIN;
	    INSERT INTO category_page VALUES ({}, {});
	    COMMIT;
	    '''.format(page_id, category_cid)
    cur.execute(query)



