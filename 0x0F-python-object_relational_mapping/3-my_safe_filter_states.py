#!/usr/bin/python3
"""
 A script that takes in arguments and displays all values
 in the states table of hbtn_0e_0_usa where name matches the argument.
 But this time, write one that is safe from MySQL injections!
 """

import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    instruction = "SELECT * FROM states WHERE name = {};".format(sys.argv[4])
    cursor.execute(instruction)
    data = cursor.fetchall()

    for state in data:
        print(state)
