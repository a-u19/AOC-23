def main(input):
	with open(input,"r") as data:
		data = data.readlines()
		res = 0
	for line in data:
		line = line[9:]
		#print(line)
		numbers = line.split("|")
		#print(numbers)
		winningnums,mynums = numbers[0],numbers[1]
		winningnums = winningnums.split()
		mynums = mynums.split()
		for i,eachnum in enumerate(mynums):
			mynums[i] = int(eachnum)
		for j,eachnum in enumerate(winningnums):
			winningnums[j] = int(eachnum)
		winningnums.sort()
		mynums.sort()
		#print(mynums)
		n = 0
		for winningNumber in winningnums:
			if matchingNum(winningNumber,mynums):
				n += 1
		#print(n)
		if n != 0:
			res += 2**(n-1)
	print(res)

def matchingNum(winningNumber,myNums):
	if winningNumber in myNums:
		return True
	return False

def mainv2(input):
	with open(input,"r") as data:
		data = data.readlines()
	res = [1]*len(data)
	# print(res)	
	for cardnum,line in enumerate(data):
		line = line[9:]
		#print(line)
		numbers = line.split("|")
		#print(numbers)
		winningnums,mynums = numbers[0],numbers[1]
		winningnums = winningnums.split()
		mynums = mynums.split()
		for i,eachnum in enumerate(mynums):
			mynums[i] = int(eachnum)
		for j,eachnum in enumerate(winningnums):
			winningnums[j] = int(eachnum)
		winningnums.sort()
		mynums.sort()
		#print(mynums)
		n = 0
		for winningNumber in winningnums:
			if matchingNum(winningNumber,mynums):
				n += 1
		#print(n)
		if n != 0:
			for add in range(1,n+1):
				res[cardnum + add] += res[cardnum]
	# print(res)
	print(sum(res))

# main("day4.txt")
# mainv2("day4testdatainput.txt")
mainv2("day4.txt")
