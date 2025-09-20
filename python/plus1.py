def plus1(l1):
    s= ""
    s2 =""
    for i in range(len(l1[0])):
        s+=str(l1[0][i])
        s2 +=str(l1[1][i])
        n = int(s)+1
        n2 = int(s2)+1
    n = list(str(n) )
    n2 = list(str(n2))
    op = list([n,n2])
    
    print(s)
    print(n)
    print(n2)
    print(op)
    return op
    
lst = [[1,3,0],[9,9,9]]
print(plus1(lst))