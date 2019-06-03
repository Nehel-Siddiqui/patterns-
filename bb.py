#print number patteren
a = int(input("Enter a numbers where you want to start your series: "))
b = int(input("Enter a numbers where you want to stop your series: "))
for i in range(a , b+1) :
	for j in range (i) :
		print (i , end="  ")
	print()