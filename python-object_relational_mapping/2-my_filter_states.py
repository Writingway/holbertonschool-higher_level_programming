#!/usr/bin/python3
""" Filter all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    states = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306, user=username,
        password=password,
        database=database,
    )

    cur = db.cursor()
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC".format(states)
    )

    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
