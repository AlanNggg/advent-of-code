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

pos: list[int] = []
index = 0
row = rows[index]
for i in range(len(row)):
  if row[i] == 'S':
    pos.append(i)


res = 0
def pre_order(index: int, pos: List[int]) -> None:
  global res
  if index == len(rows):
    # print(pos)
    res += 1
    return

  row = rows[index]
  last_pos = pos[-1]
  for i in range(len(row)):
    if row[i] == '^' and i == last_pos:
      pos.append(i-1)
      pre_order(index + 1, pos)
      pos.pop()
      pos.append(i+1)
      pre_order(index + 1, pos)
      pos.pop()
    elif i == last_pos:
      pos.append(i)
      pre_order(index + 1, pos)
      pos.pop()

pre_order(1, pos)
print(res)