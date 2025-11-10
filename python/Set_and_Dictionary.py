print(1)
print("Add Element to a Set")
s={1,2,3}
s.add(4)
print(s)
"""
1
Add Element to a Set
{1, 2, 3, 4}
"""
print("----------------------------------------------------------")
print(2)
print("Remove Element from Set")
s={1,2,3}
s.remove(3)
print(s)
"""
2
Remove Element from Set
{1, 2}
"""
print("----------------------------------------------------")
print(3)
print("Union of Two Sets")
s1 = {1,2}
s2={2,3}
print(s1.union(s2))
"""
3
Union of Two Sets
{1, 2, 3}
"""
print("----------------------------------------------------")
print(4)
print("Intersection of Sets")
s1={1,2}
s2={2,3}
print(s1.intersection(s2))
"""
4
Intersection of Sets
{2}
"""
print("----------------------------------------------------")
print(5)
print("Difference of Sets")
s1= {1,2,3}
s2={2,3}
print(s1-s2)
"""
5
Difference of Sets
{1}
"""
print("----------------------------------------------------")
print(6)
print("Check Subset")
s1={1,2,3}
s2={2,3}
print(s2.issubset(s1))
"""
6
Check Subset
True
"""
print("----------------------------------------------------")
print(7)
print("Set Length")
s1={1,2,3}
print(len(s1))
"""
7
Set Length
3
"""
print("----------------------------------------------------")
print(8)
print("Clear a Set")
s1 = {1,2,3,4}
print(s1.clear())
"""
8
Clear a Set
None

"""
print("----------------------------------------------------")
print(9)
print("Symmetric Difference")
s1={1,2,3}
s2={2,3,4}
print(s1.symmetric_difference(s2))
"""
9
Symmetric Difference
{1, 4}
"""
print("----------------------------------------------------")
print(10)
print("Convert List to Set")
s1 = [1,2,2,3]
print(set(s1))
"""
10
Convert List to Set
{1, 2, 3}
"""
print("---------------------------------------------")
print("Dictionary Based  Questions")
print(11)
print("Create a Dictionary from Two Lists")
l1=["a","b"]
l2=[1,2]
dic = dict(zip(l1,l2))
print(dic)
"""
Dictionary Based  Questions
11
Create a Dictionary from Two Lists
{'a': 1, 'b': 2}
"""
print("--------------------------------------------------------")
print(12)
print("Update Dictionary Value")
d={"a":1}
d["a"]=2
print(d)
"""
12
Update Dictionary Value
{'a': 2}
"""
print("--------------------------------------------------------")
print(13)
print("Remove Key from Dictionary")
d={"a":1,"b":2}
d.pop("b")
print(d)
"""
13
Remove Key from Dictionary
{'a': 1}
"""
print("--------------------------------------------------------")
print(14)
print("Check Key Existence")
dic={"x":1}
key="x"
if key in dic:
    print(True)
else:
    print(False)
"""
14
Check Key Existence
True
"""
print("--------------------------------------------------------")
print(15)
print("Iterate Over Dictionary")
dic = {"a":10,"b":20}
for key,value in dic.items():
    print(key, value)
"""
15
Iterate Over Dictionary
a 10
b 20
"""
print("--------------------------------------------------------")
print(16)
print("Dictionary Length")
dic= {"x":1,"y":2}
print(len(dic))
"""
16
Dictionary Length
2
"""
print("--------------------------------------------------------")
print(17)
print("Merge Two Dictionaries")
dic1={"a":1}
dic2={"b":2}
dic1.update(dic2)
print(dic1)
"""
17
Merge Two Dictionaries
{'a': 1, 'b': 2}
"""
print("--------------------------------------------------------")
print(18)
print("Get Value with Default")
dic ={"a":1}
print(dic.get("b",0))
"""
18
Get Value with Default
0
"""
print("--------------------------------------------------------")
print(19)
print("Count Frequency of Elements")
lst=[1,2,2,3]
dic=dict()
for i in lst:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
"""
19
Count Frequency of Elements
{1: 1, 2: 2, 3: 1}
"""
print("--------------------------------------------------------")
print(20)
print("Invert a Dictionary")
dic = {"a":1,"b":2}
dic1=dict()
for key,value in dic.items():
    dic1[value]=key
print(dic1)
"""
20
Invert a Dictionary
{1: 'a', 2: 'b'}
"""
print("--------------------------------------------------------")
print(21)
print("Find Key with Maximum Value")
dic = {"a":10,"b":20,"c":15}
k=[]
v=[]
for key,value in  dic.items():
    k.append(key)
    v.append(value)
a=0
lar=float('-inf')
for i in range(len(v)):
    if v[i]>lar:
        lar=v[i]
        a=i
        
print(a)
print(k[a])
"""
21
Find Key with Maximum Value
1
b
"""
print("--------------------------------------------------------")
print(22)
print("Sort Dictionary by Values")
dic = {"a":3,"b":2,"c":1}
dic1 = dict()
lst = list(dic.items())
for i in range(len(dic)):
    for j in range(len(dic)-1):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
"""
22
Sort Dictionary by Values
[('a', 3), ('b', 2), ('c', 1)]
"""
print("--------------------------------------------------------")
print(23)
print("Create Dictionary of Squares")
lst=[]
sqlst=[]
for i in range(1,4):
    lst.append(i)
    sqlst.append(i**2)
dic= dict(zip(lst,sqlst))
print(dic)
"""
23
Create Dictionary of Squares
{1: 1, 2: 4, 3: 9}
"""
print("--------------------------------------------------------")
print(24)
print(" Filter Dictionary by Value Condition")
dic= {"a": 10, "b": 5, "c": 15}
threshold = 10
dic1 = {}

for key, value in dic.items():
    if value > threshold:
        dic1[key] = value

print(dic1) 
"""
24
 Filter Dictionary by Value Condition
{'c': 15}
"""
print("--------------------------------------------------------")
print(25)
print("Combine Values of Duplicate Keys")
dic1={"a": 1, "b": 2}
dic2=  {"a": 3, "c": 4}
res={}
for key , value in dic1.items():
    res[key]= value
for key ,value in dic2.items():
    if key in res:
        res[key]= res[key]+value
    else:
        res[key]=value
print(res)
"""
25
Combine Values of Duplicate Keys
{'a': 4, 'b': 2, 'c': 4}
"""
print("--------------------------------------------------------")
print(26)
print("Count Word Frequency in Sentence")
text = "apple banana apple"
words = text.split()
dic = {}

for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print(dic)
"""
26
Count Word Frequency in Sentence
{'apple': 2, 'banana': 1}
{'apple': 2, 'banana': 1}
"""
print("--------------------------------------------------------")
print(27)
print("Remove Duplicate Values from Dictionary")
dic = {"a": 1, "b": 2, "c": 1}
new_dic = {}
seen = []

for key, value in dic.items():
    if value not in seen:
        seen.append(value)
        new_dic[key] = value

print(new_dic)
"""
27
Remove Duplicate Values from Dictionary
{'a': 1, 'b': 2}
"""
print("--------------------------------------------------------")
print(28)
print("Find Common Keys in Two Dictionaries")
dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}
common = []

for key in dic1:
    if key in dic2:
        common.append(key)

print(common)
"""
28
Find Common Keys in Two Dictionaries
['b']
"""
print("--------------------------------------------------------")
print(29)
print("Swap Keys and Values Safely")
dic = {"x": 1, "y": 2}
new_dic = {}
unique = True

for key, value in dic.items():
    if value not in new_dic:
        new_dic[value] = key
    else:
        unique = False
        print("Duplicate values found. Cannot swap safely.")
        break

if unique:
    print(new_dic)
"""
29
Swap Keys and Values Safely
{1: 'x', 2: 'y'}
"""
print("--------------------------------------------------------")
print(30)
print("Delete Items by Value")
dic = {"a": 1, "b": 2, "c": 1}
value_to_remove = 1
new_dic = {}

for key, value in dic.items():
    if value != value_to_remove:
        new_dic[key] = value

print(new_dic)
"""
30
Delete Items by Value
{'b': 2}

"""