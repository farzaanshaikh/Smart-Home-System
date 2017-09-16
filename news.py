#https://newsapi.org/v1/articles?source=techcrunch&apiKey=773c852ac3b94e46869da137d176a37d
#https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=773c852ac3b94e46869da137d176a37d
import urllib2
import json
from tts import say
def local():
    response = urllib2.urlopen('https://newsapi.org/v1/articles?source=the-times-of-india&sortBy=latest&apiKey=1bb66d8bf0e94f449381d101ab3e4f9c')
    data = json.load(response)
    for x in range(0,5):
        a = data["articles"][x]["title"]
        a= str(a)
        say(a)

def world():
    response = urllib2.urlopen('https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=1bb66d8bf0e94f449381d101ab3e4f9c')
    data = json.load(response)
    for x in range(0,5):
        a = data["articles"][x]["title"]
        a= str(a)
        say(a)
