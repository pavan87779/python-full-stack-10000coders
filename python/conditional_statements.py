import math
n = int(input("enter:"))
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
vote = int(input("vote age:"))


if n%2==0:
	print("even number")
else:
	print("odd number")

print("----------------------------------")

if n%5==0 and n%10 !=0:
	print("satisfy")
else:
	print("not satisfy")


print("----------------------------------")


if a>b:
	print("Biggest",a)
else:
	print("Biggest",b)
print("----------------------------------")

if a<b:
	print("Smallest",a)
else:
	print("Smallest",b)
print("----------------------------------")

if a%2==0 and b%3==0 and c%6==0:
	print("Satisfy")
else:
	print("not satisfy")

print("----------------------------------")
if vote>=18:
	print("Eligible to vote")
else:
	print("not eligible to vote")
print("----------------------------------")
math = int(input("m:"))
phy = int(input("p:"))
chem = int(input("c:"))

if math >= 35 and phy >= 35 and chem>=35:
	print("pass")
else:
	print("fail")
print("----------------------------------")

if math>=35 or phy >= 35 or chem>= 35:
	print("pass")
else:
	print("fail")
print("----------------------------------")

if (math >=35 and phy>=35) or (phy>=35 and chem>=35) or (math>=35 and chem>=35):
	print("pass")
else:
	print("fail")
print("----------------------------------")
if a<b and a<c:
	print("smallest is ",a)
elif b<a and b<c:
	print("smallest is ",b)
else:
	print("smallest is ",c)
print("----------------------------------")

sqroot= int(input("root:"))
sq = int(math.sqrt(sqroot))
if sq*sq == sqroot:
	print("perfect square")
else:
	print("not perfect square")








