#!/usr/bin/python3
'''
    comment
'''
import collections
import csv
import json
import requests
import sys

if __name__ == "__main__":
    i = 1
    retval = {}
    while i <= 10:
        r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                         format(i))
        p = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.
            format(i))

        userId = i
        username = r.json()['username']
        val = []
        for obj in p.json():
            dic = {}
            dic["task"] = obj['title']
            dic["completed"] = obj['completed']
            dic["username"] = username
            val.append(dic)
        retval[i] = val
        i = i + 1
    with open('todo_all_employees.json', 'w') as f:
        json.dump(retval, f, ensure_ascii=False)
