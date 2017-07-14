import GetTheNITWQuotes

'''

You are so close~!!! 'w'~~~ Don't give up! You KNOW this works!!!!!!!
uh Thx My Comptueroeruiejrioemjfio


a log file that lists two numbers: what variable in the array we are on and the total number of variables in that array

open(arrayLogFile.txt).read()
  QuoteNum: 0
TotalNumOfQuotes: 38
    if (data.split(:)


'''

try:
    with open('QuoteCounter.txt', 'r+', encoding='utf-8'):
except FileNotFoundError as FileNotFoundErr:
    with open('QuoteCounter.txt', 'w', encoding='utf-8') as QuoteCounter:
        data = QuoteCounter.read()
        #print(data)
        data = data.strip().split("\n")
        #data = data.strip().split("\:")
        QuoteNum = int(data[0])
        TotalNumOfQuotes = int(data[1])
except ValueError as ValErr:
    #data[0] = int(data[0]) + 1
    data = [str(0) + '\n', str(QuoteListLen)]
    QuoteCounter.writelines(data)
    QuoteCounter.close()
    QuoteNum = int(data[0])
    TotalNumOfQuotes = int(data[1])
    #except FileNotFoundError as FileNotFoundErr:
    
from time import sleep

with open('QuoteCounter.txt', encoding='utf-8') as QuoteCounter:
    data=QuoteCounter.read()
    #print(data)
    data = data.strip().split("\n")
    #data = data.strip().split("\:")
    QuoteNum = int(data[0])
    TotalNumOfQuotes = int(data[1])
    #print(QuoteNum)
    #print(TotalNumOfQuotes)
    #a = True
    #while a:
        #data[0] = QuoteNum
    i = True
    while i:
        if int(QuoteNum) < TotalNumOfQuotes:
            GetTheNITWQuotes.PrintTweet(QuoteList[QuoteNum - 1])(QuoteList[QuoteNum - 1])
            with open('QuoteCounter.txt', 'r+', encoding='utf-8') as QuoteCounter:
                data[0] = data[0] + "\n"
                if "\n\n" in data[0]:
                    #print("Hello")
                    data[0] = data[0].replace("\n\n", "\n")
                    #data[0] = data[0] + "\n"
                data = QuoteCounter.readlines()
                #QuoteNum += int(QuoteNum)
                #print(str(QuoteNum + 1))
                data[0] = int(data[0]) + 1
                QuoteNum = data[0]
                data[0] = str(data[0])
                data[0] = data[0] + "\n"
                print(data[0])
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    i = False
                    #sleep(5)
        else:
            QuoteCounter.close()
            QuoteNum = 1
            #a = False
            i = False
            print("No more quotes! Getting more quotes...")
            QuoteList = GetTheNITWQuotes.getNITWQuotes()
            QuoteListLen = QuoteList.__len__()
            GetTheNITWQuotes.Tweet(QuoteList[QuoteNum - 1])
            print(QuoteList)
            print(QuoteListLen)
            with open('QuoteCounter.txt', 'r+', encoding='utf-8') as QuoteCounter:
                data[0] = data[0] + "\n"
                if "\n\n" in data[0]:
                    #print("Hello")
                    data[0] = data[0].replace("\n\n", "\n")
                    #data[0] = data[0] + "\n"
                data = QuoteCounter.readlines()
                #QuoteNum += int(QuoteNum)
                #print(str(QuoteNum + 1))
                data = [str(0), str(QuoteListLen)]
                QuoteNum = data[0]
                data[0] = str(data[0])
                data[0] = data[0] + "\n"
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    i = True

'''
                #QuoteCounter.seek(QuoteNum)
                QuoteNum = str(QuoteNum + 1)
                #QuoteCounter.write(QuoteNum)
                #QuoteCounter.truncate()
                #QuoteCounter.close()
                data=QuoteCounter.read()
                #print(data)
                data = data.strip().split("\n")
                QuoteNum = data[0]
                TotalNumOfQuotes = data[1]
                print(QuoteNum)
                print(TotalNumOfQuotes)
                sleep(5)
'''






