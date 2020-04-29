import os
import csv

##
# edit by Songli Wang
# over Python 3.7
# April 29 2020
##


# global variables
WORKING_DIR = './'
TARGET_WEBSITE = "www.nytimes"
RAW_FILE = "SAMPLE.csv"
RESULT_FILE='SAMPLE_FILTERED.csv'


def search_csv(ID):
    with open(RAW_FILE, 'r', encoding='UTF-8') as rawFile:
        # lines = csv.DictReader(rawFile)
        lines = csv.reader(rawFile)
        writer = csv.writer(open(RESULT_FILE,'a+'))
        for i, row in enumerate(lines):
            if i == ID:
                print(row)
                writer.writerow(row)
                break

    rawFile.close()

def search(fname):
    f = open(fname, 'r', encoding='UTF-8')
    lines = f.readlines()
    flag = False
    for line in lines:
        if TARGET_WEBSITE in line:
            flag = True
            break
    if flag:
        print("hit:", fname)
        # this part is awkward and needs optimization
        a, b = fname.split('rumor', 1)
        c, d = b.split('.', 1)
        rumorID = int(c)
        print("rumorID is:", rumorID)
        search_csv(rumorID)


def walkDir(working_dir):
    # walk through all the files/directories
    for root, dirs, files in os.walk(working_dir):
        for name in files:
            name_split = os.path.splitext(name)
            f_name, f_type = name_split
            # only csv files are taken into consideration
            if f_type == '.csv':
                search(name)


walkDir(WORKING_DIR)
