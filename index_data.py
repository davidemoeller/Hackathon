import pandas as pd
from elasticsearch import Elasticsearch
import json
import re
import argparse as arg
import glob
import pdb
import os

def build_database(index_file, name):
    
    print name
    dict = {}
    es = Elasticsearch()
    #pdb.set_trace()
    for i in range(0, len(index_file)):
        for j in range(0, len(index_file.columns)):
           # print index_file.columns[j]
            if index_file.iloc[i,j] is not None:
                dict[index_file.columns[j]] = index_file.iloc[i,j]
        es.index(index='columbusdata', doc_type=name, body=dict)
        dict = {}

def main():
    
    i = 0
    for file in glob.glob('csv_files/*.csv'):
        for loc,ch in enumerate(file):
            if ch == '.':
                n = file[10:loc]
        index_file = pd.read_csv(file)
        build_database(index_file, n)
        
        i += 1
    print("Done!")

if __name__ == "__main__":
    main()
