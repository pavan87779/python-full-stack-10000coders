import copy
original_list= [1,2,3,4,5]

shallow_copy_list = copy.copy(original_list)

deep_copy_list = copy.deepcopy(original_list)

original_list[0] = 0 #changing

shallow_copy_list[1] = 1 #changing

print("original list: ",original_list) #affecting
print("shallow copy list: ",shallow_copy_list) #affecting
print("deep copy list: ",deep_copy_list)


"""
output:

original list:  [0, 2, 3, 4, 5]
shallow copy list:  [1, 1, 3, 4, 5]
deep copy list:  [1, 2, 3, 4, 5]

=== Code Execution Successful ===
"""