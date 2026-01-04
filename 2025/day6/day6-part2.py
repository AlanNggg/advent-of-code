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
rows = [row for row in content.splitlines()]
operands = rows[:-1]
operators = rows[-1]

res = 0
true_ops: dict[int, str] = {}
for row in rows:
    rtl_row = row[::-1]

    for i in range(len(rtl_row)):
        char = rtl_row[i]
        
        if i not in true_ops:
            true_ops[i] = ''

        if char != ' ':
            true_ops[i] += char

nums: list[int] = []

for op in true_ops.values():
    if '+' in op or '*' in op:
        newnum, operator = int(op[:-1]), op[-1]
        
        if operator == '+':
            res += newnum
            for num in nums:
                res += num
        elif operator == '*':
            product = newnum
            for num in nums:
                product *= num
            res += product
        nums = []
    elif op != '':
        nums.append(int(op))
                
                
print(res)
