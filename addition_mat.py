r1=int(input("enter the number of rows:"))
c1=int(input("enter the number of columns:"))  
matrix1=[]
print("enter the elements of a matrix:")
for i in range(r1):
  a=[]
  for j in range(c1):
    a.append(int(input()))
  matrix1.append(a)
for i in range(r1):
  for j in range(c1):
    print(matrix1[i][j], end=" ")
  print()
r2=int(input("enter the number of rows:"))
c2=int(input("enter the number of columns:"))  
matrix2=[]
print("enter the elements of a matrix:")
for i in range(r2):
  b=[]
  for j in range(c2):
    b.append(int(input()))
  matrix2.append(b)
for i in range(r2):
  for j in range(c2):
    print(matrix2[i][j], end=" ")
  print()
print("Resultant matrix:")

res=[]
if r1==r2 and c1==c2:
  for i in range(r1):
    c=[]
    for j in range(c1):
      c.append(matrix1[i][j]+matrix2[i][j])
    res.append(c)
else:
  print("Invalid matrix.")
for i in range(r1):
  for j in range(c1):
    print(res[i][j] ,end=" ")

  print()
 output:
 enter the number of rows:2
enter the number of columns:2
enter the elements of a matrix:
1
2
3
4
1 2 
3 4 
enter the number of rows:2
enter the number of columns:2
enter the elements of a matrix:
1
2
3
4
1 2 
3 4 
Resultant matrix:
2 4 
6 8 
