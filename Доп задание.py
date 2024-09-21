# Способ 1
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
for i in range(len(grades)): grades[i] = sum(grades[i]) / len(grades[i])
students = sorted(list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))
print(dict(zip(students, grades)))

# Способ 2
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = sorted(list({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}))
s0 = []
for i in range(len(students)):
    s = []
    grades[i] = sum(grades[i]) / len(grades[i])
    s.append(students[i])
    s.append(grades[i])
    s0.append(s)
print(dict(s0))

