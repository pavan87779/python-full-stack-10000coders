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
def copy_lst(lst):
    nlst = lst.copy()
    return nlst
l=[1, 2, 3]
print(l)
print("copied list: ",copy_lst(l))
"""
18
Copy List to Another List
[1, 2, 3]
copied list:  [1, 2, 3]
"""
print("--------------------------------------------------")
print(19)
print("Print All Prime Numbers in List")
l = [1, 2, 3, 4, 5]
def primenumbers_list(l):
    p = []
    for i in l:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        if count==2:
            p.append(i)
    return p
print(l)
print(primenumbers_list(l))
"""
19
Print All Prime Numbers in List
[1, 2, 3, 4, 5]
[2, 3, 5]
"""
print("--------------------------------------------------")
print(20)
print("Replace All Zeroes with a Given Number")
l=[0, 2, 0, 4]
def replace_zeros(l):
    for i in range(len(l)):
        if l[i] ==0:
            l[i] = -1
    return l
print(l)
print(replace_zeros(l))
"""
20
Replace All Zeroes with a Given Number
[0, 2, 0, 4]
[-1, 2, -1, 4]
"""
print("--------------------------------------------------")
print(21)
print("Check if All Elements Are Same")
l =[5, 5, 5, 5]
def check_elements(l):
    a = True
    for i in range(len(l)-1):
        if l[i]!=l[i+1]:
            a=False
            break
    return a
print(l)
print(check_elements(l))
"""
21
Check if All Elements Are Same
[5, 5, 5, 5]
True
"""
print("--------------------------------------------------")
print(22)
print("Find Frequency of All Elements")
l = [1,2,2,3,1]
def frequency_elements(l):
    s = set(l)
    d = dict()
    for i in s:
        d[i]=0
    for i in range(len(l)):
        if l[i] in l:
            d[l[i]]+=1
    return d
print(l)
print(frequency_elements(l))
"""
22
Find Frequency of All Elements
[1, 2, 2, 3, 1]
{1: 2, 2: 2, 3: 1}
"""
print("--------------------------------------------------")
print(23)
print("Flatten a Nested List")
l =[[1,2],[3,4]]
def flatten_list(l):
    n=[]
    for i in range(len(l)):
        for j in range(len(l[i])):
            n.append(l[i][j])
    return n
print(l)
print(flatten_list(l))
"""
23
Flatten a Nested List
[[1, 2], [3, 4]]
[1, 2, 3, 4]
"""
print("--------------------------------------------------")
print(24)
print("Split a List into Even and Odd Lists")
l=[1, 2, 3, 4, 5]
def even_odd(l):
    e=[]
    o=[]
    for i in l:
        if i %2==0:
            e.append(i)
        else:
            o.append(i)
    return f"Even: {e} Odd: {o}"
print(l)
print(even_odd(l))
"""
24
Split a List into Even and Odd Lists
[1, 2, 3, 4, 5]
Even: [2, 4] Odd: [1, 3, 5]
"""
print("--------------------------------------------------")
print(25)
print("Find Pair of Elements with Given Sum")
l =[1, 2, 3, 4]
s = 5
def pair_elements(l,s):
    a=[]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==s:
                a.append((l[i],l[j]))
    return list(a)
print(l)
print(s)
print(pair_elements(l,s))
"""
25
Find Pair of Elements with Given Sum
[1, 2, 3, 4]
5
[(1, 4), (2, 3)]
"""
print("--------------------------------------------------")
print(26)
print("Remove All Odd Numbers")
l=[1, 2, 3, 4, 5]
def remove_odd(l):
    for i in l:
        if i%2!=0:
            l.remove(i)
    return l
print(l)
print(remove_odd(l))
"""
26
Remove All Odd Numbers
[1, 2, 3, 4, 5]
[2, 4]
"""
print("--------------------------------------------------")
print(27)
print("Remove All Even Numbers")
l=[1, 2, 3, 4, 5]
def remove_even(l):
    for i in l:
        if i%2==0:
            l.remove(i)
    return l
print(l)
print(remove_even(l))
"""
27
Remove All Even Numbers
[1, 2, 3, 4, 5]
[1, 3, 5]
"""
print("--------------------------------------------------")
print(28)
print("Multiply All Elements by a Number")
l=[1, 2, 3]
n = 2
def multiply_lst(l,n):
    nl=[0]*len(l)
    for i in range(len(l)):
        nl[i] = l[i]*n
    return nl
print(l)
print(n)
print(multiply_lst(l,n))
"""
28
Multiply All Elements by a Number
[1, 2, 3]
2
[2, 4, 6]
"""
print("--------------------------------------------------")
print(29)
print("Find Difference Between Max and Min") 
l=[4, 2, 7, 1]
def min_max_diff(l):
    lar=float('-inf')
    small= float('inf')
    for i in range(len(l)):
        if l[i]>lar:
            lar=l[i]
    for j in range(len(l)):
        if l[j]<small:
            small=l[j]
    return lar-small
print(l)
print(min_max_diff(l))
"""
29
Find Difference Between Max and Min
[4, 2, 7, 1]
6
"""
print("--------------------------------------------------")
print(30)
print("Check if a List is Empty") 
l=[] 
def check_lst_empty(l):
    a=True
    if len(l)!=0:
        a=False
    return a
print(l)
print(check_lst_empty(l))
"""
30
Check if a List is Empty
[]
True
"""
print("--------------------------------------------------")
print(31)
print("Insert Element at Specific Index") 
l=[1, 2, 4]
element=3
ind=2
def insert_e_i(l,e,i):
    l.insert(i,e)
    return l
print(l)
print(insert_e_i(l,element,ind))
"""
31
Insert Element at Specific Index
[1, 2, 4]
[1, 2, 3, 4]
"""
print("--------------------------------------------------")
print(32)
print("Remove All Instances of a Value")
l=[1, 2, 2, 3]
x=2
def remove_instance(l,x):
    i=0
    while i<len(l):
        if l[i]==x:
            l.pop(i)
        else:
            i+=1
    return l
print(l)
print("remove ",x)
print(remove_instance(l,x))
"""
32
Remove All Instances of a Value
[1, 2, 2, 3]
remove  2
[1, 3]
"""
print("--------------------------------------------------")
print(33)
print("Get Index of an Element")
l=[10, 20, 30]
x=20
def index_of_element(l,x):
    ind=False
    for i in range(len(l)):
        if l[i]==x:
            ind = i
    return f"index of {x} is {ind}"
print(l)
print(x)
print(index_of_element(l,x))
"""
33
Get Index of an Element
[10, 20, 30]
20
index of 20 is 1
"""
print("--------------------------------------------------")
print(34)
print("Square All Elements in a List")
l=[1, 2, 3]
def square_elements(l):
    for i in range(len(l)):
        l[i] = l[i]**2
    return l
print(l)
print(square_elements(l))
"""
34
Square All Elements in a List
[1, 2, 3]
[1, 4, 9]
"""
print("--------------------------------------------------")
print(35)
print("Filter Out Negative Numbers")
l= [-1, 2, -3, 4]
def remove_neg_elements(l):
    n=[]
    for i in range(len(l)):
        if l[i]>=0:
            n.append(l[i])
    return n
print(l)
print(remove_neg_elements(l))
"""
35
Filter Out Negative Numbers
[-1, 2, -3, 4]
[2, 4]
"""
print("--------------------------------------------------")
print(36)
print("Get Elements Greater Than a Value")
l=[1, 5, 8, 3]
g=4
def greater_elements(l,g):
    s=[]
    for i in l:
        if i>g:
            s.append(i)
    return s
print(l)
print(g)
print(greater_elements(l,g))
"""
36
Get Elements Greater Than a Value
[1, 5, 8, 3]
4
[5, 8]
"""
print("--------------------------------------------------")
print(37)
print("Find Duplicates in List")
l=[1, 2, 2, 3, 3, 4]
def duplicates_in_list(l):
    d=[]
    for i in range(len(l)):
        count=0
        for j in range(len(l)):
            if l[i]==l[j]:
                count+=1
        if count>1:
            d.append(l[i])
    d=set(d)
    return list(d)
print(l)
print(duplicates_in_list(l))
"""
37
Find Duplicates in List
[1, 2, 2, 3, 3, 4]
[2, 3]
"""
print("--------------------------------------------------")
print(38)
print("Rotate List Elements Right")
l=[1, 2, 3, 4]
k=2
def rotate_list_element(l,k):
    k = k%len(l)
    new=[0]*len(l)
    for i in range(len(l)):
        new[(i+k)%len(l)] = l[i]
    return new
print(l)
print(f"rotate elements by {k}")
print(rotate_list_element(l,k))
"""
38
Rotate List Elements Right
[1, 2, 3, 4]
rotate elements by 2
[3, 4, 1, 2]
"""
print("--------------------------------------------------")
print(39)
print("Check If List Contains a Value")
l=[1, 2, 3]
x=2
def check_list_value(l,x):
    a = True
    if x not in l:
        a=False
    return a
print(l,x)
print(check_list_value(l,x))
"""
39
Check If List Contains a Value
[1, 2, 3] 2
True
"""
print("--------------------------------------------------")
print(40)
print("Chunk List into Smaller Lists")
l=[1, 2, 3, 4, 5, 6]
c=2
def l_into_smallerL(l, c):
    ch = []
    for i in range(0, len(l), c):   
        ch.append(l[i:i+c])     
    return ch

print(l, c)
print(l_into_smallerL(l, c))
"""
40
Chunk List into Smaller Lists
[1, 2, 3, 4, 5, 6] 2
[[1, 2], [3, 4], [5, 6]]
"""
            