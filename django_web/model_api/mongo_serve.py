from pymongo import MongoClient
import csv


MongoClient = MongoClient()
db = MongoClient['dating_dump']
collection = db['dating']

csvfile = open('C:\\Users\\Mario\\Documents\\dating data analysis\\dataset\\data_preproses.csv', 'r')
reader = csv.DictReader(csvfile)

header = ['iid', 'gender', 'partner', 'pid', 'match', 'samerace', 'age_o',
       'race_o', 'pf_o_sin', 'pf_o_int', 'pf_o_fun', 'pf_o_amb', 'pf_o_sha',
       'sinc_o', 'intel_o', 'fun_o', 'amb_o', 'shar_o', 'like_o', 'prob_o',
       'met_o', 'age', 'field_cd', 'race', 'imprace', 'imprelig', 'income',
       'date', 'go_out', 'career_c', 'sports', 'tvsports', 'exercise',
       'dining', 'museums', 'art', 'hiking', 'gaming', 'clubbing', 'reading',
       'tv', 'theater', 'movies', 'concerts', 'music', 'shopping', 'yoga']

for data in reader:
    row = {}
    for field in header:
        row[field] = data[field]
    collection.insert(row)

