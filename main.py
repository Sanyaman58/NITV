import functions

#@classmethod
#def setUpClass(cls):
#if QuoteList == []:
#QuoteList = functions.remove_adjacent(functions.getNITWQuotes())
#else:
#    pass

# make sure the file exists and contains valid data, if not, make it so
try:
    open('QuoteCounter.txt', 'r+', encoding='utf-8')
#except FileNotFoundError as FileNotFoundErr:
#    with open('QuoteCounter.txt', 'w', encoding='utf-8') as QuoteCounter:
#        data = [str(0) + '\n', str(data[1])]
#        QuoteCounter.writelines(data)
#        QuoteCounter.close()
except ValueError as ValErr:
    with open('QuoteCounter.txt', 'w', encoding='utf-8') as QuoteCounter:
        data = QuoteCounter.read()
        #print(data)
        data = data.strip().split("\n")
        QuoteNum = int(data[0])
        TotalNumOfQuotes = int(data[1])

with open('QuoteCounter.txt', 'r+', encoding='utf-8') as QuoteCounter:
    data = QuoteCounter.read()
    data = data.strip().split("\n")
    try:
        QuoteNum = int(data[0])
        TotalNumOfQuotes = int(data[1])
        #WriteToQuotesFromData(data[0], data[1])
    except (ValueError, IndexError) as ValErr:
        #data[0] = int(data[0]) + 1
        #data = [str(0) + '\n', str(data[1])]
        QuoteCounter.writelines(data)
        QuoteCounter.close()
        QuoteNum = int(data[0])
        TotalNumOfQuotes = int(data[1])
    i = True
    while i:
        if QuoteNum == 0:
        QuoteList = functions.remove_adjacent(functions.getNITWQuotes())
        if QuoteNum < TotalNumOfQuotes:
            QuoteNum = int(QuoteNum)
            #print(QuoteList)
            #put try/except tweepy tweet error handling in this file?
            #try:
            #(QuoteList[QuoteNum])
            NewTweet = functions.Tweet(QuoteList[QuoteNum])
            print(NewTweet)
            if NewTweet == "ERROR: TweepError":
                print("ERROR: TweepError")
                break
            #except:
                #IndexError
            #DateTime = GetTheNITWQuotes.DateTime()
            QuoteNum = int(QuoteNum)
            with open('QuoteCounter.txt', 'r+', encoding='utf-8') as QuoteCounter:
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
        else:
            QuoteCounter.close()
            # QuoteNum & TotalNumOfQuotes are equal in text file, get more quotes...
            print("No more quotes! Getting more quotes...")
            #global QuoteList
            QuoteList = functions.remove_adjacent(functions.getNITWQuotes())
            #QuoteListLen = QuoteList.__len__()
            #test = functions.Tweet(QuoteList[QuoteNum])
            #print(QuoteListLen)
            #print(test)
            #print(QuoteListLen)
            # These lines below are just for updating the text file counter
            with open('QuoteCounter.txt', 'r+', encoding='utf-8') as QuoteCounter:
                data[0] = data[0] + "\n"
                if "\n\n" in data[0]:
                    #print("Hello")
                    data[0] = data[0].replace("\n\n", "\n")
                    #data[0] = data[0] + "\n"
                data = QuoteCounter.readlines()
                data = [str(0), str(QuoteList.__len__())]
                QuoteNum = int(data[0])
                TotalNumOfQuotes = int(QuoteList.__len__())
                data[0] = str(data[0])
                data[0] = data[0] + "\n"
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    i = True

#if __name__ == "__main__":



