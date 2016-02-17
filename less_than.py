a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

less_than = []
for x in a:
    if x < 5:
        less_than.append(x)

#print(less_than)

xxy = [num for num in a if num < 5]
print(xxy)

#The following is for Extra 3

user_num = int(input("What number should be the high number?\n"))
user_list = []
for i in a:
    if i < user_num:
        user_list.append(i)

print(user_list)
