from openFile import OpenFile

def validHand(hand):
    maxCubes = {"red":12,"green":13,"blue":14}
    num,colour = hand.split(" ")
    # print("num is {} and colour is {}".format(num,colour))
    if int(num) > maxCubes[colour]:
        # print("False")
        return False
    # print("True")
    return True

def validGame(line):
    for grab in line:
        grab = grab.split(",")
        # print(grab)
        for hand in grab:
            hand = hand.strip()
            if not validHand(hand):
                return False
    return True

def main(input):
    data = OpenFile(input)
    gameid = 0
    ans = []
    for line in data:
        currLine = line.split(";")
        gameid += 1
        if currLine[0][0] == "G":
            currLine[0] = currLine[0][(currLine[0].index(":"))+2:]
        # print(currLine)
        if (validGame(currLine)):
            ans.append(gameid)
                        
    print(ans)
    print(sum(ans))

main("day2input.txt")