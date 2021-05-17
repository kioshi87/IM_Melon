import os
import csv
import crud #note, not currently a file
from server import app
from model import [insert class here], db, connect_to_db


def seed_csv_data(filename):
    with open(filename, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            for key in row:
                if row[key] == '':
                    row[key] = None
            melons = [Class name] (
            melon_name =  row['melon_name'],
            melon_quantity = row['melon_quantity'],
            melon_type = row['melon_type'],
            melon_season = row['melon_season']
            )

            db.session.add([insert seeded class name here])
            db.session.commit()
    csv_file.close()









if __name__ == '__main__':
    

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    
    os.system('dropdb [db name here]')
    os.system('createdb [db name here]')
    connect_to_db(app)
    db.create_all()
    seed_csv_data('melons.csv')