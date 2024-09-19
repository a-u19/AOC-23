def OpenFile(file):
    with open(file,"r") as file:
        data = file.readlines()
    return data

def main(input):
    data = OpenFile(input)
    times = ""
    dists = ""
    ans = 1
    for line in data:
        line = line.split()
        line.pop(0)
        for race in line:
            times += race
        times += " "
    times,dists = times.split()
    times,dists = int(times),int(dists)
    # print(dists)
    winning_ways = 0
    record_dist = dists
    for buttonPressTime in range(times):
        curr_dist = (times - buttonPressTime) * buttonPressTime
        if curr_dist > record_dist:
            winning_ways += 1
    print(winning_ways)

    

main("day6input.txt")