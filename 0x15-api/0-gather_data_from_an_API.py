#!/usr/bin/python3
""" grabbing users data using given api"""

import requests as req
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]
    user = req.get(url + "users/{}".format(user_id)).json()
    user_todos = req.get(url + "todos", params={"userId": user_id}).json()

    completed = [todos.get("title") for todos in user_todos
                if todos.get("completed")]
    print("Employee {} is done with tasks({}/{}):".format(
         user.get("name"), len(completed), len(user_todos)))
    [print("\t {}".format(c)) for c in completed]
