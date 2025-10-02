"""
print this
enter n value:5
 * 
 *  * 
 *  *  * 
 *  *  *  * 
 *  *  *  *  * 
"""
n = int(input("enter n value:"))
for i in range(0,n):
    for j in range(0,i+1):
        print(" * ", end="")
    print()
    