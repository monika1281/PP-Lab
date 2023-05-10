#addition of matrix
import numpy as np
r1=int(input("rows:"))
c1=int(input("columns:"))
li1=list(map(int,input().split()))
matrix1=np.array(li1).reshape(r1,c1)
print(matrix1)

r2=int(input("rows:"))
c2=int(input("columns:"))
li2=list(map(int,input().split()))
matrix2=np.array(li2).reshape(r2,c2)
print(matrix2)
if r1==r2 and c1==c2:
  mat3=np.add(matrix1,matrix2)
  print(mat3)
else:
  print("Invalid matrix")
output:
rows:2
columns:2
1 2 3 4
[[1 2]
 [3 4]]
rows:2
columns:2
1 2 3 4
[[1 2]
 [3 4]]
[[2 4]
 [6 8]]



