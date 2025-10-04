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
print("-------------------------------")
print(17)
m=4
n=5
for i in range(1,m+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==m or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
"""
17
* * * * *
*       *
*       *
* * * * *

"""
print("-------------------------------")
print(18)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if i==1 or j ==1 or j==i or i ==n or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
18
*
* *
*   *
*     *
* * * * *
"""
print("-------------------------------")
print(19)
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if i==1  or j==1 or i==n or j==i:
            
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()

"""
19
        *
      * *
    *   *
  *     *
* * * * *
"""

print("-------------------------------")
print(20)
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i == 1 or j ==1 or i==n  or j==i:
            print("*",end= " ")
        else:
            print(" ",end=" ")
    print()


"""
20
* * * * *
*     *
*   *
* *
*
"""
print("-------------------------------")
print(21)

for i in range(n,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        if  i ==n or j ==i or i == 1 or j==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
21
* * * * *
  *     *
    *   *
      * *
        *
"""
print("-------------------------------")
print(22)
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if i==1 or i==n or j==1 or j ==2*i-1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


"""
22
      *
    *   *
  *       *
* * * * * * *
"""
print("-------------------------------")
print(23)
n=3
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==2*i-1 or j ==1 or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==2*i-1 or j ==1 or i==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

"""
23
    *
  *   *
*       *
  *   *
    *
"""
print("-------------------------------")
print(24)
n = 4

for i in range(1, n+1):
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(1, 2*(n-i)+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(n, 0, -1):
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(1, 2*(n-i)+1):
        print(" ", end=" ")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


"""
24
*       *
* *   * *
*   *   *
*       *
*   *   *
* *   * *
*       *
"""

print("-------------------------------")
print(25)
n = 5

for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if i == n or j == 1 or j == 2*i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end=" ")
    for j in range(1, 2*i):
        if i == n or j == 1 or j == 2*i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()



"""
25
* * * * *
*       *
  *   *
    *
  *   *
*       *
* * * * *
"""
print("-------------------------------")
print(26)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()



"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
print("-------------------------------")
print(27)
n= 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


"""
27
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5 
"""
print("-------------------------------")
print(28)
n=4
c=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c,end=" ")
        c+=1
    print()

    
"""
28
1
2 3
4 5 6
7 8 9 10
"""
print("-------------------------------")
print(29)
n=5
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

"""
29

1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

print("-------------------------------")
print(30)
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

"""
30
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1

"""

print("-------------------------------")
print(31)
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    print()

"""
31
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5
"""

print("-------------------------------")
print(32)
n=4
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
"""
32
      1
    1 2 1
  1 2 3 2 1
1 2 3 4 3 2 1
"""


print("-------------------------------")
print(33)
n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i*2)%2==0:
            print(j*2,end=" ")
    print()
"""
33
2
2 4
2 4 6
2 4 6 8
2 4 6 8 10
"""

print("-------------------------------")
print(34)
for i in range(1,n+1):
    c=1
    for j in range(1,i+1):
        print(c,end=" ")
        c+=2
    print()
"""
34
1
1 3
1 3 5
1 3 5 7
1 3 5 7 9
"""

print("-------------------------------")
print(35)
for i in range(n):
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()

"""
35
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
"""