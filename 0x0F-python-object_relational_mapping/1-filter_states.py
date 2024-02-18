#!/usr/bin/python3
"""Get all states that start with N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    curr = db.cursor()
    curr.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = curr.fetchall()

    for row in rows:
        if row[1].startswith("N"):
            print(row)
    curr.close()
    db.close()
