set_a = {2,4,8,2,1,9,5,10}
set_b = {3,13,2,5,3}
print(set_a)
print(set_b)
print(set_a.union(set_b))
print(set_a.intersection(set_b))
print(set_a-set_b)
print(set_a.isdisjoint(set_b))
set_a.add("pavan")
set_a.add((4,5))
print(set_a.remove(9))
print(set_a)
"""
{1, 2, 4, 5, 8, 9, 10}
{13, 2, 3, 5}
{1, 2, 3, 4, 5, 8, 9, 10, 13}
{2, 5}
{1, 4, 8, 9, 10}
False
None
{1, 2, 4, 5, 8, 10, (4, 5), 'pavan'}

"""