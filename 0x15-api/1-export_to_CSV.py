#!/usr/bin/python3
'''
    comment
'''
import csv
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(sys.argv[1]))
    p = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(sys.argv[1]))
    nm = r.json()['username']
    text = []
    for ob in p.json():
        text.append("\"{}\",\"{}\",\"{}\",\"{}\""
                    .format(ob['userId'], nm,
                            ob['completed'], ob['title']))
    f = open('{}.csv'.format(sys.argv[1]), 'w')
    for line in text:
        f.write('{}\n'.format(line))
    f.close()
