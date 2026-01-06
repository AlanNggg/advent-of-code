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

start = rows[0].index('S')
dp = {start: 1}

for index in range(1, len(rows)):
    row = rows[index]
    new_dp = {}
    
    for pos, count in dp.items():
        if pos < 0 or pos >= len(row):
            continue
        
        if row[pos] == '^':
            # Split left and right
            new_dp[pos - 1] = new_dp.get(pos - 1, 0) + count
            new_dp[pos + 1] = new_dp.get(pos + 1, 0) + count
        else:
            # Continue straight
            new_dp[pos] = new_dp.get(pos, 0) + count
    
    dp = new_dp

result = sum(dp.values())
print(result)  # 40