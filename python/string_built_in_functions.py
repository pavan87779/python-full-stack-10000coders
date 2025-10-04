print("SwapCase")
s = "PyThOn"
result = ""

for ch in s:
    if 'a' <= ch <= 'z':        
        result += chr(ord(ch) - 32)
    elif 'A' <= ch <= 'Z':      
        result += chr(ord(ch) + 32)
    else:
        result += ch

print(result)
"""
pYtHoN
"""
print("--------------------------------------------------")

print("Strip")
s = "    Hello World   "
chars = " \t\n\r\f\v"   
start = 0
end = len(s) - 1

while start <= end and s[start] in chars:
    start += 1
while end >= start and s[end] in chars:
    end -= 1

result = ""
for i in range(start, end + 1):
    result += s[i]

print(result)
"""
Hello World
"""
print("--------------------------------------------------")
print("replace")
s = "I love Python because Python is fun"
old = "Python"
new = "Java"
result = ""
i = 0

while i < len(s):
    match = True

    # check if substring matches
    for j in range(len(old)):
        if i + j >= len(s) or s[i + j] != old[j]:
            match = False
            break

    if match:
        result += new
        i += len(old)
    else:
        result += s[i]
        i += 1

print(result)
"""
I love Java because Java is fun
"""