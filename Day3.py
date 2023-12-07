def main(inputdata):
    with open(inputdata,"r") as data:
        data = data.readlines()
    symbolIndexes = GetSymbolIndexes(data)
        
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
 
def GetSurroundingNumbers(indexOfASymbol):
    xCoord,yCoord = indexOfASymbol[0],indexOfASymbol[1]
    for y in [-1,0,1]:
        for x in [-1,0,1]:
            if 
GetSurroundingNumbers((1,3))
