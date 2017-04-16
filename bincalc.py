def bintodec( bin_num ):
	result = 0
	j=1
#	while bin_num > 0:
	for i in range(0,len(bin_num)):
		if bin_num[-j] == '1':
			result += pow(2,i)
		j+=1
	return result



def dectobin ( dec_num ):
	result = []
#	if dec_num == 0:
#		return 0
#	if dec_num == 1:
#		return 1

	while True:
		div_result = int(dec_num) / 2
		if int(dec_num) % 2 == 0:
			result.insert(0,'0')
		elif int(dec_num) % 2 == 1:
			result.insert(0,'1')

		if div_result == 1:
			result.insert(0,'1')
			break
		elif div_result == 0:
			result.insert(0,'0')
			break
		dec_num = div_result
	return result


x = True
while x:
	number = input("Gimme number then number system. For example: 10101 2 or 2495 10\n")

	print(number)

	split_numbers = number.split(" ")

	print("split number: ",split_numbers)
	if len(split_numbers) == 2 and split_numbers[0].isnumeric() and split_numbers[1].isnumeric() :
		first = split_numbers[0]
		second = split_numbers[1]
	else:
		print("Something went wrong! Lets go one more time")




	if second == '10':
		print(dectobin(first))
	elif second == '2':
		for i in range(0,len(first)):
			if first[i] != '0' and first[i] != '1':
				print("ERROR! THIS IS NOT BIN NUMBER!")
			else:
				print(bintodec(first))
				break
