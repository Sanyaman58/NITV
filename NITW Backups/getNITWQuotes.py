import os
#import date
from random import randint
from time import sleep
import tweepy


def isNotEmpty(s):
    return bool(s and s.strip())
#from NITWAllChars import Characters

def getNITWQuotes():
    return targetLineQuotes

def get_last_tweet(self):
    tweet = self.client.user_timeline(id = self.client_id, count = 1)[0]
    print(tweet.text)

''' TODO

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



import time
start_time = time.time()
lines = []
targetLineQuotes = []
randomNum = randint(0, 11000)
randomNumPlusRandom = randomNum + randint(30, 50)
#randomNum = 6000
#randomNumPlusRandom = 6030
i = 0
isError = False
#print("---Making sure internet is connected...---")
sleep(.5)
for line in enumerate(open('D:\\Users\\Rob\\My Programming Folder\\Python Stuff\\Hugs\\New Files 7-9-2017\\NightDial.txt', encoding='utf-8')):
     lines.append(line)

while i == 0:
    randomNum = randint(0, 11000)
    randomNumPlusRandom = randomNum + randint(3, 5)
    numOfQuotes = randomNumPlusRandom - randomNum
    #print(numOfQuotes)
        #print(lines)
        #list(range(9))
    for line in lines:
        if line[0] == randomNumPlusRandom:
            break
    for line in lines:
        #if line[0] == randomNumPlusRandom:
        #    print('loop')
        #    break
        if line[0] in targetlineNumbers:
                #if str(line[0]) == "":
            try:
                #myTweet = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
                myTweet = line[1].rstrip('\n')
                print(myTweet)
                consumer_key = 'CCxw7VxTNCf7tSwOVyKaCGHk4'
                consumer_secret = 'LOFKd0OzgMTz6dNGYegJGRVEFvi7rxoCTGULCYwFvk4XY0BhuY'
                access_token = '735158048654786560-GE9ZnEeh5ignDvyVpNjFyevz1ixznt0'
                access_token_secret = 'wPTrsIt9WYC5RHdSdfYFqc4dFaPPLCBSdM16wLmwGLhEK'
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
                #print(line[0])
                targetLineQuotes.append(line[1])
                print(line[0])
                print(randomNumPlusRandom - 1)
                # api.update_status(status=myTweet)
            except (tweepy.error.TweepError) as err:
                print("---Error Caught---")
                print("The tweet that didn't work was: " + myTweet)
                isError = True
                #sleep(5)
                #pass
            if (isError):
                #print(isError)
                pass
            if bool(line[0] >= (randomNumPlusRandom - 1)):
                print("[This is the last quote in this set.]")
                print("--- %s seconds ---" % (time.time() - start_time))
                i = 1
                #print(targetLineQuotes)
                #NumberList = [1,1,1,2,3,4,5,5,5,5,6,6]
                #NumberList = remove_duplicates(NumberList)
                #print(NumberList)
            else:
                ranTimer = randint(1600, 1900)
                isError = False
                #sleep(ranTimer)
                #vvv debug sleep vvv
                #sleep(.5)
            break

#        sleep(.5)

#if line[randomNumPlusRandom].endswith(('.', '?')):
'''
NumberList = [1,1,1,2,3,4,5,5,5,5,6,6]
NumberList = remove_duplicates(NumberList)
print(NumberList)
'''
