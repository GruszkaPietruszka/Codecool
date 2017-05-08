def add_definition(definition):
	with open('slowniczek.txt','a') as inputfile:
		inputfile.write(definition+'\n')

def find_by_word(word, tab): #szukanie po slownie, albo czy litera
	index = []
	for i in range(0, len(tab)):
		if word in tab[i]:
			index.append(i)
	return index

def find_by_first_letter(letter, tab):
	index = []
	first_letter = ''
	for i in range(0, len(tab)):
		first_letter = tab[i]
		if first_letter[0] == letter:
			index.append(i)
	return index




def main():

	dictionary = []


	#import z .txt
	with open('slowniczek.txt') as inputfile:
		for line in inputfile:
			dictionary.append(line)

	dictionary.sort()

	inputfile.close()
	print('''Dictionary for a little programmer:
1) search explanation by appellation
2) add new definition
3) show all appellations alphabetically
4) show available definitions by first letter of appellation
0) exit''')

	while True:
		selection = input("Please Select:")
		if selection =='1':
			print("1) search explanation by appellation ")
			word = input("Please gimme word")
			for i in range(0,len(find_by_word(word,dictionary))):
				print("Searching by word: \'",word,'\'',dictionary[find_by_word(word,dictionary)[i]])
		elif selection == '2':
			print("2) add new definition")
			definition = input("What shall i add??")
			add_definition(definition)
		elif selection == '3':
			print("3) show all appellations alphabetically")
			for i in range(0,len(dictionary)):
				print(dictionary[i])
		elif selection == '4':
			print("4) show available definitions by first letter of appellation ")
			first_letter = input("gimme first letter")
			for i in range(0,len(find_by_first_letter(first_letter,dictionary))):
				print("\nSearching by first letter:" ,dictionary[find_by_first_letter(first_letter,dictionary)[i]])
		elif selection == '0':
			print("0) exit")
			break




main()
