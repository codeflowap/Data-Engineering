import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

def get_path():
    filepath = './data'
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        # get absolute path of all files
        for f in files :
            all_files.append(os.path.abspath(f))
    print(all_files)


def main():
    get_path()



if __name__ == "__main__":
    main()