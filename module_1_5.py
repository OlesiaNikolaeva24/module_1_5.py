# Кортеж - это неизменяемая упорядоченная коллекция, которая может содержать изменяемые элементы
immutable_var = (1, 2)
print("Исходный кортеж: ", immutable_var)
immutable_var = (1, 2) * 3 + (False, -1, 2, [3, 4.5])
immutable_var[9][1] = ['Year']
print("Обновленный кортеж: ", immutable_var)
print()

# Список - это изменяемая упорядоченная коллекция
mutable_list = [ 1, 2.5, False, [-3, 4.7], 'False', (6, 7)]
print("Исходный список: ", mutable_list)
mutable_list.extend("smile")
mutable_list[3] = tuple(mutable_list[3]) * 3
mutable_list[5] = list(mutable_list[5])
a = mutable_list.pop(2)
mutable_list.remove(2.5)
mutable_list.append(a)
print("Обновленный список: ", mutable_list)
print()

# Кортеж экономит память
print("Вес кортежа:", immutable_var.__sizeof__(), "             Вес списка:", mutable_list.__sizeof__())
print("Вес списка из кортежа:", list(immutable_var).__sizeof__(), "   Вес кортежа из списка:", tuple(mutable_list).__sizeof__())