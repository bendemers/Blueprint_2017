from pprint import pprint
import requests
import json
import random

def getTitleAndLink():
    r = requests.get(r'https://www.reddit.com/r/nottheonion/new.json?sort=new')
    data = r.json()
    return random.choice(data['data']['children'])['data']['title']

def main():
    print(getTitleAndLink())

if __name__ == '__main__':
    main()