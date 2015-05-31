__author__ = 'poke19962008'

import urllib2
from bs4 import BeautifulSoup
import pync
import sys

url = sys.argv[1]

if url.split("/")[2] == "www.goal.com":
    print("Connection Successfull!!!")
else:
    print("Invalid URL!!!")
    quit()

init_home_score = "-1"
init_away_score = "-1"

html = urllib2.urlopen(url)
soup = BeautifulSoup(html.read())

home_tag = soup.find('div', class_="home")
home = home_tag.a.h2.text.encode("utf-8")

away_tag = soup.find('div', class_="away")
away = away_tag.a.h2.text.encode('utf-8')

header = home + " Vs. " + away

while True:
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html.read())

    home_score_tag = soup.find('div', class_="home-score")
    home_score = home_score_tag.text.encode('utf-8')

    away_score_tag = soup.find('div', class_="away-score")
    away_score = away_score_tag.text.encode('utf-8')

    if (init_away_score != away_score) or (init_home_score != home_score):
        content = home + ": " + home_score + "\n" + away + ": " + away_score
        pync.Notifier.notify(content, title=header, open=url, contentImage="logo.jpg")

        init_away_score = away_score
        init_home_score = home_score