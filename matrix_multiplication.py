#matrix multiplication
r1=int(input("enter the number of rows of mat1:"))
c1=int(input("enter the number of columns of mat1:"))  
matrix1=[]
print("enter the elements of a matrix 1:")
for i in range(r1):
  a=[]
  for j in range(c1):
    a.append(int(input()))
  matrix1.append(a)
for i in range(r1):
  for j in range(c1):
    print(matrix1[i][j], end=" ")
  print()
r2=int(input("enter the number of rows of mat1:"))
c2=int(input("enter the number of columns of mat1:"))  
matrix2=[]
res=[]
print("enter the elements of a matrix 2:")
for i in range(r2):
  b=[]
  for j in range(c2):
    b.append(int(input()))
  matrix2.append(b)
for i in range(r2):
  for j in range(c2):
    print(matrix2[i][j], end=" ")
  print()
res=[]
if c1==r2:
  for i in range(r1):
    c=[]
    for j in range(c2):
      e=0
      for k in range(c1):
        e=e+(matrix1[i][k]*matrix2
         [k][j])
      c.append(e)
    res.append(c)
  print("resultant mat:")
  for i in range(len(res)):
    d=res[i]
    for j in range(len(d)):
      print(d[j],end=" ")
    print()

else:
  print("invalid mat")
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
0
0
1
1 0 
0 1 
resultant mat:
1 2 
3 4 
