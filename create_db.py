"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import os
import inspect
import sqlite3
from datetime import datetime
from faker import Faker

fake = Faker("en_CA")

def main():
    global db_path
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    create_people_table()
    populate_people_table()

def create_people_table():
    """Creates the people table in the database"""
# Open a connection to the database.
    con = sqlite3.connect(db_path)
# Get a Cursor object that can be used to run SQL queries on the database.
    cur = con.cursor()
# Define an SQL query that creates a table named 'people'.
# Each row in this table will hold information about a specific person.
    create_ppl_tbl_query = """
     CREATE TABLE IF NOT EXISTS people
        (
            id          INTEGER PRIMARY KEY,
            name        TEXT NOT NULL,
            email       TEXT NOT NULL,
            address     TEXT NOT NULL,
            city        TEXT NOT NULL,
            province    TEXT NOT NULL,
            bio         TEXT,
            age         INTEGER,
            created_at  DATETIME NOT NULL,
            updated_at  DATETIME NOT NULL
        );
    """
# Execute the SQL query to create the 'people' table.
# Database operations like this are called transactions.
    cur.execute(create_ppl_tbl_query)
# Commit (save) pending transactions to the database.
# Transactions must be committed to be persistent.
    con.commit()

# Close the database connection.
# Pending transactions are not implicitly committed, so any
# pending transactions that have not been committed will be lost.
    con.close()


def populate_people_table():
    """Populates the people table with 200 fake people"""
    # TODO: Create function body
    conn = sqlite3.connect(db_path)

    cur = conn.cursor()

    add_person_query = """
        INSERT INFO people
        (
            name,
            email,
            address,
            city,
            province,
            bio,
            age,
            created_at,
            updated_at
        
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    for _ in range(200):
        person_data = (
            fake.name(),
            fake.email(),
            fake.street_address(),
            fake.city(),
            fake.provience(),
            fake.sentence(),
            fake.random_int(1, 100),
            datetime.now(),
            datetime.now()
        )
        cur.execute(add_person_query, person_data)

    conn.commit()
    conn.close()
    
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides

    Returns:
        str: Full path of the directory in which this script resides
    """
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()