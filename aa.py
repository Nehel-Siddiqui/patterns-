# Triangle half pyramide patteren
a = int(input("Enter a numbers where you want to start your series: "))
c = int(input("Enter a numbers where you want to stop your series: "))
for i in range(a-1 , c+2) :
	for j in range (a,i) :
		print (j , end="  ")
	print()