def getNumold(line):
	currnum = ""
	for index in range(len(line)//2+1):
		if len(currnum) == 2:
			return currnum
		# print(line[index])
		if line[index].isdigit():
			# print("index {} is {}".format(index,line[index]))
			currnum += line[index]
		if len(currnum) == 2:
			return currnum
		if line[-index].isdigit():
			# print("index {} is {}".format(-index,line[-index]))
			currnum += line[-index]
		# print(currnum)
	return (currnum + currnum)

def main():
	sum = 0
	with open("input.txt", "r") as data:
		data = data.read().strip().split("\n")
		for index in range(len(data)):
			#print(index)
			# print((getNum(data[index])))
			sum += int(getNum(data[index]))
	print(sum)

def getNum(line):
	num = []
	for char in line:
		if char.isdigit():
			num.append(char)
	return num[0] + num[-1]

def getNum2(line):
	nums = []
	wordlist = ["zero","one","two","three","four","five","six","seven","eight","nine"]
	for i,letter in enumerate(line):
			for val,num in enumerate(wordlist):
				if num in line[i:i+len(num)]:
					nums.append(str(val))
				if letter.isdigit():
					nums.append(letter)
	return nums[0] + nums[-1]

def mainv2():
	sum = 0
	with open("than.txt", "r") as data:
		data = data.read().strip().split("\n")
		for index in range(len(data)):
			#print(index)
			# print((getNum(data[index])))
			sum += int(getNum2(data[index]))
	print(sum)
# print(getNum("mbvtbcjvv33rqfsllshb"))
# main()
# print(getNum2("two1nine"))
# mainv2()
# print(getNum2("28gtbkszmrtmnineoneightmx"))