n = 5
m=3
print(1)
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()
"""
1
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
"""
print(2)
print("-------------------------------")
for i in range(1,m+1):
    for j in range(1,n+1):
        print("*", end=" ")
    print()
"""
2
* * * * * 
* * * * * 
* * * * * 
"""
print("-------------------------------")
print(3)

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
"""
3
* 
* * 
* * * 
* * * * 
* * * * * 
"""
print("-------------------------------")
print(4)

for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
"""
4
        * 
      * * 
    * * * 
  * * * * 
* * * * * 
"""
print("-------------------------------")
print(5)
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end=" ")
    print()
"""
5
* * * * * 
* * * * 
* * * 
* * 
* 
"""
print("-------------------------------")
print(6)
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
     
"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
print("-------------------------------")
print(7)
