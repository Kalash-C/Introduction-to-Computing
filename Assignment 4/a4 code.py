#question1
class Towers:
    def __init__(self, disks=3):
        self.disks = disks
        self.towers = [[]]*3
        self.towers[0] = [i for i in range(self.disks, 0, -1)]
        self.towers[1] = []
        self.towers[2] = []
    def __str__(self):
        output = ""
        for i in range(self.disks, -1, -1):
            for j in range(3):
                if len(self.towers[j]) > i:
                    output += " " + str(self.towers[j][i])
                else:
                    output += "  "
            output += "\n"
        return output + "-------"
    def move(self, from_tower, dest_tower):
        disk = self.towers[from_tower].pop()
        self.towers[dest_tower].append(disk)
def solve_tower_of_hanoi(towers, n, start_tower, dest_tower, aux_tower):
    if n == 0:
        return
    solve_tower_of_hanoi(towers, n - 1, start_tower, aux_tower, dest_tower)
    towers.move(start_tower, dest_tower)
    print(towers)
    solve_tower_of_hanoi(towers, n - 1, aux_tower, dest_tower, start_tower)
t = Towers()
print(t)
solve_tower_of_hanoi(t, len(t.towers), 0, 2, 1)


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
        self.roll_number=rnumber
    def __del__(self):
        print('Object destroyed')
s1=Student('abc',11)
del s1


#question 5
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary=salary
e1=Employee('Mehak',40000)
e2=Employee('Ashok',50000)
e3=Employee('Viren',60000)

#part a
e1.salary=70000
print(e1.__dict__)

#part b
del e3
