s = input("enter: ")
rev = s[::-1]
res=""
index=[]
for i in range(len(rev)):
    if rev[i]!=" ":
        res+=rev[i]
for i in range(len(s)):
    if s[i]==" ":
        index.append(i)
for i in index:
    res = res[:i]+" "+res[i:]
print(res)

"""
enter: my name is a java
av ajas ie m anym
"""