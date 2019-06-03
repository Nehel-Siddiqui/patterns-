a = int(input("Enter max star to be display on single line"))
for i in range (0, a):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range (a, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")