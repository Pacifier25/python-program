new_list = [1,2,3,3,3,4,4,5,6,1]
print(set(new_list))
print(new_list.count(3))
set1 = {1,2,3}
set2 = {3,5,6}
set = set1.union(set2)
print(set)
set = set1.intersection(set2)
print(set)
print(set1.issubset(set2))
set1.remove(1)
print(set1)
new_list.append(100)
print(new_list)
