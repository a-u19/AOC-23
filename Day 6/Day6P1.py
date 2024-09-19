def OpenFile(file):
    with open(file,"r") as file:
        data = file.readlines()
    return data

def main(input):
    data = OpenFile(input)
    #separate the input into times and distances
    times = []
    dists = []
    ans = 1
    for line in data:
        line = line.split()
        line.pop(0)
        for race in line:
            times.append(int(race))
    #i appended everything to the single list times then split it between both lists appropriately
    dists = times[len(times)//2:]
    print(dists)
    times = times[:len(times)//2]
    print(times)
    # times = [7]
    # dists = [9]
    for time_i in range(len(times)):
        winning_ways = 0
        record_dist = dists[time_i]
        for buttonPressTime in range(times[time_i]):
            curr_dist = (times[time_i] - buttonPressTime) * buttonPressTime
            # print(curr_dist)
            if curr_dist > record_dist:
                winning_ways += 1
        # print(winning_ways)
        ans *= winning_ways
    print(ans)


    

main("day6input.txt")