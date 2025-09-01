my_tuple = ("apple", "banana", "cherry")
num = (10,20,30,20,40,20,60,20)

for i in my_tuple:
    print(i)

new_tuple = my_tuple+("orange",)
print(new_tuple)
print(num.index(30))
print(num.count(20))

my_tuple +=("mango",)
print(my_tuple)

find = 60
for i in range(0, len(num)):
    if (find== num[i]):
        print("the index of tuple is :", i)
        break
    else:
        print(-1)
count =0
for i in range(0,len(num)):
    if (20==num[i]):
        count+=1
    
print(count)
   

"""
apple
banana
cherry
('apple', 'banana', 'cherry', 'orange')
2
4
('apple', 'banana', 'cherry', 'mango')
-1
-1
-1
-1
-1
-1
the index of tuple is : 6
4
"""