print("prime number from range m to n.")
m = int(input("enter m value: "))
n = int(input("enter n value: "))
for i in range(m,n+1):
    count=1
    for j in range(2,i):
        if i%j==0:
            count+=1
            break
    if count==1:
        print(f"{i} is prime number")
    else:
        print(f"{i} is not prime number")
"""
enter m value: 10
enter n value: 30
10 is not prime number
11 is prime number
12 is not prime number
13 is prime number
14 is not prime number
15 is not prime number
16 is not prime number
17 is prime number
18 is not prime number
19 is prime number
20 is not prime number
21 is not prime number
22 is not prime number
23 is prime number
24 is not prime number
25 is not prime number
26 is not prime number
27 is not prime number
28 is not prime number
29 is prime number
30 is not prime number
"""
print("-----------------------------------------")
print("prime number from range m to n.")
m = int(input("enter m value: "))
n = int(input("enter n value: "))
p_count=0
for i in range(m,n+1):
    count=1
    for j in range(2,i):
        if i%j==0:
            count+=1
            break
    if count==1:
        p_count+=1
    else:
        
        pass
print(f"count of prime from {m} to {n} is {p_count}")
print("-----------------------------------------")

print("all armstrong numbers in a range")
m = int(input("enter m armstrong: "))
n = int(input("enter n armstrong: "))
for i in range(m,n+1):
    temp = i
    res=0
    for j in range(len(str(i))):
        a=i%10
        res+=a**3 
        i//=10
    if temp==res:
        print(temp)
    else:
        pass
"""
all armstrong numbers in a range
enter m armstrong: 1
enter n armstrong: 500
1
153
370
371
407
"""
print("-----------------------------------------")
print("first prime numbers from m to n")
m = int(input("enter m armstrong: "))
n = int(input("enter n armstrong: "))
for i in range(m,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
        break
#11
print("-----------------------------------------")
for i in range(n,m-1,-1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)
        break
#23
print("-----------------------------------------")
print("first vowel in string")
s = input("enter string: ")
vowels="aeiouAEIOU"
for i in s:
    if i in vowels:
        print(i)
        break
#a
print("-----------------------------------------")
print("last vowel in python")
for i in s[::-1]:
    if i in vowels:
        print(i)
        break
print("-----------------------------------------")
print("all even number using continue")
n = int(input("enter n no: "))
for i in range(1,n+1):
    if i%2!=0:
        continue
    print(i)
"""
2
4
6
8
10
"""
print("-----------------------------------------")
print("all odd number using continue")
for i in range(1,n+1):
    if i%2==0:
        continue
    print(i)
"""
all odd number using continue
1
3
5
7
9

"""
print("-----------------------------------------")
print("count prime and composite number from m to n")
m = int(input("enter m: "))
n = int(input("enter n: "))
pc=0
cc=0
for i in range(m,n):
    pcount =0
    for j in range(1,i+1):
        if i%j==0:
            pcount+=1
    if pcount==2:
        pc+=1
    elif pcount>2:
        cc+=1
print(f"prime count{pc} consonent counts {cc}")
"""
enter m: 1
enter n: 10
prime count4 consonent counts 4
"""