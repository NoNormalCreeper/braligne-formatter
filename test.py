from formatter import Formatter
from pathlib import Path

path = Path(__file__).parent / 'examples' / 'loadFiles.java'

with open(path, 'r') as f:
    print(Formatter(f.read()).format())