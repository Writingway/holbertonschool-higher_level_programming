#!/usr/bin/python3
"""
Filter all states from the database hbtn_0e_0_usa
that start with N (upper N) and are safe from MySQL injections
"""
import MySQLdb
import sys


def connect_to_db():
    """
    Filter all states from the database hbtn_0e_0_usa
    that start with N (upper N) and are safe from MySQL injections
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    connect_to_db()
