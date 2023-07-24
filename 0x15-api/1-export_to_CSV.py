#!/usr/bin/python3
""" exports the data in the CSV format. """

import csv
import requests as req
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = req.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = req.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
             [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
