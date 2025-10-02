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
6
* * * * *
  * * * *
    * * *
      * *
        *
"""
print("-------------------------------")
print(7)
s = 4
for i in range(1,s+1):
    for j in range(s-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()
    

"""
7
      *
    * * *
  * * * * *
* * * * * * *
"""
print("-------------------------------")
print(8)
n=3
for i in range(1,n+1):
    z=2*i-1
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(z):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for k in range(2*i-1):
        print("*",end=" ")
    print()


"""
8
    *
  * * *
* * * * *
  * * *
    *
"""
print("-------------------------------")
print(9)
n= 4
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    for j in range(2*(n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

"""
9
*             * 
* *         * * 
* * *     * * * 
* * * * * * * * 
* * *     * * * 
* *         * * 
*             * 
"""
print("-------------------------------")
print(10)
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


"""
10
*
* *
* * *
* * * *
* * *
* *
*
"""
print("-------------------------------")
print(11)
n=4
for i in range(1,n+1):
    for j in range((n-i)):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


"""
11
      *
    * *
  * * *
* * * *
  * * *
    * *
      *
"""
print("-------------------------------")
print(12)
for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


"""
12
* * * *
  * * *
    * *
      *
    * *
  * * *
* * * *
"""
print("-------------------------------")
print(13)
n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

"""
13
*
* *
* * *
* * * *
* * * * *

"""
print("-------------------------------")
print(14)
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
14
* * * * *
* * * *
* * *
* *
*

"""
print("-------------------------------")
print(15)
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


"""
15
      *
    * *
  * * *
* * * *
"""
print("-------------------------------")
print(16)
n=4
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


"""
16
* * * *
*     *
*     *
* * * *
"""
