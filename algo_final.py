#metrices values of each topoloy
ring=[[0,1,0,0,0,1],[1,0,1,0,0,0],[0,1,0,1,0,0],[0,0,1,0,1,0],[0,0,0,1,0,1],[1,0,0,0,1,0]]
mesh=[[0,1,0,0,1,0],[1,0,1,0,0,0],[0,1,0,1,0,0],[1,0,1,0,1,1],[1,0,0,1,0,0],[0,0,0,1,0,0]]
star=[[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[0,0,0,0,0,1],[1,1,1,1,1,0]]
tree=[[0,1,0,0,0,0],[1,0,1,0,0,0],[0,1,0,0,0,0],[0,1,0,0,1,0],[0,0,0,1,0,1],[0,0,0,0,1,0]]
fully_connected=[[0,1,1,1,1,1],[1,0,1,1,1,1],[1,1,0,1,1,1],[1,1,1,0,1,1],[1,1,1,1,0,1],[1,1,1,1,1,0]]
line=[[0,1,0,0,0,0],[1,0,1,0,0,0],[0,1,0,1,0,0],[0,0,1,0,1,0],[0,0,0,1,0,1],[0,0,0,0,1,0]]
bus=[[0,1,1,1,1,1],[1,0,0,0,0,1],[1,0,0,0,0,1],[1,0,0,0,0,1],[1,0,0,0,0,1],[1,1,1,1,1,0]]
#corrisponding name of each matrix
topology=[ring,mesh,star,tree,fully_connected,line,bus]
names=['ring','mesh','star','tree','fully_connected','bus']
#varibalbe for saving values
var = ''
#taking number of rows and columns
n = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

#initialize matrix
matrix = []
print("Enter your matrix row by row:")

#for user input
for i in range(n):  #loop for row entries
    a = []
    for j in range(C):  #loop for column entries
        a.append(int(input()))
    matrix.append(a)
#searching for the inputed matrix in the list of matrices

for i in range(0, len(names)):
    if matrix == topology[i]: #iffound savethe name of the matrix in var
        var = names[i]

        break
    else: #else print not found
        var = "Not Found"
print(var)