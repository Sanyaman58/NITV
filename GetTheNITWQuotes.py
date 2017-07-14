import os
#import date
from random import randint
from time import sleep
import tweepy


def isNotEmpty(s):
    return bool(s and s.strip())
#from NITWAllChars import Characters

def get_last_tweet(self):
    tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
    print(tweet.text)

''' TODO

- Check if last tweet is not too old, if so, either kill the app or delay tweet

- Gather all text files from 'yarn files', search for a Character name, colon, and space after it, and write the corresponding
dialogue that to a file. Ideally we should be left with one giant stripped down text file with JUST dialogue, nothing else.

Characters
colon = ': '
charactersNew = [x + colon for x in characters]

print(charactersNew)
line = open('D:\\Users\\Rob\\My Programming Folder\\Python Stuff\\Hugs\\Night In The Oh Shit This Is Ending.txt',
                          encoding="utf8").readlines()
print(random.choice(line))
print(line)
if line != 'hello'
print(line)

import random
with open('D:\\Users\\Rob\\My Programming Folder\\Python Stuff\\Hugs\\Night In The Oh Shit This Is Ending.txt', encoding="utf8") as f:
    lines = random.sample(f.readlines(),20)
    #print(lines)
    print(*lines, end="")
'''

randomNum = randint(0, 11000)
randomNumPlusRandom = randomNum + randint(30, 50)

def getRandomNum():
    #randomNum = randint(0, 11000)
    randomNumPlusRandom = randomNum + randint(3, 5)
    return randomNum

def getRandomNamPlusRandom():
#    randomNumPlusRandom = randomNum + randint(30, 50)
#    return randomNumPlusRandom
    return randomNumPlusRandom

def NumOfTweetsOfSetMade():
    return 0

def PrintTweet(myTweet):
    print(myTweet)

def Tweet(myTweet):
    consumer_key = ''
    consumer_secret = ''
    access_token = ''
    access_token_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    #print(line[0])
    print(myTweet)
    #print(targetLineQuotes)
    #print(randomNumPlusRandom - 1)
    #api.update_status(status=myTweet)
    NumOfTweetsOfSetMade =+ 1

# NumOfTweetsOfSetMade = 0

def getNITWQuotes():

    lines = []
    targetLineQuotes = []

    #randomNum = 6000
    #randomNumPlusRandom = 6030
    i = 0
    isError = False
    #print("---Making sure internet is connected...---")
    sleep(.5)
    while i == 0:
        #randomNum = randint(0, 11000)
        #randomNumPlusRandom = randomNum + randint(30, 50)
        for line in enumerate(open('D:\\Users\\Rob\\My Programming Folder\\Python Stuff\\Hugs\\New Files 7-9-2017\\NightDial.txt', encoding='utf-8')):
            lines.append(line)
            #print(lines)
            #list(range(9))
            targetlineNumbers = list(range(getRandomNum(), getRandomNamPlusRandom()))
        for line in lines:
            if line[0] == getRandomNamPlusRandom():
                print('loop')
                break
            if line[0] in targetlineNumbers:
                    #if str(line[0]) == "":
                try:
                    #myTweet = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                    myTweet = line[1].rstrip('\n')
                    #print(myTweet)
                    targetLineQuotes.append(line[1])
                except (tweepy.error.TweepError) as err:
                    print(err)
                    print("The tweet that didn't work was: " + myTweet)
                    isError = True
                    #sleep(5)
                    #pass
                if (isError):
                    isError = False
                    #print(isError)
                    pass
                if bool(line[0] >= (getRandomNamPlusRandom() - 1)):
                    #print("[This is the last quote in this set.]")
                    #print(targetLineQuotes)
                    #NumberList = [1,1,1,2,3,4,5,5,5,5,6,6]
                    #NumberList = remove_duplicates(NumberList)
                    #print(NumberList)
                    #print(getRandomNum())
                    return targetLineQuotes

                else:
                    ranTimer = randint(1600, 1900)
                    isError = False
                    #print("test")
                    #sleep(ranTimer)
                    #vvv debug sleep vvv
                    #sleep(.5)

#        sleep(.5)

#if line[randomNumPlusRandom].endswith(('.', '?')):
'''
NumberList = [1,1,1,2,3,4,5,5,5,5,6,6]
NumberList = remove_duplicates(NumberList)
print(NumberList)
'''
