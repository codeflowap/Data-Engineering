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
        print(file_path_list)



def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=csvtodb user=postgres password=admin")
    cur = conn.cursor()

    get_file_pathes()

    conn.close()


if __name__ == "__main__":
    main()