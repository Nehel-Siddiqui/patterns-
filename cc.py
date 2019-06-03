#Print half pyramid pattern using an asterisk (star)
b = int(input("Enter a numbers ,how many rows you want to print asterisk : "))
for i in range(1 , b+1) :
	for j in range (i) :
		print ("*" , end="  ")
	print()