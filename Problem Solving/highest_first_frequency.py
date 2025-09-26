s = "aaaaabbbbbccccc"
res = ""
c = 0
for i in s:
    if s.count(i)>c:
        c = s.count(i)
        res = i
print(res,":",c)

"""
a : 5

=== Code Execution Successful ===
"""