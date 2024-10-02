import numpy as np
def open_input(file):
    with open(file,'r') as file:
        lines = file.readlines()
    arr = np.array([list(line.strip()) for line in lines])
    return (arr)

def find_empty_columns(arr):
    empty_cols = []
    for i in range(len(arr[0])):
        if '#' not in arr[:, i]:
            empty_cols.append(i)

    return (empty_cols)

def find_empty_rows(arr):
    empty_rows = []
    for i in range(len(arr)):
        if '#' not in arr[i, :]:
            empty_rows.append(i)

    return (empty_rows)

def expansion(arr, empty_rows, empty_columns):
    for i,row in enumerate(empty_rows):
        arr = np.insert(arr, row + i, ['.']*len(arr[0]), axis=0) # after adding a row, the indexes
        # print(f"Inserted a row at index {row}") #                  will change hence adding i
    for i,col in enumerate(empty_columns):
        arr = np.insert(arr, col+i, ['.']*len(arr), axis = 1)
    return (arr)

def find_distance(coord1, coord2):
    return (abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1]))

def find_sum(coordinates):
    res = 0
    for i, coord in enumerate(coordinates):
        for other_coord in coordinates[i + 1:]:
            res += find_distance(coord, other_coord)
    return (res)

# This approach takes too long and doesn't work well
# def expansion_part_2(arr, empty_rows, empty_columns):
#     for i,row in enumerate(empty_rows):
#         for j in range(9):
#             arr = np.insert(arr, row + i * 9 + j, ['.'] * len(arr[0]), axis=0) # after adding a row, the indexes
#         # print(f"Inserted a row at index {row}") #                  will change hence adding i
#     for i,col in enumerate(empty_columns):
#         for j in range(9):
#             arr = np.insert(arr, col + i * 9 + j, ['.'] * len(arr), axis=1)
#     return (arr)

def main_part_1(file):
    arr = open_input(file)
    # print(f"Input looks like this: \n{arr}")
    empty_cols = find_empty_columns(arr)
    empty_rows = find_empty_rows(arr)
    # print(f"Empty rows are {empty_rows} and empty columns are {empty_cols}")
    arr = expansion(arr, empty_rows, empty_cols)
    # find where all the galaxies are
    locations = np.where(arr == '#')
    coordinates = [list(x) for x in zip(locations[0], locations[1])]
    # print(f"The coordinates of the galaxies are {coordinates}")
    res = find_sum(coordinates)
    print(f"The total sum for part 1 is {res}")

def find_sum_version_2(coordinates, empty_rows, empty_columns,scale):
    res = 0
    for i, [r1,c1] in enumerate(coordinates):
        for [r2,c2] in coordinates[:i]:
            for r in range(min(r1, r2), max(r1,r2)):
                res += scale if r in empty_rows else 1
            for c in range(min(c1,c2), max(c1,c2)):
                res += scale if c in empty_columns else 1
    
    print(res)
            

def main_part_2(file):
    np.set_printoptions(threshold=np.inf, linewidth=np.inf)
    arr = open_input(file)
    # print(f"Input looks like this: \n{arr}")
    empty_cols = find_empty_columns(arr)
    empty_rows = find_empty_rows(arr)
    # find where all the galaxies are
    locations = np.where(arr == '#')
    coordinates = [list(x) for x in zip(locations[0], locations[1])]
    # print(f"The coordinates of the galaxies are {coordinates}")
    find_sum_version_2(coordinates, empty_rows, empty_cols, 1000000)

if __name__ == '__main__':
    main_part_1('Day11input.txt')
    main_part_2('Day11input.txt')