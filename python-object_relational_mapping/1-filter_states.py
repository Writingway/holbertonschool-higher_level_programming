#!/usr/bin/python3
"""
Filter all states from the database hbtn_0e_0_usa
that start with N (upper N) and are safe from MySQL injections
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Filter all states from the database hbtn_0e_0_usa
    that start with N (upper N) and are safe from MySQL injections
    """
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        password=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
