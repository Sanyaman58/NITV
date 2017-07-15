import functions
QuoteList = functions.getNITWQuotes()
QuoteListLen = QuoteList.__len__()

try:
    open('QuoteCounter.txt', 'r+', encoding='utf-8')
except FileNotFoundError as FileNotFoundErr:
    with open('QuoteCounter.txt', 'w', encoding='utf-8') as QuoteCounter:
        data = [str(0) + '\n', str(QuoteListLen)]
        QuoteCounter.writelines(data)
        QuoteCounter.close()
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
        data = [str(0) + '\n', str(QuoteListLen)]
        QuoteCounter.writelines(data)
        QuoteCounter.close()
        QuoteNum = int(data[0])
        TotalNumOfQuotes = int(data[1])
    i = True
    while i:
        if QuoteNum < TotalNumOfQuotes:
            QuoteNum = int(QuoteNum)
            #put try/except tweepy tweet error handling in this file?
            print(functions.Tweet(QuoteList[QuoteNum]))
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
                print(data[0])
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    i = False
                    #sleep(5)
        else:
            QuoteCounter.close()
            print("No more quotes! Getting more quotes...")
            QuoteList = functions.getNITWQuotes()
            QuoteListLen = QuoteList.__len__()
            test = functions.Tweet(QuoteList[QuoteNum])
            print(test)
            print(QuoteList)
            print(QuoteListLen)
            with open('QuoteCounter.txt', 'r+', encoding='utf-8') as QuoteCounter:
                data[0] = data[0] + "\n"
                if "\n\n" in data[0]:
                    #print("Hello")
                    data[0] = data[0].replace("\n\n", "\n")
                    #data[0] = data[0] + "\n"
                data = QuoteCounter.readlines()
                data = [str(0), str(QuoteListLen)]
                QuoteNum = int(data[0])
                TotalNumOfQuotes = int(data[1])
                data[0] = str(data[0])
                data[0] = data[0] + "\n"
                with open('QuoteCounter.txt', 'w') as file:
                    file.writelines(data)
                    QuoteCounter.close()
                    i = True