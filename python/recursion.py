print(1)
print("Add an Element to a List")
def list_add(lst,n):
    lst.append(n)
    return lst
l = [1,2,3]
a = 4
print(l)
print(a)
print(list_add(l,a))
"""
1
Add an Element to a List
[1, 2, 3]
4
[1, 2, 3, 4]
"""
print("--------------------------------------------------")
print(2)
print("Remove an Element from a List")
def list_remove(lst,n):
    lst.remove(n)
    return lst
l = [1,2,3,4]
a = 3
print(l)
print(a)
print(list_remove(l,a))
"""
2
Remove an Element from a List
[1, 2, 3, 4]
3
[1, 2, 4]
"""
print("--------------------------------------------------")
print(3)
print("Find Maximum in List")
def list_max(lst):
    return max(lst)
l = [4,7,1,9]
print(l)
print(list_max(l))
"""
3
Find Maximum in List
[4, 7, 1, 9]
9
"""
print("--------------------------------------------------")
print(4)
print("Find Minimum in List")
def list_min(lst):
    return min(lst)
l = [4,7,1,9]
print(l)
print(list_min(l))
"""
4
Find Minimum in List
[4, 7, 1, 9]
1
"""
print("--------------------------------------------------")
print(5)
print("Sum of All Elements in List")
def list_sum(lst):
    sum=0
    for i in lst:
        sum+=i
    return sum
l = [1,2,3]
print(l)
print(list_sum(l))
"""
5
Sum of All Elements in List
[1, 2, 3]
6
"""
print("--------------------------------------------------")
print(6)
print("Count Occurrence of an Element")
def list_ele_count(lst,n):
    count = 0
    for i in lst:
        if i ==n:
            count+=1
    return count
l = [1,2,2,3,2]
val = 2
print(l,val)
print(list_ele_count(l,val))
"""
6
Count Occurrence of an Element
[1, 2, 2, 3, 2] 2
3
"""
print("--------------------------------------------------")
print(7)
print("Reverse a List")
def list_reverse(l):
    rev=[]
    for  i in range(len(l)-1,-1,-1):
        rev.append(l[i])
    return rev
l = [1,2,3]
print(l)
print(list_reverse(l))
"""
7
Reverse a List
[1, 2, 3]
[3, 2, 1]
"""
print("--------------------------------------------------")
print(8)
print("Sort a List")
l= [4, 1, 3, 2] 
def list_sort(lst):
    for i in range(len(lst)):
        for j  in  range(len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j+1],lst[j] = lst[j],lst[j+1]
    return lst
print(l)
print(list_sort(l))
"""
8
Sort a List
[4, 1, 3, 2]
[1, 2, 3, 4]
"""
print("--------------------------------------------------")
print(9)
print("Remove Duplicates from a List")
l=[1, 2, 2, 3]
def remove_duplicates(l):
    rev=[]
    for i in l:
        if i not in rev:
            rev.append(i)
    return rev
print(l)
print(remove_duplicates(l))
"""
9
Remove Duplicates from a List
[1, 2, 2, 3]
[1, 2, 3]
"""
print("--------------------------------------------------")
print(10)
print("Merge Two Lists")
a=[1, 2]
b=[3, 4]
def merge_list(l1,l2):
    return l1+l2
print(a,b)
print(merge_list(a,b))
"""
10
Merge Two Lists
[1, 2] [3, 4]
[1, 2, 3, 4]
"""
print("--------------------------------------------------")
print(11)
print("Find Common Elements in Two Lists")
a=[1, 2, 3]
b=[2, 3, 4]
def common_lst(l1,l2):
    res = []
    for i in l1:
        if i in l2:
            res.append(i)
    return res
print(a,b)
print(common_lst(a,b))
"""
11
Find Common Elements in Two Lists
[1, 2, 3] [2, 3, 4]
[2, 3]
"""
print("--------------------------------------------------")
print(12)
print("Print Even Numbers in a List")
l=[1, 2, 3, 4] 
def evenInList(lst):
    res=[]
    for i in lst:
        if i %2==0:
            res.append(i)
    return res
print(l)
print(evenInList(l))
"""
12
Print Even Numbers in a List
[1, 2, 3, 4]
[2, 4]
"""
print("--------------------------------------------------")
print(13)
print("Print Odd Numbers in a List")
l=[1, 2, 3, 4] 
def oddInList(lst):
    res=[]
    for i in lst:
        if i %2!=0:
            res.append(i)
    return res
print(l)
print(oddInList(l))
"""
13
Print Odd Numbers in a List
[1, 2, 3, 4]
[1, 3]
"""
print("--------------------------------------------------")
print(14)
print("Check if List is Palindrome")
l = [1,2,1]
def palindrome_lst(lst):
    res=[]
    for i in range(len(l)-1,-1,-1):
        res.append(lst[i])
    if lst==res:
        return True
print(l)
print(palindrome_lst(l))
"""
14
Check if List is Palindrome
[1, 2, 1]
True
"""
print("--------------------------------------------------")
print(15)
print("Count Positive, Negative, Zero")
l=[0, -1, 2, -3, 4] 
def ve_Nve_zero(lst):
    p =0
    n=0
    z=0
    for i in lst:
        if i >0:
            p+=1
        elif i==0:
            z+=1
        elif i<0:
            n+=1
        else:
            pass
    return  f"Positive: {p}, Negative: {n}, Zero: {z}"
print(l)
print(ve_Nve_zero(l))
"""
15
Count Positive, Negative, Zero
[0, -1, 2, -3, 4]
Positive: 2, Negative: 2, Zero: 1
"""
print("--------------------------------------------------")
print(16)
print("Find Second Largest Number in List")
l= [1, 3, 4, 5, 0]
def second_largest(lst):
    lar= float("-inf")
    sec= float("-inf")
    for i in lst:
        if i>lar:
            lar=i
    for j in lst:
        if j >sec and j<lar:
            sec=j
    return sec
print(l)
print(second_largest(l))
"""
16
Find Second Largest Number in List
[1, 3, 4, 5, 0]
4
"""
print("--------------------------------------------------")
print(17)
print("Find Second Smallest Number in List")
l=[5, 1, 4, 2, 3]
def secondSmallest(lst):
    fs=float("inf")
    ss=float("inf")
    for i in lst:
        if i<fs:
            fs=i
    for j in lst:
        if j <ss  and j >fs:
            ss=j
    return ss
print(l)
print(secondSmallest(l))
"""
17
Find Second Smallest Number in List
[5, 1, 4, 2, 3]
2
"""
print("--------------------------------------------------")
print(18)
print("Copy List to Another List")
def
        