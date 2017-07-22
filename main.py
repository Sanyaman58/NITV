#import functions
from random import randint
import tweepy
#QuoteList = functions.remove_adjacent(functions.getNITWQuotes())
#QuoteListLen = QuoteList.__len__()

with open('QuoteCounter.txt', 'r+') as QuoteCounter:
    data = QuoteCounter.read()
    data = data.strip().split("\n")
    QuoteNum = int(data[0])
    TotalNumOfQuotes = int(data[1])
        #WriteToQuotesFromData(data[0], data[1])
    i = True
    while i:
        if QuoteNum >= TotalNumOfQuotes - 1:
            QuoteCounter.close()
            #print("No more quotes! Getting more quotes...")
            import functions
            #QuoteList = functions.remove_adjacent(functions.getNITWQuotes())
            #QuoteListLen = QuoteList.__len__()
            #test = functions.Tweet(QuoteList[QuoteNum])
            #print(test)
            #print(QuoteList)
            #print(QuoteListLen)
            with open('QuoteCounter.txt', 'r+') as QuoteCounter:
                data[0] = data[0] + "\n"
                if "\n\n" in data[0]:
                    #print("Hello")
                    data[0] = data[0].replace("\n\n", "\n")
                    #data[0] = data[0] + "\n"
                data = QuoteCounter.readlines()
                RandomQuoteSet = randint(30, 50)
                data = [str(0), str(RandomQuoteSet)]
                QuoteNum = int(data[0])
                TotalNumOfQuotes = int(data[1])
                data[0] = str(data[0])
                data[0] = data[0] + "\n"
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    i = True
        if QuoteNum < TotalNumOfQuotes - 1:
            QuoteNum = int(QuoteNum)
            #put try/except tweepy tweet error handling in this file?
            #import functions
            #print(functions.Tweet(functions.QuoteList[QuoteNum]))
            #NewTweet = functions.Tweet(functions.QuoteList[QuoteNum])
            with open('CurrentSet.txt', 'r+') as CurrentSet:
                data = CurrentSet.read()
                data = data.strip().split("\n")
                NewTweet = data[QuoteNum]
                print(NewTweet)
                try:
                    consumer_key = ''
                    consumer_secret = ''
                    access_token = ''
                    access_token_secret = ''
                    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                    auth.set_access_token(access_token, access_token_secret)
                    api = tweepy.API(auth)
                    #api.update_status(status=myTweet)
                    #NumOfTweetsOfSetMade =+ 1
                    #return myTweet
                except tweepy.error.TweepError as err:
                    myTweet = "ERROR: TweepError"
                    #break
            #DateTime = GetTheNITWQuotes.DateTime()
            QuoteNum = int(QuoteNum)
            with open('QuoteCounter.txt', 'r+') as QuoteCounter:
                data[0] = data[0] + "\n"
                if "\n\n" in data[0]:
                    #print("Hello")
                    data[0] = data[0].replace("\n\n", "\n")
                    #data[0] = data[0] + "\n"
                data = QuoteCounter.readlines()
                data[0] = int(data[0]) + 1
                QuoteNum = data[0]
                data[0] = str(data[0]) + "\n"
                #print(data[0])
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    i = False
                    #sleep(5)
