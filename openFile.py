def OpenFile(file):
    with open(file,"r") as file:
        data = file.readlines()
    return data