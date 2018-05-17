#!/usr/bin/python3
'''
    comment
'''
import requests
import sys

if __name__ == '__main__':

    link = ''
    p = {}
    ret = 0
    try:
        link = 'https://www.reddit.com/r/{}/.json'.format(sys.argv[1])
    except IndexError:
        print(0)
    p = requests.get(link, headers={'User-agent': 'x'})
    try:
        ret = p['data']['children'][0]['data']['subreddit_subscribers']
        print(ret)
    except KeyError:
        print(0)
