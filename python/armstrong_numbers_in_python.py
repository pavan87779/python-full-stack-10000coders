m=10
n=30
for i in range(m,n+1):
    if i>1:
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1
                break
        if c==0:
            print(i)
"""
11
13
17
19
23
29
"""
print("-------------------------------------------------------")
m = 1
n = 10
count = 0

for i in range(m, n + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            count += 1

print("Count of Prime Numbers:", count)
#4
print("-------------------------------------------------------")
print("all armstrong number")
m = 1
n = 500

for i in range(m, n + 1):
    num = i
    digits = len(str(num))
    res = 0
    while num > 0:
        d = num % 10
        res += d ** digits
        num //= 10
    if res == i:
        print(i, end=" ")

print("-------------------------------------------------------")
m = 10
n = 25
print("first prime number")
for i in range(m, n + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            print("First Prime Number:", i)
            break
print("-------------------------------------------------------")
m = 10
n = 25
last_prime = -1
print("last prime number")
for i in range(m, n + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            last_prime = i

if last_prime != -1:
    print("Last Prime Number:", last_prime)
else:
    print("No prime numbers in range")
print("-------------------------------------------------------")
name = "Krishna"
vowels = "aeiouAEIOU"

for ch in name:
    if ch in vowels:
        print("First vowel:", ch)
        break
else:
    print("No vowel found")
print("-------------------------------------------------------")
name = "Ramakrishna"
vowels = "aeiouAEIOU"

last_vowel = None
for ch in name:
    if ch in vowels:
        last_vowel = ch

if last_vowel:
    print("Last vowel:", last_vowel)
else:
    print("No vowel found")
print("---------------------------------------------------------")
n = 10
for i in range(1, n + 1):
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()
    
print("---------------------------------------------------------")
    
n = 10
for i in range(1, n + 1):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()
print("-------------------------------------------------------")
m = 1
n = 10
prime_count = 0
composite_count = 0

for i in range(m, n + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                composite_count += 1
                break
        else:
            prime_count += 1

print("Prime:", prime_count)
print("Composite:", composite_count)


"""
11
13
17
19
23
29
-------------------------------------------------------
Count of Prime Numbers: 4
-------------------------------------------------------
all armstrong number
1 2 3 4 5 6 7 8 9 153 370 371 407 
-------------------------------------------------------
first prime number
First Prime Number: 11
-------------------------------------------------------
last prime number
Last Prime Number: 23
-------------------------------------------------------
First vowel: i
-------------------------------------------------------
Last vowel: a
---------------------------------------------------------
2 4 6 8 10 
---------------------------------------------------------
1 3 5 7 9 
-------------------------------------------------------
Prime: 4
Composite: 5

=== Code Execution Successful ===
"""