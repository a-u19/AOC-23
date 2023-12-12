def openFile(inputfile):
    with open(inputfile,"r") as data:
        data = data.read()
        data = data.split("\n\n")
    return data

def main(input):
    data = openFile(input)
    seeds = data[0].split()[1:]
    # print(mapping(data[1],79))
    locationnum = []
    for eachseed in seeds:
        output = int(eachseed)
        for eachmapping in range(1,8):
            output = mapping(data[eachmapping],output)
            # print(output)
        locationnum.append(output)
    print(min(locationnum))

def mapping(map,value):
    map = map.split() # split each mapping into individual words or numbers
    # print(map)
    finalval = [] # an array of tuples that contains the starting number, max number and the relative function
    # print(map)
    for index in range(2,len(map)-1,3): # increment by 3 each time because each set of 3 numbers contains the mapping details - destination range start, source range start, range length
        finalval.append((int(map[index+1]),int(map[index+1])+int(map[index+2])-1,int(map[index]) - int(map[index+1])))
    finalval.sort()
    # print(finalval)
    for x in finalval:
        if value >= x[0] and value <= x[1]:
            return value + x[2]
    return value
    
# main("day5testdatainput.txt")
# main("day5input.txt")
def testmapping(inputvalue):
    data = openFile("day5testdatainput.txt")
    seeds = data[0].split()[1:]
    output = inputvalue
    for eachmapping in range(1,8):
        output = mapping(data[eachmapping],output)
    print(output)

testmapping(2232685647)