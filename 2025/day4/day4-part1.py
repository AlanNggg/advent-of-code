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
    res = 0
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '@':
                t = (row - 1, col)
                b = (row + 1, col)
                l = (row, col - 1)
                r = (row, col + 1)
                tl = (row - 1, col - 1)
                tr = (row - 1, col + 1)
                bl = (row + 1, col - 1)
                br = (row + 1, col + 1)

                if row == 0 and col > 0 and col < len(lines[row]) - 1:
                    directions = [b, l, r, bl, br]
                elif row == len(lines) - 1 and col > 0 and col < len(lines[row]) - 1:
                    directions = [t, l, r, tl, tr]
                elif col == 0 and row > 0 and row < len(lines) - 1:
                    directions = [t, b, r, tr, br]
                elif col == len(lines[row]) - 1 and row > 0 and row < len(lines) - 1:
                    directions = [t, b, l, tl, bl]
                elif row > 0 and row < len(lines) - 1 and col > 0 and col < len(lines[row]) - 1:
                    directions = [t, b, l, r, tl, tr, bl, br]
                else:
                    res += 1
                    continue

                n_neighbors = 0    
                for dr in directions:
                    if lines[dr[0]][dr[1]] == '@':
                        n_neighbors += 1
                if n_neighbors < 4:
                    res += 1

    print(res)

