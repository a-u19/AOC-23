from openFile import OpenFile

def part1():
    data = OpenFile("day2input.txt")
    for line in data:
        currLine = line.split(";")
        dict = {}
        # print(currLine)
        # print(currLine[0].index(":"))
        currLine = currLine[7:]
        print(currLine)


part1()