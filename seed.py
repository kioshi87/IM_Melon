"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server
import csv

os.system('dropdb melon')
os.system('createdb melon')

model.connect_to_db(server.app)
model.db.create_all()

# Load coupon data from CSV file, create coupon objects, load into db
with open('melons.tsv') as tsv_f:
    f = csv.reader(tsv_f, delimiter="\t")
    
    for line in f:
        # melon_name, melon_qty, melon_type, melon_season=line
        # melon=crud.create_melons(melon_name,melon_qty,melon_type,melon_season)
        print('*******************************')
        melon_name, melon_qty, melon_type, melon_season = line
        melon = crud.create_melons(melon_name, melon_qty, melon_type, melon_season)
    


# import os
# import csv
# import crud #note, not currently a file
# from server import app
# from model import Melon, Subscriber, db, connect_to_db

# with open('data/melons.tsv') as tsv_f:
# 	f = csv.reader(tsv_f, delimiter="\t")
# 	count = 1


# def cast_int(str):
#     try:
#         n = int(str)
#         return n
#     except (ValueError, TypeError):
#         return None


# def seed_csv_data(filename):


# # with open('data/melons.csv') as csv_file:
# with open(filename, 'r') as csv_file:

#     #file = csv.reader(csv_file)
#     file = csv.DictReader(csv_file)

#     for row in file:
#         for key in row:
#             if row[key] == '':
#                 row[key] = None
#     melons = Melon (
#         # subscriber_number = cast_int(row['subscriber_number']),
#         melon_name =  row['melon_name'],
#         melon_qty = cast_int(row['melon_qty']),
#         melon_type = row['melon_type'],
#         melon_season = row['melon_season']
#         )
#     db.session.add(melons)
#     db.session.commit()

#     print("################")
#     # melon = crud.create_melons(melon_name, melon_qty, melon_type, melon_season)
#     # print("################", melon)

# csv_file.close()


# def seed_users():
#     for i in range(9):
#         name = fake.name().split()
#         username = ''.join(name)
#         password = fake.password()
#         subscriber_number = fake.subscriber_number()
#         email = fake.email()
#         city = fake.city()
#         state = fake.state()
#         crud.create_user(username, password, email, city, state)


# if __name__ == '__main__':


#     # Call connect_to_db(app, echo=False) if your program output gets
#     # too annoying; this will tell SQLAlchemy not to print out every
#     # query it executes.

#     os.system('dropdb melon')
#     os.system('createdb melon')
#     connect_to_db(app)
#     db.create_all()
# seed_csv_data('data/melons.csv')
