import time
start_time = time.time()
from GetTheNITWQuotes import getNITWQuotes
from GetTheNITWQuotes import getRandomNamPlusRandom

# remember to replace tjis with a "remove duplicates next to each other function

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
print(getRandomNamPlusRandom())
print()
#print("test")
remove_duplicates(getNITWQuotes())
print(getNITWQuotes())
print("--- %s seconds ---" % (time.time() - start_time))

