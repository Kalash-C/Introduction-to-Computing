#Question 1
# Finding Average of 3 Numbers
no1=int(input('Enter Number 1: '))
no2=int(input('Enter Number 2: '))
no3=int(input('Enter Number 3: '))
Average=(no1+no2+no3)/3
print('Average of 3 Number: ',Average)

#Question 2
# Program For Computing a Person's Tax

gross=float(input('Gross Income is: '))     #Gross Income
strdd=float(10000)                            #Standard Deduction
nd=float(input('Number of Dependents: '))     #Number of Dependents
dpntd=float(3000)                             #Dependent Deduction
txblei=gross-strdd-(dpntd*nd)                #Taxable Income
tax=txblei*0.2
if txblei<0:
    txblei=0
if tax<0:
    tax=0
print('Taxable Income is: ',txblei)
print('Tax is: ',tax)


#Question 3
# Storing different data type values in list
sid=int(input('Enter your SID: '))
name=input('Enter your Name: ')
gender=input('Enter your Gender(Male: M, Female: F, Unknown: U): ')
course_name=input('Enter your Course Name: ')
cgpa=float(input('Enter your CGPA: '))
list=[sid, name, gender, course_name, cgpa]
print(list)


#Question 4
# Displaying marks in a sorted way in a list
marks1=int(input('Enter marks of student 1: '))
marks2=int(input('Enter marks of student 2: '))
marks3=int(input('Enter marks of student 3: '))
marks4=int(input('Enter marks of student 4: '))
marks5=int(input('Enter marks of student 5: '))
list=[marks1, marks2, marks3, marks4, marks5]
list.sort(reverse=True)
print(list)



#Question 5
# Part 1
# Removing an element in a list
color=['Red', 'Green', 'White', 'Black','Pink', 'Yellow']   #Orignal list
print('Orignal list is: ', color)
color.pop(3)                                                #List after removing 4th element
print('List after removing an element: ', color)
# Part 2
color=['Red', 'Green', 'White', 'Black','Pink', 'Yellow']   #Orignal list
del color[3:4]
color[3]='Purple'
print('List after adding purple: ', color)








