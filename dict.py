my_dict ={
'name': 'Piyush Bist',
'age': 21,
'magic_power': False
}
print(len(my_dict))
print(list(my_dict.items()))
print(tuple(my_dict.keys()))
print(list(my_dict.values()))
print(my_dict.get('age'))
del my_dict['name']
print(my_dict)
my_dict['favaurite_snack'] = 'grapes'
print(my_dict)
my_dict.update({'cool':True})
print(my_dict)
new_dict = my_dict
print(my_dict)
my_dict.update({'cool':False})
print(my_dict)
