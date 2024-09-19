def openFile(inputfile):
    with open(inputfile,"r") as data:
        data = data.read()
        data = data.split("\n\n")
    return data

def mainv2(input):
    data = openFile(input)
    seeds = data[0].split()[1:]
    intervals = []
    for seedpair in range(len(seeds)//2):
        intervals.append((int(seeds[seedpair*2]),int(seeds[seedpair*2]) + int(seeds[seedpair*2+1])))
    # print(intervals)    
    counter = 0
    while True:
        counter += 1
        print("counter is ",counter)
        output = counter
        for eachmapping in range(7,0,-1):
            output = reverse_mapping(data[eachmapping],output)
            # print(output)
        for eachinterval in intervals:
            if output >= eachinterval[0] and output <= eachinterval[1]:
                print("the final location is {}".format(counter))
                return
    # output = 46
    # for eachmapping in range(7,-1,-1):
    #     output = reverse_mapping(data[eachmapping],output)
    # print(output)

def reverse_mapping(map,value):
    map = map.split() # split each mapping into individual words or numbers
    # print(map)
    finalval = [] # an array of tuples that contains the starting number, max number and the relative function
    # print(map)
    for index in range(2,len(map)-1,3): # increment by 3 each time because each set of 3 numbers contains the mapping details - destination range start, source range start, range length
        finalval.append((int(map[index]),int(map[index])+int(map[index+2])-1,int(map[index+1]) - int(map[index])))
    finalval.sort()
    for x in finalval:
        if value >= x[0] and value <= x[1]:
            return value + x[2]
    return value

mainv2("day5input.txt")
##### reverse mapping took too long or i didn't implement properly
################################################################################################################################################################################
