#!/usr/bin/python3
"""sql module"""

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
    cur.execute("SELECT name FROM cities \
            WHERE state_id = (SELECT id FROM states WHERE \
            name = %s)", (key,))
    res = cur.fetchall()
    st = []
    for item in res:
        st.append(item[0])

    print(', '.join(st))
    cur.close()
    db.close()
