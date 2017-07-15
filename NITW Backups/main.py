import time
start_time = time.time()
from getNITWQuotes import getNITWQuotes

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output
#NITWQuotes = getNITWQuotes
print()
remove_duplicates(getNITWQuotes())
print(getNITWQuotes())
#print(getNITWQuotes())
#NITWQuotes = getNITWQuotes
print([key for key, grp in itertools.groupby(getNITWQuotes())])
# print(numOfQuotes)
#print()
#remove_duplicates(getNITWQuotes())
#print(getNITWQuotes())
print("--- %s seconds ---" % (time.time() - start_time))

