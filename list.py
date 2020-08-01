my_list = [1, 2, 3, True, 'Piyush' ]
print(len(my_list))
print(my_list.count('Piyush'))
print(my_list[3])
print(my_list[1:3])
print(my_list[: :-1])
print(my_list * 2)
print(my_list + [100])
my_list.append(200)
print(my_list)
my_list.extend([300,'messi'])
print(my_list)
my_list.insert(2,'hello')
print(my_list)
new_list = my_list
print(new_list)
my_list.pop(2)
print(my_list)
my_list.remove('Piyush')
print(my_list)
list = [6,3,1,8]
list.sort()
print(list)
print(list[ : :-1])
matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]
print(matrix[0][2])
print(1 in my_list)
