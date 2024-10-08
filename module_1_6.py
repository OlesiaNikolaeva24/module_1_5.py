# Работа со словарями
my_dict = {'Olesia': 2000, 'Alisa': 2001, 'Leta': 2002}
print('Dictionary:', my_dict)
print('Existing value:', my_dict.get("Olesia"))
print('Not existing value:', my_dict.get("?"))
my_dict.update({'Artur': '19XX', 'Sense': '19XX'})
a = my_dict.pop('Alisa')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print()
# Работа с множествами
my_set = {1, 2, 2, 2, 13, 13, 44, True, (1, 2)}
print('Set:', my_set)
my_set.add('Terra')
my_set.add('***')
my_set.update('Terra', '***')
my_set.discard((1,2))
print('Modified set:', my_set)