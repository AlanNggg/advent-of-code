from pathlib import Path

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
        largest = 0
        banks = list(line)
        for i in range(len(banks)):
            for j in range(i + 1, len(banks)):
                res = int(f"{banks[i]}{banks[j]}")
                if res > largest:
                    largest = res
        joltage += largest
    print(joltage)