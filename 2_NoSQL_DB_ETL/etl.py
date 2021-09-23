# Import Python packages
import pandas as pd
import cassandra
import re
import os
import glob
import numpy as np
import json
import csv
import psycopg2

import sql_queries

def get_file_paths(data_directory = '/event_data'):
    """ collect and join each file path in all subdirectories """

    # checking your current working directory
    print(os.getcwd())

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + data_directory

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root, '*.csv'))
    print('SUCCESS: file paths collected')
    return file_path_list

def get_full_data(file_path_list):

    """ Processing the files to create the data file csv from rows of single
        csv files """

    # initiating an empty list of rows that will be generated from each file
    full_data_rows_list = []

    # for every filepath in the file path list
    for f in file_path_list:

        # reading csv file
        with open(f, 'r', encoding='utf8', newline='') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            next(csvreader) # skip the header

            # extracting each data row one by one and append it
            for line in csvreader:
                # print(line)
                full_data_rows_list.append(line)
    print('SUCCESS: data list created')
    return full_data_rows_list

def create_csv_from_list(data_list):

    """ create a csv file, set the header with desired column names, and then INSERT the
        data from a list to the csv """

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding='utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length', \
                         'level', 'location', 'sessionId', 'song', 'userId'])
        for row in data_list:
            if (row[0] == ''):
                continue
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))
    # check the number of rows in your csv file
    with open('event_datafile_new.csv', 'r', encoding = 'utf8') as f:
        print('SUCCESS: csv from data list created. Total lines = ', sum(1 for line in f))

def process_data(cur, conn, filepath='event_datafile_new.csv'):
    """
    stores a csv into postgres database
    """
    with open(filepath, 'r', encoding='utf8', newline='') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        next(csvreader)  # skip the header

        # extracting each data row one by one and store into database
        for row in csvreader:
            if (row[0] == ''):
                continue
            cur.execute(songtable_table_insert,(row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[12], row[13], row[16]))











def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=csvtodb user=postgres password=admin")
    cur = conn.cursor()

    # create a united csv from all csv in subdirectories
    data_directory = '/event_data'
    file_path_list = get_file_paths(data_directory='/event_data')
    full_data_rows_list = get_full_data(file_path_list)
    create_csv_from_list(full_data_rows_list)




    conn.close()


if __name__ == "__main__":
    main()