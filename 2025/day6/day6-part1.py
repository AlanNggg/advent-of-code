from pathlib import Path

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
rows = [row.split() for row in content.splitlines()]

res = 0
for ops in zip(*rows):
    operands, operator = map(int, ops[:-1]), ops[-1]
    
    if operator == '+':
        for operand in operands:
           res += operand
    elif operator == '*':
        product = 1
        for operand in operands:
            product *= operand
        res += product
print(res)
