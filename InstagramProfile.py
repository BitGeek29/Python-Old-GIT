import requests
from lxml import html
import re
import sys

def main(username):

    url = "https://www.instagram/{}/?hl=en".format(username)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    data = tree.xpath('//meta[start-with(@name,"description")]/@content')

    if data:
        data = tree.xpath('//meta[start-with(@name,"description")]/@content')
        data = data[0].split(', ')
        follower = data[0][:-9].strip()
        following = data[1][:-9].strip()
        posts = re.findall(r'\d+[,]*', data[2])[0]
        name = re.findall(r'name":\w*[\s]+\w"', page.text)[7:-1]
        aboutinfo = re.findall(r'"description"':""())
