#!/usr/bin/python3
"""
Script that displays all values in the states table:
-hbtn_0e_0_usa where name matches the argument (safe from MySQL injection)
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1], passwd=argv[2],
            db=argv[3])
    cursor = db.cursor()
    sql_query = "SELECT * FROM states WHERE name LIKE BINARY %s \
    ORDER BY id ASC"

    cursor.execute(sql_query, (argv[4] + '%',))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
