print(1)
s = input("enter: ")
res=""
for i in s:
    if i!=" ":
        res+=i
print(res)
"""
enter: he llo wor ld
helloworld
"""
print("-------------------------------------------------")
print(2)

s = input("enter: ")
res=""
for i in range(len(s)-1,-1,-1):
    if s[i]!=" ":
        res+=s[i]
print(res)
"""
enter: hello
olleh
"""
print("-------------------------------------------------")
print(3)

print("reverse a string after removing spaces")
s = input("enter s: ")
res = ""
for i in range(len(s)-1,-1,-1):
    if s[i]!=" ":
        res+=s[i]
print(res)
"""
reverse a string after removing spaces
enter s: he llo world
dlrowolleh
"""
print("-------------------------------------------------")
print(4)

print("convert snake case to camel case")
s = input("enter a string: ")
res=""
result=""
index=[]
for i in range(len(s)):
    if s[i]=="_":
        index.append(i)

        
for i in range(len(s)):
    if (i-1) in index:
        res+=s[i].upper()
    else:
        res+=s[i]
for i in range(len(res)):
    if res[i]!="_":
        result+=res[i]
print(result)
"""
4
convert snake case to camel case
enter a string: my_variable_name
myVariableName
"""
print("-------------------------------------------------")
print(5)
print("convert snake case to pascal case")

res=""
result=""
index=[]
for i in range(len(s)):
    if s[i]=="_":
        index.append(i)

        
for i in range(len(s)):
    if i==0 or (i-1) in index:
        res+=s[i].upper()
    else:
        res+=s[i]
for i in range(len(res)):
    if res[i]!="_":
        result+=res[i]
print(result)
"""
5
convert snake case to pascal case
MyVariableName
"""
print("------------------------------------------------")
print(". Convert Camel Case to Snake Case")
print(6)
s= input("enter string: ") #myVariableName->my_variable_name
res=""
for i in range(len(s)):
    if s[i].islower():
        res+=s[i]
    elif s[i].isupper():
        res+="_"+s[i].lower()
print(res)
"""
. Convert Camel Case to Snake Case
6
enter string: myVariableName
my_variable_name
"""
print("--------------------------------------------------")
print(7)
print("Convert Camel Case to Pascal Case")
s = input("enter: ") #myVariable->MyVariable
res=""
for i in range(len(s)):
    if i==0:
        res+=s[i].upper()
    else:
        res+=s[i]
print(res)
"""
7
Convert Camel Case to Pascal Case
enter: myVariable
MyVariable
"""
print("--------------------------------------------------")
print(8)
print("Convert Pascal Case to Camel Case")
s = input("enter: ") #MyVariable -> myVariable
for i in range(len(s)):
    if i==0:
        res+=s[i].lower()
    else:
        res+=s[i]
print(res)
"""
8
Convert Pascal Case to Camel Case
enter: MyVariable
myVariable
"""
print("--------------------------------------------------")
print(9)
print("Convert Pascal Case to Snake Case")
s= input("enter: ") #MyVariable -> my_variable
res=""
for i in range(len(s)):
    if i==0:
        res+=s[i].lower()
    elif s[i].isupper():
        res+="_"+s[i]
    else:
        res+=s[i]
print(res)
"""
9
Convert Pascal Case to Snake Case
enter: MyVariable
my_Variable
"""
print("--------------------------------------------------")
print(10)
print("Convert Text to Camel Case") #hello world example -> helloWorldExample

s= input("enter: ")
res=""
count =0
for i in range(len(s)):
    if count==1:
        count=0
    elif s[i]==" ":
        res+=s[i+1].upper()
        count+=1
    else:
        res+=s[i]
print(res)
"""
enter: hello world example
helloWorldExample
"""
print("--------------------------------------------------")
print(11)
print("Convert Text to Snake Case")
s= input("enter s: ") #hello world example -> hello_world_example
res=""
for i in range(len(s)):
    if s[i]!=" ":
        res+=s[i]
    elif s[i]==" ":
        res+="_"
print(res)
"""
enter s: hello world example
hello_world_example
"""

print("--------------------------------------------------")
print(12)
print("Convert Text to Pascal Case") #hello world example -> HelloWorldExample
s= input("enter s: ")
res = ""
count=0
for i in range(len(s)):
    if count==1:
        count=0
    elif s[i]==" ":
        res+=s[i+1].upper()
        count+=1
    else:
        res+=s[i]
res[0].upper()
print(res)

"""
12
Convert Text to Pascal Case
enter s: hello world example
helloWorldExample
"""
print("--------------------------------------------------")
print(13)
print(" Swap Upper and Lower Case")  #HeLLo -> hEllO
s = input("enter s: ")
res=""
for i in s:
    if i.islower():
        res+=i.upper()
    elif i.isupper():
        res+=i.lower()
print(res)
"""
13
 Swap Upper and Lower Case
enter s: HeLLo
hEllO
"""
print("--------------------------------------------------")
print(14)
print("Separate Digits from Text")
s = input("enter s: ") #abc123d4 -> "1234"
res = ""
for i in s:
    if i.isdigit:
        res+=i
print(res)
"""
14
Separate Digits from Text
enter s: abc123d4
1234
"""
print("--------------------------------------------------")
print(15)
print("Print Uppercase, Lowercase, Digits, and Special Characters Separately")
s = input("enter s: ") 
#"Abc123!@#" 
#Uppercase: A
#Lowercase: b c
#Digits: 1 2 3
#Special Characters: ! @ #
uppercase = ""
lowercase=""
digits = ""
special = ""
for i in s:
    if i.isupper():
        uppercase+=" "+i
    elif i.islower():
        lowercase+=" "+i
    elif i.isdigit():
        digits+=" "+i
    else:
        special+=" "+i
print(f"UpperCase: {uppercase}")
print(f"LowerCase: {lowercase}")
print(f"Digits: {digits}")
print(f"Special Characters: {special}")

"""
15
Print Uppercase, Lowercase, Digits, and Special Characters Separately
enter s: Abc123!@#
UpperCase:  A
LowerCase:  b c
Digits:  1 2 3
Special Characters:  ! @ #
"""

print("--------------------------------------------------")
print(16)
print("Count of Uppercase, Lowercase, Digits, and Special Characters")
s = input("enter s: ")  #AbC@123x!
#Uppercase: 2
#Lowercase: 1
#Digits: 3
#Special Characters: 2
uppercase = 0
lowercase=0
digits = 0
special = 0
for i in s:
    if i.isupper():
        uppercase+=1
    elif i.islower():
        lowercase+=1
    elif i.isdigit():
        digits+=1
    else:
        special+=1
print(f"UpperCase: {uppercase}")
print(f"LowerCase: {lowercase}")
print(f"Digits: {digits}")
print(f"Special Characters: {special}")
"""
16
Count of Uppercase, Lowercase, Digits, and Special Characters
enter s: AbC@123x!
 UpperCase: 2
 LowerCase: 2
Digits: 3
Special Characters: 2
"""
print("--------------------------------------------------")
print(17)
print("Check Password Strength")
s = input("enter s: ")  #Pass123!-> Strong Password
upper=0
lower=0
digits=0
special = 0
for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    elif i.isdigit():
        digits+=1
    else:
        special+=1
if (upper & lower & digits & special) >=1:
    print("Strong Password")
else:
    print("Weak Password")
"""
17
Check Password Strength
enter s: Pass123!
Strong Password

Check Password Strength
enter s: pass123!
Weak Password

"""
print("--------------------------------------------------")
print(18)
print("Remove Duplicates in a Given Input")
s = input("enter s: ")  #aabbcc -> abc
res=""
for i in s:
    if i not in res:
        res+=i
print(res)
"""
18
Remove Duplicates in a Given Input
enter s: aabbc
abc
"""
print("--------------------------------------------------")
print(19)
print("Print Duplicates in a Given String")
s = input("enter s: ")  #aabbccde -> a b c
res=""
for i in range(len(s)):
    if s.count(s[i])>1 and s[i] not in res:
        res+=" "+s[i]
print(res)
"""
19
Print Duplicates in a Given String
enter s: aabbccde
abc

"""


print("--------------------------------------------------")
print(20)
print("Print Next Characters in a Given String")
s = input("enter s: ")  #abc -> bcd
res = ""
for i in s:
    res+=chr(ord(i)+1)
print(res)

"""
20
Print Next Characters in a Given String
enter s: abc
bcd
"""
