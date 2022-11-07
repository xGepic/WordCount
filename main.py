import time
import sys

startTimeInMS = time.time()*1000

# Check for Number of Arguments
if (len(sys.argv) != 3):
    sys.exit("Invalid Number of Arguments")

# Parse Arguments
path = sys.argv[1]
fileExtension = sys.argv[2]


endTimeInMS = time.time()*1000
print('{:3.5f}ms'.format(endTimeInMS-startTimeInMS))
