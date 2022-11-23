import re
import pandas as pd
from pathlib import Path
import time
import sys
import numpy as np

start = time.time()

# Check for Number of Arguments
if (len(sys.argv) != 3):
    sys.exit("Invalid Number of Arguments")

# Parse Arguments
path = sys.argv[1]
fileExtension = sys.argv[2]

# Read all files in directory tree filtered by extension
for p in Path(path).glob('**/*'+fileExtension):
    words = re.sub(r"[-\[\]()\"#$%/@;:<>{}'*`+=~|.!?,\n]",
                   ' ', p.read_text()).split()
    lowerWords = [word.lower() for word in words]
    lowerWords = [s.strip() for s in lowerWords]
    values = pd.value_counts(np.array(lowerWords))

# Write to File
f = open("outputs/"+sys.argv[1]+".txt", "w")
f.write(values.to_string())
f.close()

end = time.time()
print(f'Time: {((end-start)*1000):3.5f}ms')
