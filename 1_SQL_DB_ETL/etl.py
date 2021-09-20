import os
import glob
import json
import psycopg2
import pandas as pd
from sql_queries import *

def process_song_file(cur,filepath):
    with open(filepath, 'r') as json_file:
        # load a json file (here returns a dict due to scalar values in json)
        single_json_file = json.load(json_file)

        # convert dict to dataframe
        df = pd.DataFrame.from_dict(single_json_file.items())

        # set columns of df to keys in dict
        df = df.T
        col = df.iloc[0]
        df.rename(columns=col, inplace=True)
        df.drop(index=0, inplace=True)

        # insert song
        song_data = (str(df['song_id'][1]), str(df['title'][1]), str(df['artist_id'][1]), int(df['year']), float(df['duration']))
        cur.execute(song_table_insert, song_data)

def process_log_file(cur, filepath):
    # open log file (two steps)

    # Step 1: Loading and parsing a JSON file with multiple JSON objects (the case of log files)
    data = []
    with open(filepath, 'r') as json_file:
        for line in json_file:
            data.append(json.loads(line))

    df =

def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        # get absolute path of all files
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=admin")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)

    conn.close()


if __name__ == "__main__":
    main()