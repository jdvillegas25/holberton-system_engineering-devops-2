#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                     format(sys.argv[1]))
    p = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                     format(sys.argv[1]))
    nm = r.json()['name']
    tr = 0
    fl = 0
    for obj in p.json():
        if obj['completed'] is False:
            fl = fl + 1
        elif obj['completed'] is True:
            tr = tr + 1
    tl = tr + fl
    ln = []
    for obj in p.json():
        if obj['completed'] is True:
            ln.append(obj['title'])
    print('Employee {} is done with tasks({}/{}):'.format(nm, tr, tl))
    for line in ln:
        print('  ' + line)
