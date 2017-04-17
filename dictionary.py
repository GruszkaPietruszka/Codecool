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


dictionary = []


#import z .txt
with open('slowniczek.txt') as inputfile:
	for line in inputfile:
		dictionary.append(line)

dictionary.sort() #tu elegancko sortujemy

# for i in range(0,len(dictionary)):
print(dictionary)

inputfile.close() #klasycznie zamykamy
'''
menu = {}
menu['1']="Add Student."
menu['2']="Delete Student."
menu['3']="Find Student"
menu['4']="Exit"


while True:
	options=menu.keys()
	#options.sort()
	for entry in options:
		print(entry, menu[entry])
		selection = input("Please Select:")
		if selection =='1':
			print("Sec 1")
		elif selection == '2':
			print("sec 2")
		elif selection == '3':
			print("sec 3")
		elif selection == '4':
			break
		else:
			print("lipa")

'''

definition = input("co mam odac?")
add_definition(definition)
print(find_by_word("a",dictionary))
print(find_by_first_letter('a',dictionary))
#znajdowanie po slowie
for i in range(0,len(find_by_word('madziksior',dictionary))):
	print("Znajdowanie po slowie Madzikisor",dictionary[find_by_word('madziksior',dictionary)[i]])

#znajodwanie po literze
for i in range(0,len(find_by_first_letter('a',dictionary))):
	print("\nznajdowanie po literze: a",dictionary[find_by_first_letter('a',dictionary)[i]])
