"""Script to seed database."""

import os
import json
import crud
from model import db, Melon, Subscriber, connect_to_db
import server
import csv

os.system('dropdb melon')
os.system('createdb melon')

connect_to_db(server.app)
db.create_all()

with open('melons.tsv') as tsv_f:
    f = csv.reader(tsv_f, delimiter="\t")
    
    for line in f:

        melon_name, melon_qty, melon_type, melon_season = line
        melon = crud.create_melons(melon_name, melon_qty, melon_type, melon_season)

