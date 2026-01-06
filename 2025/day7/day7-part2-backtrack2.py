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

def pre_order(index: int, pos: int) -> None:
    global res
    if index == len(rows):
        res += 1
        return
    
    row = rows[index]
    if pos < 0 or pos >= len(row):
        return  # out of bounds
    
    if row[pos] == '^':
        pre_order(index + 1, pos - 1)
        pre_order(index + 1, pos + 1)
    else:
        pre_order(index + 1, pos)

# Find starting position
start = rows[0].index('S')
res = 0
pre_order(1, start)
print(res)