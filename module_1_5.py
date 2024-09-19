# Кортеж - это неизменяемая упорядоченная коллекция, которая может содержать изменяемые элементы
immutable_var = (1, 2)
print(immutable_var)
immutable_var = (1, 2) * 3 + (False, 1, 2, [3, 4.5])
immutable_var[9][1] = ['Year']
print(immutable_var)
print()

# Список - это изменяемая упорядоченная коллекция
mutable_list = [ 1, 2.5, False, [3, 4.7], 'False', (6, 7)]
print(mutable_list)
mutable_list.extend("smile")
mutable_list[3] = tuple(mutable_list[3]) * 3
mutable_list[5] = list(mutable_list[5])
mutable_list[4] = []
print(mutable_list)