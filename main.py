import time

start = time.time()


numerOfWords = 0.0

with open(r'book.txt', 'r') as file:
    data = file.read()
    lines = data.split()
    numerOfWords += len(lines)

end = time.time()
print('{:5.3f}s'.format(end-start))
