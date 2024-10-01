def get_valid_surrounding_dir(s_x_index, s_y_index, field, max_x, max_y):
    # Get valid directions (up, down, left, right) excluding any invalid cells like '.'
    return [
        [field[s_y_index + y][s_x_index + x], [s_x_index + x, s_y_index + y]]
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (Left, Right, Up, Down)
        if is_within_bounds(s_x_index + x, s_y_index + y, max_x, max_y)  # Bounds check
        and field[s_y_index + y][s_x_index + x] != '.'
    ]

def is_within_bounds(x, y, max_x, max_y):
    return 0 <= x < max_x and 0 <= y < max_y

def find_s(file):
    field = []
    max_x_index, max_y_index = 0, 0
    
    # Parse the file and find the initial position of 'S'
    for y, line in enumerate(open(file)):
        field.append(line.strip())  # Remove newline characters from the lines
        index = line.find('S')
        if index >= 0:
            s_x_index, s_y_index = index, y  # Save the position of 'S'
        if max_x_index == 0:
            max_x_index = len(line.strip())  # Set max_x_index based on line length
    max_y_index = len(field)  # Set max_y_index based on number of lines
    
    print (f"s_orig_x_index = {s_x_index}, s_orig_y_index = {s_y_index}")
    return s_x_index, s_y_index, max_x_index, max_y_index, field

def move(symbol, curr_x, curr_y, max_x_index, max_y_index, prev_x, prev_y):
    # Define movement vectors based on the symbol
    symbol_to_movement = {
        '|': [(0, 1), (0, -1)],  # Moves up or down
        '-': [(-1, 0), (1, 0)],  # Moves right or left
        'L': [(0, -1), (1, 0)],  # Up or right
        'J': [(0, -1), (-1, 0)], # Up or left
        '7': [(0, 1), (-1, 0)],  # Down or left
        'F': [(0, 1), (1, 0)],    # Down or right
    }

    # Try all possible moves for this pipe
    for move_x, move_y in symbol_to_movement[symbol]:
        new_x, new_y = curr_x + move_x, curr_y + move_y
        
        # Avoid moving back to the previous position
        if (new_x, new_y) == (prev_x, prev_y):
            continue

        if is_within_bounds(new_x, new_y, max_x_index, max_y_index):
            return new_x, new_y

    return None, None  # No valid moves


def main(file):
    s_orig_x_index, s_orig_y_index, max_x_index, max_y_index, field = find_s(file)
    paths = get_valid_surrounding_dir(s_orig_x_index, s_orig_y_index, field, max_x_index, max_y_index)
    s_x_index, s_y_index = s_orig_x_index, s_orig_y_index
    steps = 1
    for each_path in paths:
        curr_x_index, curr_y_index = each_path[1][0], each_path[1][1]
        symbol = field[curr_y_index][curr_x_index]
        while curr_x_index != None and curr_y_index != None:
            steps += 1
            prev_x_index, prev_y_index = curr_x_index, curr_y_index
            curr_x_index, curr_y_index = move(symbol, curr_x_index, curr_y_index, max_x_index, max_y_index, s_x_index, s_y_index)
            print(f"Symbol: {symbol}, New: ({curr_x_index},{curr_y_index}), Old:({s_x_index},{s_y_index})")
            symbol = field[curr_y_index][curr_x_index]
            s_x_index, s_y_index = prev_x_index, prev_y_index
            if symbol == "S":
                if steps % 2 == 0:
                    steps /= 2
                else:
                    steps = (steps + 1)/2
                print(f"Symbol is S and steps is {steps}")
                exit()

if __name__ == "__main__":
    main('day10input.txt')