my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Write your code here.
temp_list = []

for n in my_list:
    if n not in temp_list:
        temp_list.append(n)
my_list = temp_list

#
print("The list with unique elements only:")
print(my_list)

