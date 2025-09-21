s = input("enter name:")
age = int(input("enter age:"))
l = len(s)
#print(s[])
print("------------------")

half = l//2
firsthalf = len(s[:half])
secondhalf = len(s[half:])
print(firsthalf)
print(secondhalf)

print("---------------------")

print(firsthalf)
print(s[half:])
 
print("---------------------")
 
print(s,"is ", age, "years old")
 
print("---------------------")
a=s[0]
b=s[-1]
print(a+b+str(age))
print("---------------------")

print("*"*half+s[:half])
print("---------------------")

print(s[half:]+"*"*half)
print("---------------------")
a = age+5
print(s+" is "+str(a) +" years old")
print("---------------------")

print(s[::-1]+str(age))

"""
enter name:manoj
enter age:20
------------------
2
3
---------------------
2
noj
---------------------
manoj is  20 years old
---------------------
mj20
---------------------
**ma
---------------------
noj**
---------------------
manoj is 25 years old
---------------------
jonam20

=== Code Execution Successful ===
"""