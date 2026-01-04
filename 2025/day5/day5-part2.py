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

# a-b,c-d
# a<c
# a<b, c<d

# a<c<b<d 
# a<c<d<b b-a
# a<b<c<d 

# last_end = b, end = d

if id_ranges:
    sorted_ranges = sorted([tuple(map(int, id_range.split('-'))) for id_range in id_ranges])
    last_end = 0
    res = 0
    for id_range in sorted_ranges:
        start, end = id_range
        
        if end <= last_end:
            continue
        
        if last_end <= start:
            res += end - start
            if last_end < start:
                res += 1
        else:
            res += end - last_end
            
        last_end = end
        
    print(res)