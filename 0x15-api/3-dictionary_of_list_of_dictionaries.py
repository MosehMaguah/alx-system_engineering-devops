#!/usr/bin/python3
"""Exports todo list info of all employees to JSON format."""
import json
import requests as req

if __name__ == "__main__":

    url = "https://jsonplaceholder.typicode.com/"
    users = req.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in req.get(url + "todos",
                               params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
