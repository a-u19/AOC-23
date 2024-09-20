def read_file(file_name):
    with open(file_name,"r") as data:
        return data.read().split("\n")

def get_next(list):
    if all(n == 0 for n in list):
        return 0
    
    diff = [list[i + 1] - list[i] for i in range(len(list) - 1)]
    new_diff = get_next(diff)
    return list[-1] + new_diff

def get_prev(list):
    if all(n == 0 for n in list):
        return 0
    
    diff = [list[i + 1] - list[i] for i in range(len(list) - 1)]
    new_diff = get_prev(diff)
    return list[0] - new_diff

def parse_line(line):
    return [int(v) for v in line.split(" ")]

def main(file_name):
    res = 0
    data = read_file(file_name)
    for line in data:
        nums = parse_line(line)
        res += get_prev(nums)
    print(res)
        
if __name__ == "__main__":
    main("Day9P1.txt")