import os
import glob
import json
import psycopg2
import pandas as pd
from sql_queries import *

def get_files_in_subdirectoris(folder_path = './data'):
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        files = glob.glob(os.path.join(root,'*.json'))
        # get absolute path of all files
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files

def process_song_file(cur,filepath):
    with open(filepath, 'r') as json_file:
        # load a json file (here returns a dict due to scalar values in json)
        single_json_file = json.load(json_file)




def main():
    get_path()



if __name__ == "__main__":
    main()