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

    try:
   # Explicitly set host to "localhost" and use default socket
        db = MySQLdb.connect(
            host="localhost", port=3306, user=us, passwd=ps, db=dbs, unix_socket="/var/run/mysqld/mysqld.sock"
        )
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY \
            '{}' ORDER BY id ASC".format(name))

        rows = cursor.fetchall()

        for row in rows:
            print(row)
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error connecting to MySQL:", e)
        sys.exit(1)
