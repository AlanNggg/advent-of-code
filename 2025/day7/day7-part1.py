from collections import defaultdict
from pathlib import Path
from typing import DefaultDict, List


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
    
# Get the directory where the script is located
script_dir = Path(__file__).parent.absolute()
file_path = script_dir / "inputs.txt"
content = read_file(file_path)
rows = [list(row) for row in content.splitlines()]

pos: set[int] = set()
res = 0
for row in rows:
  for i in range(len(row)):
    col = row[i]
    if col == 'S':
      pos.add(i)
    
    if col == '^':
      if i in pos:
        pos.remove(i)
        pos.add(i-1)
        pos.add(i+1)
        res += 1
print(res)