#Dictionary

database = {
	"home" : "ngoi nha",
	"baby" : "em be"
}

def showMenu():
	print("====================")
	print("CHUONG TRINH TU DIEN")
	print("====================")
	print("1. Them tu")
	print("2. Tim tu")
	print("3. Xoa tu")
	print("4. Xem tat ca tu")
	print("0. Thoat")
	print("====================")

#Insert word
def insert():
	word = input("New word: ")
	mean = input("Mean of word: ")
	database[word] = mean
	print("Insert successed.")


#Find word
def find():
	print("Find word")
	word = input("Key search: ")
	if word in database:
		print("Search completed!!!")
		print("Word: {} ".format(word) + "	Mean: {}".format(database[word]))
		print("Thank you")
	else:
		print("Sorry {} not available !!! Please try again".format(word))

#delete word
def delete():
	print("Delete word")
	word = input("Key delete: ")
	if word in database:
		del database[word]
		print("{} was deleted. Thank you".format(word))
	else:
		print("Sorry {} not available !!! Please try again".format(word))

#Show all
def showAll():
	k = 0
	for i in database:
		k += 1
		print(str(k) + ". Word: {} ".format(i) + "	Mean: {} ".format(database[i]))

#Show menu
showMenu()

#Progress
choice = int(input("Xin hay chon su kien: "))

while choice != 0:
	if choice == 0: 
		break
	elif choice == 1:
		#Insert
		insert()

	elif choice == 2:
		#Find word
		find()

	elif choice == 3:
		#Delete word
		delete()

	elif choice == 4:
		#Show All
		showAll()
	else:
		print("Please choice again !!!")

	choice = int(input("Xin hay chon su kien: "))

print("See you again ^_^")