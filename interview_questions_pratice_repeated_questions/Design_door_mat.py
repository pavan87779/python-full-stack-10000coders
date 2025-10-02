N, M = map(int,input().split())
c = ".|."
for i in range(N//2):
    pattern = c*(2*i+1)
    print(pattern.center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in range(N//2-1,-1,-1):
    pattern = c* (2*i+1)
    print(pattern.center(M,'-'))
"""
Sample Input

9 27
Sample Output
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
