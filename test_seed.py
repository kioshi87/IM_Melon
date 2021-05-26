"""Script to seed database."""

import os
import json
import crud
import model
import server
import csv



def create_test_data():

    with open('melons.tsv') as tsv_f:
        f = csv.reader(tsv_f, delimiter="\t")
        
        for line in f:

            melon_name, melon_qty, melon_type, melon_season = line
            melon = crud.create_melons(melon_name, melon_qty, melon_type, melon_season)
    
if __name__ == "__main__":
    #from server import app
    #connect_to_db(app, "postgresql:///testdb")
    from flask import Flask
    app = Flask(__name__)
    os.system('dropdb testdb')
    os.system('createdb testdb')

    model.connect_to_db(app, "postgresql:///testdb")
    model.db.create_all()
    create_test_data()