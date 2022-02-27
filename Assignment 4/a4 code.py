#question1
def Towers_Of_Hanoi(numdisks, frm_disc, to_disc, aux_disc):
    if numdisks == 1:
        print("Move disk [1] from rod [",frm_disc, "] to rod {", to_disc, '}')
        return
    Towers_Of_Hanoi(numdisks-1, frm_disc, aux_disc, to_disc)
    print("Move disk ["+str(numdisks) + "] from rod [",str(frm_disc)+" ] to rod {", to_disc, '}')
    Towers_Of_Hanoi(numdisks-1, aux_disc, to_disc, frm_disc)
numdisks = 4
Towers_Of_Hanoi(numdisks, 'A', 'C', 'B')


#question2
#iterative method
n=int(input('Enter number of rows: '))
for i in range(1, n+1):
    for j in range(0, n-i+1):
        print(' ', end='')
    C = 1
    for j in range(1, i+1):
        print(' ', C, sep='', end='')
        C = C * (i - j) // j
    print()
#recursive method
def ptriangle(n):
    if n == 1:
        return [[1]] 
    else:
        result = ptriangle(n-1) 
        c_row = [1]
        previous_row = result[-1] 
        for i in range(len(previous_row)-1):
            c_row.append(previous_row[i] + previous_row[i+1])
        c_row += [1]
        result.append(c_row)
        return result
triangle = ptriangle(5)
for row in triangle:
    print(row)


#question3
n1=int(input('Enter 1st number: '))
n2=int(input('Enter 2nd number: '))
result=divmod(n1,n2)
print(result)

#part a
print(callable(result))

#part b
if 0 not in result:
    print('All the values are non-zeros')
else:
    print('There is a zero')

#part c
nresult=(4,5,6)+result
l=[]
for i in nresult:
    if i>4:
        l.append(i)
print(l)

#part d
set=set(nresult)
print(set)

#part e
set=frozenset(nresult)
print(set)

#part f
mval=max(set)
hash=hash(mval)
print('max value is',mval,'hash val of max val is',hash)


#question4
class Student:
    def __init__(self,name,rnumber):
        self.name = name
        self.rnumber=rnumber
    def __del__(self):
        print('Object destroyed')
s1=Student('abc',11)
print('Name of student is',s1.name,'and roll number is',s1.rnumber)
del s1


#question 5
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
e1=Employee('Mehak',40000)
e2=Employee('Ashok',50000)
e3=Employee('Viren',60000)
dict={'Name':{e1.name,e2.name,e3.name},'Salary':{e1.salary,e2.salary,e3.salary}}
print(dict)

#part a
e1.salary=70000
print(e1.__dict__)

#part b
del e3


#question 6
word1=input('Enter a word: ')
word2=input('Enter a meaningful word from letters of 1st word: ')
set1=set(word1)
set2=set(word2)
set3=set1 & set2
len1=len(set1)
len2=len(set2)
len3=len(set3)
if len3 !=len1 or len3 != len2:
    print('Friendship is fake')
else:
    print('Friendship is real')

