#!/usr/bin/python3
"""
Script that displays all values in the states table:
-hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys

if __name__ == "__main__":

    us = sys.argv[1]
    ps = sys.argv[2]
    dbs = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(
         host="localhost", port=3306 user=us, passwd=ps, db=dbs)
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY \
    '{}' ORDER BY id ASC".format(name))

    rows = cursor.fetchall()

    for row in rows:
        print(row)
