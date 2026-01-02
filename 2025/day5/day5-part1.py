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
id_ranges, ids = [section.splitlines() for section in content.split('\n\n')]

if id_ranges and ids:
    res = 0
    for id in ids:
        id_num = int(id)
        for id_range in id_ranges:
            start, end = map(int, id_range.split('-'))
            if start <= id_num <= end:
                res += 1
                break
    print(res)