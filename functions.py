import os
#import date
from random import randint
from time import sleep, gmtime, strftime
import time
import tweepy
import datetime

def FirstRun(num):
    if num == 0:
        return True
def isNotEmpty(s):
    return bool(s and s.strip())
#from NITWAllChars import Characters

def get_last_tweet(self):
    tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
    print(tweet.text)

''' TODO

- Check if last tweet is not too old, if so, either kill the app or delay tweet
'''

def remove_adjacent(nums):
  a = nums[:1]
  for item in nums[1:]:
    if item != a[-1]:
      a.append(item)
  return a

randomNum = randint(0, 11000)
#randomNum = 0
#randomNumPlusRandom = randomNum + 30
randomNumPlusRandom = randomNum + randint(30, 50)

def NumOfTweetsOfSetMade():
    return 0

def DateTime():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #DateTime = datetime.datetime.now
    #return time.strftime('%H:%M:%S', time.localtime())

def Tweet(myTweet):
    try:
        consumer_key = ''
        consumer_secret = ''
        access_token = ''
        access_token_secret = ''
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        #api.update_status(status=myTweet)
        NumOfTweetsOfSetMade =+ 1
        #return myTweet
        return myTweet
    except tweepy.error.TweepError as err:
        #myTweet = err
        return "ERROR: TweepError"

def getNITWQuotes():
    lines = []
    targetLineQuotes = []
    #randomNum = 6000
    #randomNumPlusRandom = 6030
    i = 0
    isError = False
    sleep(.5)
    while i == 0:
        for line in enumerate(open('D:\\Users\\Rob\\My Programming Folder\\Python Stuff\\Hugs\\New Files 7-9-2017\\NightDialTest.txt', encoding='utf-8')):
            lines.append(line)
            targetlineNumbers = list(range(randomNum, randomNumPlusRandom))
        for line in lines:
            if line[0] == randomNumPlusRandom:
                print('loop')
                break
            if line[0] in targetlineNumbers:
                #print(len(line[1].rstrip('\n')))
                #print(int(len(line[1])))
                if 0 < int(len(line[1])) <= 140:
                    #myTweet = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                    myTweet = line[1].rstrip('\n')
                    #global targetLineQuotes
                    targetLineQuotes.append(line[1].rstrip('\n'))
                #this should be replaced with a valueError or something like that
                else:
                    pass
                #except tweepy.error.TweepError as err:
                #    print(err)
                #    print("The tweet that didn't work was: " + myTweet)
                #if (isError):
                #    isError = False
                #    pass
                if bool(line[0] >= (randomNumPlusRandom - 1)):
                    #global JustTargetLineQuotes
                    #JustTargetLineQuotes = targetLineQuotes
                    #n Hello = targetLineQuotes
                    return targetLineQuotes
                #else:
                #    ranTimer = randint(1600, 1900)
                #    isError = False

#def getTargetLineQuotes():
#    return targetLineQuotes

#def run_once(f):
#    def wrapper(*args, **kwargs):
#        if not wrapper.has_run:
#             wrapper.has_run = True
#             return f(*args, **kwargs)
#    wrapper.has_run = False
#    return wrapper

#@run_once
#def web_service(QuoteList):
#    QuoteList = []
#    QuoteList = remove_adjacent(getNITWQuotes())
#    return QuoteList


#QuoteList = remove_adjacent(getNITWQuotes())