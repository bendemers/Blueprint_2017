from pprint import pprint
import requests
import json
import random
from flask import Flask, url_for

def getTitleAndLink():
    r = requests.get(r'https://www.reddit.com/r/nottheonion/new.json?sort=new')
    data = r.json()

    title = random.choice(data['data']['children'])['data']['title']
    link = random.choice(data['data']['children'])['data']['url']
    data = (title, link)
    print(data)
    return data

def main():
    print(getTitleAndLink())

if __name__ == '__main__':
    main()