"""📜 List Operations Challenge (Python)
Problem Statement

You are given an initially empty list. Your task is to perform a series of operations on this list based on user input commands.

The commands you can perform are:

Command	Description
insert i e	Insert integer e at position i.
print	Print the current list.
remove e	Delete the first occurrence of integer e.
append e	Add integer e to the end of the list.
sort	Sort the list in ascending order.
pop	Remove the last element from the list.
reverse	Reverse the list.
Input Format

The first line contains an integer N, the number of commands.

The next N lines each contain one command.

Output Format

For each print command, print the list on a new line.

Constraints

0 <= N <= 100

The elements added to the list will be integers.

Sample Input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Sample Output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
if __name__ == '__main__':
    N = int(input())

my_list = []

for _ in range(N):
    command = input().split()
    if command[0] == "print":
        print(my_list)
    elif command[0] == "sort":
        my_list.sort()
    elif command[0] == "pop":
        my_list.pop()
    elif command[0] == "reverse":
        my_list.reverse()
    elif command[0] == "insert":
        my_list.insert(int(command[1]),int(command[2]))
    elif command[0] == "remove":
        my_list.remove(int(command[1]))
    elif command[0] == "append":
        my_list.append(int(command[1]))
