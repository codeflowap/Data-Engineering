import psycopg2
from sql_queries import songplay_table_create

def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """

    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=postgres password=admin")
    conn.set_session(autocommit=True)
    cur = conn.cursor()

    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS csvtodb")
    cur.execute("CREATE DATABASE csvtodb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()

    # connect to csvtodb database
    conn = psycopg2.connect("host=127.0.0.1 dbname=csvtodb user=postgres password=admin")
    cur = conn.cursor()

    return cur, conn


def main():
    """
    - Drops (if exists) and Creates the csvtodb database.

    - Establishes connection with the csvtodb database and gets
    cursor to it.

    - Drops all the tables.

    - Creates all tables needed.

    - Finally, closes the connection.
    """
    cur, conn = create_database()

    # drop_tables(cur, conn)
    # create_tables(cur, conn)

    conn.close()

if __name__ == "__main__":
    main()