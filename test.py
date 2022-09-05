from formatter import Formatter
from pathlib import Path

path = Path(__file__).parent / 'examples' / 'loadFiles.java'

path2 = Path(__file__).parent / 'examples' / 'findTranspose.java'

with open(path, 'r') as f:
    result = Formatter(f.read()).format()
    print(result)

with open(path, 'w') as f:
    f.write(result)