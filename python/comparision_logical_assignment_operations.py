a = 10
b = 30
c = 20

print(a>b) #false
print(b>c) #true
print(a>c) #false
print(a>=b) #false
print(b>=c) #true
print("-----------------------")
d = 40
e = 70
f = 3
print(d<=e) #true
print(e<=d) #false
print(d!=e) #true
print(e==d) #false
print("-----------------------")
#and or not
print((d<e) and (b>a)) #true
print((d>e) and (a<b)) #false
print((a>b) or (b>c)) #true
print(not a>b) #true
print("-----------------------")
#assignment operators
a+=b
print(a) #40
b-=c
print(b) #10
c *=d
print(c) #600
d/=c
print(d) #2
d//=e
print(d)

e%=a
print(e) #remainder

a**=f
print(a) #1000