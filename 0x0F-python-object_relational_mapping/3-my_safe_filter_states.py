#!/usr/bin/python3
"""Get all states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    curr = db.cursor()
    curr.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC",
                 (argv[4], ))
    rows = curr.fetchall()

    for row in rows:
        print(row)
    curr.close()
    db.close()
