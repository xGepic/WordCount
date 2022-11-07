import time
import sys

start = time.time()

# Check for Number of Arguments
if (len(sys.argv) != 3):
    sys.exit("Invalid Number of Arguments")

# Parse Arguments
path = sys.argv[1]
fileExtension = sys.argv[2]


numberOfWords = 0.0
with open(r'testFolder/book.txt', 'r') as file:
    data = file.read()
    lines = data.split()
    numberOfWords += len(lines)

print(int(numberOfWords))
end = time.time()
print('{:5.3f}s'.format(end-start))
