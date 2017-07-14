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


from time import sleep

with open('QuoteCounter.txt', encoding='utf-8') as QuoteCounter:
    data=QuoteCounter.read()
    #print(data)
    data = data.strip().split("\n")
    #data = data.strip().split("\:")
    QuoteNum = int(data[0])
    TotalNumOfQuotes = int(data[1])
    print(QuoteNum)
    print(TotalNumOfQuotes)
    i = True
    while i:
        if int(QuoteNum) < TotalNumOfQuotes:
            with open('QuoteCounter.txt', 'r+', encoding='utf-8') as QuoteCounter:
                data = QuoteCounter.readlines()
                #QuoteNum += int(QuoteNum)
                data[0] = str(QuoteNum + 1) + "\n"
                print(data[0])
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    #i = False
                    #sleep(5)
        else:
            QuoteCounter.close()
            #i = False
            QuoteList = GetTheNITWQuotes.getNITWQuotes()
            QuoteListLen = QuoteList.__len__()

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






