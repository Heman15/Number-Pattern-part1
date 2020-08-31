""" Using for loop and Range
input : 6
output
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
N = int(input("Enter the total rows:"))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print(" ")


"""using range or for loop
input : 6
output
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
N = int(input("Enter the total rows:"))
for i in range(1,N+1):
    for j in range(1,i+1):
        print(j,end= " ")
    print(" ")

""" Inverted pyramid Pattern 
input : 6
output
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
"""
N = int(input("Enter the number of rows:"))
B =0
for i in range(N-1,0,-1):
    B+=1
    for j in range(1,i+1):
        print(B , end=" ")
    print("")
"""Inverted pyramid pattern with same numbers
input:5
ouput
5 5 5 5 5
5 5 5 5
5 5 5
5 5
5"""
N = int(input("Enter the Total Rows:"))
for i in range(N,0 ,-1):
    for j in range(1,i+1):
        print(N,end=" ")
    print("")

""" Display descending order of number
intput: 5
output
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1
"""
N = int(input("Enter the Total Rows:"))
for i in range(N,0,-1):
    for j in range(1,i+1):
        print(i,end=" ")
    print("")



