grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# journal = sorted(students)  # перевожу множество в упорядоченный по алфавиту список
average_score = [(sum(grades[i]) / len(grades[i])) for i in range (len(grades))]  # список средних оценок учеников
# diary = {journal[j] : average_score[j] for j in range (len(journal))}
diary = {sorted(students)[j] : average_score[j] for j in range (len(students))}
print(diary)