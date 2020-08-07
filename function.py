from functools import reduce
my_list = [1,2,3]
your_list = [10,20,30]
def multiplt_by2(item):#map
    return item*2
def only_odd(item):#filter
    return item%2 != 0
def accumulator(acc,item): #reduce
    print(acc,item)
    return acc + item
print(list(map(multiplt_by2,my_list)))
print(list(filter(only_odd,my_list)))
print(list(zip(my_list,your_list)))#zip
print(reduce(accumulator,my_list))
print(my_list)
