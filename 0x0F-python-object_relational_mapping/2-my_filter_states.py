#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":

    username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]


    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cursor = db.cursor()


    cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY states.id", (state_name,))


    results = cursor.fetchall()
    for row in results:
        print(row)


    cursor.close()
    db.close()

