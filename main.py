import time
import sys

startTimeInMS = time.time()*1000

# Check for Number of Arguments
if (len(sys.argv) != 3):
    sys.exit("Invalid Number of Arguments")

# Parse Arguments
path = sys.argv[1]
fileExtension = sys.argv[2]

testdictionary = {'jack': 4098, 'guido': 4127, 'irv': 49927}
for words in sorted(testdictionary, key=testdictionary.get, reverse=True):
    print(words, testdictionary[words])

endTimeInMS = time.time()*1000
print('{:3.5f}ms'.format(endTimeInMS-startTimeInMS))
