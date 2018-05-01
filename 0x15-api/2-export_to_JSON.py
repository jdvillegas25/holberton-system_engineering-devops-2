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
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(sys.argv[1]))
    p = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(sys.argv[1]))

    userId = sys.argv[1]
    username = r.json()['username']
    print('this is the Id: {}'.format(userId))
    val = []
    for obj in p.json():
        dic = {}
        dic["task"] = obj['title']
        dic["completed"] = obj['completed']
        dic["username"] = username
        val.append(dic)
    new = {userId: val}
    with open('{}.json'.format(userId), 'w') as f:
        json.dump(new, f, ensure_ascii=False)
