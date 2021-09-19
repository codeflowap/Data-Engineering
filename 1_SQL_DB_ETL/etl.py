import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *

filepath = './data'
for root, dirs, files in os.walk(filepath):
    # join the file path and roots with the subdirectories using glob
    file_path_list = glob.glob(os.path.join(root, '*'))
    print(file_path_list)