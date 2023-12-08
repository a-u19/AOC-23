def GetStarSymbolIndexes(data):    
    symbolIndexes = []
    for linenum,line in enumerate(data):
        # print(line)
        for characterindex,character in enumerate(line):
            # Checks if each character isn't a digit, or a full stop and in which case it must be a symbol.
            # The last condition is used to ensure that trailing whitespaces aren't looked at.
            if character == "*" and characterindex < len(line) - 1:
                # The "coordinates" of the symbol are appended to a list.
                symbolIndexes.append((linenum,characterindex))
            # print("symbol indexes are {}".format(symbolIndexes))
    # print(symbolIndexes)
    return symbolIndexes
 
def GetSurroundingNumbersIndexes(data,indexOfASymbol):
    # print(indexOfASymbol)
    yCoord,xCoord = indexOfASymbol[0],indexOfASymbol[1]
    # print("x coord is {} and y coord is {}".format(xCoord,yCoord))
    numbers = []
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            if data[yCoord+y][xCoord+x].isdigit():
                # print("yes at {},{},{} is a number".format(yCoord+y,xCoord+x,data[yCoord+y][xCoord+x]))
                numbers.append((yCoord+y,xCoord+x))
    return(numbers)

def GetNumbersFromIndexes(data,numberIndex):
    yCoord,xCoord = numberIndex[0],numberIndex[1]
    number = ""
    midDigit = False

    # This checks whether there are digits to the right or left and use this information to obtain the digits surrounding it
    if xCoord == 0:
        towardsRightNumber = True
    elif xCoord == len(data[0]) - 1:
        towardsRightNumber = False
    elif data[yCoord][xCoord+1].isdigit() and data[yCoord][xCoord-1].isdigit():
        midDigit = True
    elif data[yCoord][xCoord+1].isdigit():
        towardsRightNumber = True
    else:
        towardsRightNumber = False

    if midDigit:
        leftP,rightP = xCoord-1,xCoord
        while leftP > -1 and data[yCoord][leftP].isdigit():
            number = data[yCoord][leftP] + number
            leftP -= 1
        while rightP < len(data[0]) - 1 and data[yCoord][rightP].isdigit():
            number += data[yCoord][rightP]
            rightP += 1
    elif towardsRightNumber:
        while xCoord < len(data[0]) - 1 and data[yCoord][xCoord].isdigit():
            number += data[yCoord][xCoord]
            xCoord += 1    
    elif not towardsRightNumber:
        while xCoord > - 1 and data[yCoord][xCoord].isdigit():
            number = data[yCoord][xCoord] + number
            xCoord -= 1

    return(number)
# main("day3testdatainput.txt")

def mainv2(inputdata):
    res = 0
    with open(inputdata,"r") as data:
        data = data.readlines()
    starSymbolIndexes = GetStarSymbolIndexes(data)
    for index in range(len(starSymbolIndexes)):
        eachNumIndex = GetSurroundingNumbersIndexes(data,starSymbolIndexes[index])
        for eachitem in eachNumIndex:
            i = 1
            while (eachitem[0],eachitem[1]+ i) in eachNumIndex:
                eachNumIndex.remove((eachitem[0],eachitem[1]+i))
                i += 1
        if len(eachNumIndex) != 2:
            continue
        # for coordinatesOfNumbers in eachNumIndex:
        #     print(GetNumbersFromIndexes(data,coordinatesOfNumbers))
        res += (int(GetNumbersFromIndexes(data,eachNumIndex[0])) * int(GetNumbersFromIndexes(data,eachNumIndex[1])))
    print(res)
    

mainv2("day3input.txt")
