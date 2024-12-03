grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sorted_students = sorted(students)
sorted_students_list=list(sorted_students)
#print(sorted_students_list)
total1= (float(sum(grades[0])))/len(grades[0])
total2= (float(sum(grades[1])))/len(grades[1])
total3= (float(sum(grades[2])))/len(grades[2])
total4= (float(sum(grades[3])))/len(grades[3])
total5= (float(sum(grades[4])))/len(grades[4])
new_grades = [total1, total2, total3, total4, total5]
evaluations = {(sorted_students_list[0]):total1,(sorted_students_list[1]):total2,(sorted_students_list[2]):total3,(sorted_students_list[3]):total4,(sorted_students_list[4]):total5}
print(evaluations)












