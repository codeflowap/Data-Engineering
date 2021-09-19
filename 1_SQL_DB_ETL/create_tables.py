import psycopg2
from sql_queries import create_table_queries, drop_table_queries

def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """

    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=admin")
    conn.set_session(autocommit=True)
    cur = conn.cursor()