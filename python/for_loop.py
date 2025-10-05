n = 5
for i in range(1,n+1):
    print(i)
"""
1
2
3
4
5
"""
print("---------------------------------------------------")
m=3
n=7
for i in range(m,n+1):
    print(i)
"""
3
4
5
6
7
"""
print("---------------------------------------------------")
n=5
for i in range(n,0,-1):
    print(i)
"""
5
4
3
2
1
"""
print("---------------------------------------------------")
n=10
m=6
for i in range(n,m-1,-1):
    print(i)
"""
10
9
8
7
6
"""
print("---------------------------------------------------")
n= 5
s=0
for i in range(1,n+1):
    s+=i
print(s)
#15
print("---------------------------------------------------")
n=5
fac =1
for i in range(1,n+1):
    fac*=i
print(fac)
#120
print("---------------------------------------------------")
m=3
n=6
s=0
for i in range(m,n+1):
    s+=i
print(s)
#18
print("---------------------------------------------------")
m=2
n=4
s=1
for i in range(m,n+1):
    s*=i
print(s)
#24
print("---------------------------------------------------")
n=6
for i in range(1,n+1):
    if n%i==0:
        print(i)
    else:
        pass
"""
1
2
3
6
"""
print("---------------------------------------------------")
n=6
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
    else:
        pass
print(count) #4
print("---------------------------------------------------")
n=7
c=0
for i in range(1,n):
    if n%i==0:
        c+=1
    else:
        pass
if c==1:
    print("prime")
else:
    print("not prime")
#prime
    
print("---------------------------------------------------")
m=3
n=10
for i in range(m,n+1):
    if i%2==0:
        print(i)
    else:
        pass
"""
4
6
8
10
"""
print("---------------------------------------------------")
m=3
n=10
for i in range(m,n+1):
    if i%2!=0:
        print(i)
    else:
        pass
"""
3
5
7
9
"""
print("---------------------------------------------------")
m=3
n=7
ec=0
oc=0
for i in range(m,n+1):
    if i%2==0:
        ec+=1
    else:
        oc+=1
print(f"even count: {ec} | odd count: {oc}")
#2 and 3
print("---------------------------------------------------")
string = "hello"
res=""
for i in range(len(string)-1,-1,-1):
    res+=string[i]
print(res)
#olleh
print("---------------------------------------------------")
string = "madam"
res=""
for i in range(len(string)-1,-1,-1):
    res+=string[i]
if res==string:
    print("palindrome")
#palindrome
print("---------------------------------------------------")
print("sum of digits for loop")
n=123
res=0
for i in range(len(str(n))):
    a=0
    a = n%10
    n//=10
    res+=a
print(res)
#sum of digits for loop
#6
print("---------------------------------------------------")
print("product of digits for loop")

n=123
res=1
for i in range(len(str(n))):
    a=0
    a = n%10
    n//=10
    res*=a
print(res)
#product of digits for loop
#6
print("---------------------------------------------------")
n=153
temp=n
res=0
for i in range(len(str(n))):
    a=n%10
    n//=10
    s = a**len(str(temp))
    res+=s
if res==temp:
    print("armstrong")
else:
    print("not armstrong")
#armstrong
print("---------------------------------------------------")
print("reverse a number")
n = 123
temp = n
rev=" "
for i in range(len(str(n))):
    a = n%10
    s=""
    s=str(a)
    rev =rev+s
    n//=10
print(int(rev))
#321
print("---------------------------------------------------")
n=121
temp =n
res=""
for i in range(len(str(n))):
    a = n%10
    res+=str(a)
    n//=10
res= int(res)
if res ==temp:
    print("palindrome")
else:
    print("not palindrome")
print("---------------------------------------------------")
string = "apple"
vowels = "aeiouAEIOU"
count=0
for i in string:
    if i in vowels:
        count+=1
    else:
        pass
print("vowels")
print(count)
print("---------------------------------------------------")
string = "apple"
vowels = "aeiouAEIOU"
count=0
for i in string:
    if i not in vowels:
        count+=1
    else:
        pass
print("consoants")
print(count)
print("---------------------------------------------------")
string = "apple"
vowels = "aeiouAEIOU"
vcount=0
ccount=0
for i in string:
    if i in vowels:
        vcount+=1
    else:
        ccount+=1
        
print("vowels count",vcount)
print("consoants count",ccount)
print("---------------------------------------------------")
n=496
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
    else:
        pass
if s==n:
    print("perfect number")
else:
    print("not perfect number")
print("---------------------------------------------------")
n=9
s=0
sq=n**2
for i in range(len(str(sq))):
    a=sq%10
    sq//=10
    s+=a
if s == n:
    print("neon number")
else:
    print("not neon number")
print("---------------------------------------------------")

n=145
temp=n
res=0
for i in range(len(str(n))):
    a = n%10
    fac=1
    for j in range(1,a+1):
        fac*=j
    res+=fac
    n//=10
if res==temp:
    print("Strong number")
else:
    print("not strong number")

print("---------------------------------------------------")
n=18
res=0
temp=n
for i in range(len(str(n))):
    a = n%10
    res+=a
    n//=10
if temp%res==0:
    print("Harshad number")
else:
    print("Not Harshad number")
            
print("---------------------------------------------------")
print("Fibonacci Series")
n=5
a=0
b=1
for i in range(n):
    print(a)
    a,b = b,a+b
print("---------------------------------------------------")
n=9
s=0
sq=n**2
for i in range(len(str(sq))):
    a=sq%10
    sq//=10
    s+=a
if s == n:
    print("neon number")
else:
    print("not neon number")
print("---------------------------------------------------")
"""
1
2
3
4
5
---------------------------------------------------
3
4
5
6
7
---------------------------------------------------
5
4
3
2
1
---------------------------------------------------
10
9
8
7
6
---------------------------------------------------
15
---------------------------------------------------
120
---------------------------------------------------
18
---------------------------------------------------
24
---------------------------------------------------
1
2
3
6
---------------------------------------------------
4
---------------------------------------------------
prime
---------------------------------------------------
4
6
8
10
---------------------------------------------------
3
5
7
9
---------------------------------------------------
even count: 2 | odd count: 3
---------------------------------------------------
olleh
---------------------------------------------------
palindrome
---------------------------------------------------
sum of digits for loop
6
---------------------------------------------------
product of digits for loop
6
---------------------------------------------------
armstrong
---------------------------------------------------
reverse a number
321
---------------------------------------------------
palindrome
---------------------------------------------------
vowels
2
---------------------------------------------------
consoants
3
---------------------------------------------------
vowels count 2
consoants count 3
---------------------------------------------------
perfect number
---------------------------------------------------
neon number
---------------------------------------------------
Strong number
---------------------------------------------------
Harshad number
---------------------------------------------------
Fibonacci Series
1
1
2
3
5

=== Code Execution Successful ===
"""