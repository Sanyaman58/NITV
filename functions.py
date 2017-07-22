import os
#import date
from random import randint
from time import sleep, gmtime, strftime
import time
import tweepy
import datetime



def remove_adjacent(nums):
  a = nums[:1]
  for item in nums[1:]:
    if item != a[-1]:
      a.append(item)
  return a

def isNotEmpty(s):
    return bool(s and s.strip())
#from NITWAllChars import Characters

def get_last_tweet(self):
    tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
    print(tweet.text)

''' TODO
- Check if last tweet is not too old, if so, either kill the app or delay tweet
'''



def NumOfTweetsOfSetMade():
    return 0

def DateTime():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())
    #DateTime = datetime.datetime.now
    #return time.strftime('%H:%M:%S', time.localtime())

def getNITWQuotes():
    randomNum = randint(0, 11000)
    randomNumPlusRandom = randomNum + 500
    lines = []
    targetLineQuotes = []
    #randomNum = 6000
    #randomNumPlusRandom = 6030
    i = 0
    isError = False
    sleep(.5)
    while i == 0:
        for line in enumerate(open('/home/pi/NITWBotNew/NightDial.txt',)):
            lines.append(line)
            targetlineNumbers = list(range(randomNum, randomNumPlusRandom))
        for line in lines:
            if line[0] == randomNumPlusRandom:
                print('loop')
                break
            if line[0] in targetlineNumbers:
                if 0 < int(len(line[1])) <= 140:
                    #myTweet = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                    #myTweet = line[1].rstrip('\n')
                    thefile = open('CurrentSet.txt', 'w')
                    for item in targetLineQuotes:
                        thefile.write("%s\n" % item)
                    targetLineQuotes.append(line[1].rstrip('\n'))
                #this should be replaced with a valueError or something like that
                else:
                    pass
                #if (isError):
                #    isError = False
                #    pass
                if bool(line[0] >= (randomNumPlusRandom - 1)):
                    #Hello = targetLineQuotes
                    return targetLineQuotes
                #else:
                #    ranTimer = randint(1600, 1900)
                #    isError = False

QuoteList = remove_adjacent(getNITWQuotes())

#def QuoteList():
#    QuoteList = remove_adjacent(getNITWQuotes())
#    return QuoteList

#def GetQuoteList():
    #return GetQuoteList()