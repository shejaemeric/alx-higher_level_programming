#!/usr/bin/python3
"""sql module"""

from ast import keyword
import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    My_user = arg[1]
    My_pass = arg[2]
    dbname = arg[3]
    My_host = "localhost"
    key = arg[4]

    db = MySQLdb.connect(host=My_host,
                         user=My_user, passwd=My_pass,
                         db=dbname, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name like %s ORDER BY id", (key,))
    res = cur.fetchall()
    for item in res:
        print(item)
