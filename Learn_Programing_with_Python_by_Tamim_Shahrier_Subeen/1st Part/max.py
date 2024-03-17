n1 = input("Enter number 1: ")
n1 = int(n1)

n2 = input("Enter number 2: ")
n2 = int(n2)

n3 = input("Enter number 3: ")
n3 = int(n3)

if n1 > n2:
	max_n = n1
else:
	max_n = n2
if n3 > max_n:
	max_n = n3

print("Maximum: ", max_n)