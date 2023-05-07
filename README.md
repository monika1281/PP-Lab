#Python program to print all prime numbers in a given interval (use break)

n1=int(input("Enter n1:"))

n2=int(input("Enter n2:"))

I, j=0, 0

for I in range(n1,n2+1):

    for j in range(2,I+1):

        if I%j==0:

            break

    if I==j:

        print(I)
______________
output:
Enter n1:2
Enter n2:15
2
3
5
7
11
13
        
