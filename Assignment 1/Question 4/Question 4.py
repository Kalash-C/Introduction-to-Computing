# Displaying marks in a sorted way in a list
marks1=int(input('Enter marks of student 1: '))
marks2=int(input('Enter marks of student 2: '))
marks3=int(input('Enter marks of student 3: '))
marks4=int(input('Enter marks of student 4: '))
marks5=int(input('Enter marks of student 5: '))
list=[marks1, marks2, marks3, marks4, marks5]
list.sort(reverse=True)
print(list)