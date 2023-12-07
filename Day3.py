def main(inputdata):
    with open(inputdata,"r") as data:
        data = data.readlines()
    symbolIndexes = GetSymbolIndexes(data)
    GetSurroundingNumbers(data,symbolIndexes[0])
        
def GetSymbolIndexes(data):    
    symbolIndexes = []
    for linenum,line in enumerate(data):
        # print(line)
        for characterindex,character in enumerate(line):
            # Checks if each character isn't a digit, or a full stop and in which case it must be a symbol.
            # The last condition is used to ensure that trailing whitespaces aren't looked at.
            if character.isdigit() == False and character not in ["."] and characterindex < len(line) - 1:
                # The "coordinates" of the symbol are appended to a list.
                symbolIndexes.append((linenum,characterindex))
    # print(symbolIndexes)
    return symbolIndexes
 
def GetSurroundingNumbers(data,indexOfASymbol):
    xCoord,yCoord = indexOfASymbol[0],indexOfASymbol[1]
    numbers = []
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            if data[yCoord+y][xCoord+x].isdigit():
                numbers.append((yCoord+y,xCoord+x))
    print(numbers)

main("day3testdatainput.txt")