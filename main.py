import sys
import time
import pandas as pd
import numpy as np
import re
from pathlib import Path


path = sys.argv[1]
fileExtension = sys.argv[2]
words = []


def GetArguments():
    if(len(sys.argv) != 3):
        sys.exit("Invalid Number of arguments!")


def PrintTime():
    print(f'Time: {((end-start)*1000):3.5f}ms')


start = time.time()
GetArguments()

for p in Path(path).rglob('**/*'+fileExtension):
    words.append(p.read_text().split())
    flat_list = list(np.concatenate(words).flat)
    new_list = [re.split(r"[^A-Za-z0-9]+", x) for x in flat_list]
    data = list(np.concatenate(new_list).flat)
    data = [x for x in data if len(x) >= 1]

values = pd.value_counts(np.array(data))

f = open("outputs/"+sys.argv[1]+".txt", "w")
f.write(values.to_string())
f.close()

end = time.time()
PrintTime()
