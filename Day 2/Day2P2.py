from openFile import OpenFile

def main(input):
    data = OpenFile(input)
    ans = []
    for line in data:
        currLine = line.split(";")
        if currLine[0][0] == "G":
            currLine[0] = currLine[0][(currLine[0].index(":"))+2:]
        # print(currLine)
        minCubes = {"red":0,"green":0,"blue":0}
        minCubes = validGame(minCubes,currLine)
        tempans = 1
        for values in minCubes.values():
            tempans *= values
        ans.append(tempans)
    print(ans)
    print(sum(ans))

def validGame(minCubes,line):
    for grab in line:
        grab = grab.split(",")
        # print(grab)
        for hand in grab:
            hand = hand.strip()
            minCubes = validHand(minCubes,hand)
            # print(minCubes)
    return minCubes

def validHand(minCubes,hand):
    num,colour = hand.split(" ")
    # print("num is {} and colour is {}".format(num,colour))
    if int(num) > minCubes[colour]:
        # print("False")
        minCubes[colour] = int(num)
    return minCubes

main("day2input.txt")