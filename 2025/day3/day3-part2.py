from pathlib import Path
import heapq

def read_file_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        # Remove newline characters
        lines = [line.strip() for line in lines]
        return lines
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except Exception as e:
        print(f"Error reading the file: {e}")
        return None
    

# Get the directory where the script is located
script_dir = Path(__file__).parent.absolute()
file_path = script_dir / "inputs.txt"
lines = read_file_lines(file_path)

if lines:
    joltage = 0
    for line in lines:
        result = []
        start = 0
        n = 12
        for remaining in range(n, 0, -1):
            end = len(line) - remaining + 1
            best_idx = max(range(start, end), key=lambda i: int(line[i]))
            result.append(line[best_idx])
            start = best_idx + 1
        joltage += int(''.join(result))
    print(joltage)