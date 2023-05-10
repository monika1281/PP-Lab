#create a matrix and print it.
r=int(input("enter the number of rows:"))
c=int(input("enter the number of columns:"))  #using list it is possible to store elements in contiguous memory location
matrix=[]
print("enter the elements of a matrix:")
for i in range(r):
  a=[]
  for j in range(c):
    a.append(int(input()))
    #print(a)
  matrix.append(a)
#print(matrix)
for i in range(r):enter the number of rows:2
enter the number of columns:2
enter the elements of a matrix:
2
3
4
5
2 3 
4 5 
  for j in range(c):
    print(matrix[i][j], end=" ")
  print()
output:
enter the number of rows:2
enter the number of columns:2
enter the elements of a matrix:
2
3
4
5
2 3 
4 5 
