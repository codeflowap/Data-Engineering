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

def get_file_pathes():
    """ collect and join each file path in all subdirectories """

    # checking your current working directory
    print(os.getcwd())

    # Get your current folder and subfolder event data
    filepath = os.getcwd() + '/event_data'

    # Create a for loop to create a list of files and collect each filepath
    for root, dirs, files in os.walk(filepath):
        # join the file path and roots with the subdirectories using glob
        file_path_list = glob.glob(os.path.join(root, '*.csv'))
    print('get_file_pathes SUCCESS')
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
    print(full_data_rows_list[0])

def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=csvtodb user=postgres password=admin")
    cur = conn.cursor()

    file_path_list = get_file_pathes()
    get_full_data(file_path_list)


    conn.close()


if __name__ == "__main__":
    main()