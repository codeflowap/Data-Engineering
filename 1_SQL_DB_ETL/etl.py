import os
import glob
import json
import psycopg2
import pandas as pd
from sql_queries import *
from datetime import datetime

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

    # Step 2: creating a single dataframe for each line and appending all
    df = pd.DataFrame()
    for i in range(len(data)):
        df_single_row = pd.DataFrame.from_dict(data[i].items())
        df_single_row = df_single_row.T
        col = df_single_row.iloc[0]
        df_single_row.rename(columns=col, inplace=True)
        df_single_row.drop(index=0, inplace=True)
        df = df.append(df_single_row, ignore_index=True)


    # INSERT data from dataframe to tables: 1- times 2- users

    # (I) INSERT data to "times" table
    # filter by NextSong action
    mask = 'NextSong'
    time_df = df[df['page'] == mask]

    # convert timestamp column to datetime
    time_df['datetime'] = time_df['ts'].map(lambda x: datetime.fromtimestamp(int(str(x)[:-3])))

    # extract the correct format of datetime
    time_df['datetime_str'] = time_df['datetime'].map(lambda x: str(x))
    time_df['datetime_str_year_red'] = time_df['datetime_str'].map(lambda x: x[2:])
    time_df['time'] = time_df['datetime_str_year_red'].map(lambda x: datetime.strptime(x, "%y-%m-%j %H:%M:%S"))

    # extract data for time_df
    time_df['hour'] = time_df['time'].map(lambda x: x.hour)
    time_df['day'] = time_df['time'].map(lambda x: x.day)
    time_df['date'] = time_df['time'].map(lambda x: x.date())
    time_df['week'] = time_df['date'].map(lambda x: x.isocalendar()[1])
    time_df['month'] = time_df['time'].map(lambda x: x.month)
    time_df['year'] = time_df['time'].map(lambda x: x.year)
    time_df['weekday'] = time_df['time'].map(lambda x: x.weekday())

    print('data inserted into dataframe')

    # insert time data records
    time_df = time_df[['time', 'hour', 'day', 'week', 'month', 'year', 'weekday']]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))




    # (I) INSERT data to "users" table
    user_df = pd.DataFrame()

    # fill empty cells in userId with 0 to resolve the error:
    # ValueError: invalid literal for int() with base 10: ''
    def fill_empty_userId(x):
        if x == '':
            return 0
        else:
            return int(x)

    user_df['user_id'] = df['userId'].apply(fill_empty_userId)
    user_df['first_name'] = df['firstName']
    user_df['last_name'] = df['lastName']
    user_df['level'] = df['level']
    user_df['gender'] = df['gender']
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, list(row))

def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        # get absolute path of all files
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        print(datafile)
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))

def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=postgres password=admin")
    cur = conn.cursor()

    # process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()