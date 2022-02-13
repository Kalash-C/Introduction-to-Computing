#Question 1
print('Question 1')
print()

def string(str):
    dic=dict()
    spl=str.split()
    if len(spl)>1:
        for i in spl:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
    else:
        lst=list(a)
        for i in lst:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
    return dic
a=input('Enter a string: ')
print((string(a)))


print()
print()
#Question 2
print('Question 2')
print()

day=int(input('Enter Day: '))
month=int(input('Enter Month: '))
year=int(input('Enter Year (1800-2025): '))
if day==31 and month==[1,3,5,7,8,10]:
    d=1
    m=month+1
    y=year
    print('Next date is: ',d,'/',m,'/',y)
elif day==31 and month==12:
    d=1
    m=1
    y=year+1
    print('Next date is: ',d,'/',m,'/',y)
elif day==30 and month==[4,6,9,11]:
    d=1
    m=month+1
    y=year
    print('Next date is: ',d,'/',m,'/',y)
elif day==29 and month==2 and year%4==0:
    d=1
    m=3
    y=year
    print('Next date is: ',d,'/',m,'/',y)
elif day==28 and month==2 and year%4!=0:
    d=1
    m=3
    y=year
    print('Next date is: ',d,'/',m,'/',y)
elif day<1 or day>31 or month<1 or month>12 or year<1800 or year>2025:
    print('Please enter correct date')
elif day>30 and month==[4,6,9,11]:
    print('Please enter correct date')
elif day>28 and month==2 and year//4!=0:
    print('Please enter correct date')
elif day>29 and month==2 and year//4==0:
    print('Please enter correct date')
else:
    d=day+1
    m=month
    y=year
    print('Next date is: ',d,'/',m,'/',y)

    
print()
print()
#Question 3
print('Question 3')
print()

no=int(input('How many numbers do you want to add: '))
r=range(1,no+1) 
lst=list(r)
lst_1=[]
ab=0
for i in lst:
    if ab<no:          #given so that integers can only be entered a certain number of times
        i=int(input('Enter a number: '))       #numbers to be entered as given in the question
        ab+=1
        c=lst_1.append(((i,i**2)))  #number entered by user in each iteration is added into lst_1
    else:
        break
print(lst_1)


print()
print()
#Question 4
print('Question 4')
print()

gp=int(input('Enter the grade point: '))
if gp==4:
    print('Your grade is "D" and Poor performance')
elif gp==5:
    print('Your grade is "C" and Below Average performance')
elif gp==6:
    print('Your grade is "C+" and Average performance')
elif gp==7:
    print('Your grade is "B" and Good perofrmance')
elif gp==8:
    print('Your grade is "B+" and Very Good performance')
elif gp==9:
    print('Your grade is "A" and Excellent performance')
elif gp==10:
    print('Your grade is "A+" and Outstanding performance')
else:
    print('Please enter correct grade point')


print()
print()
#Question 5
print('Question 5')
print()

rows=int(7)
for i in range(rows - 1, 0, -1):
    for j in range(1, (rows - i + 1)):
        print(end = ' ')
    for k in range(1,(2 * i)):
        print( '%c' %(64 + k), end = '')
    print()


print()
print()
#Question 6
print('Question 6')
print()

sid=int(input('Enter sid: '))
name=input('Enter name: ')
data={}
a=input('Do you want to enter more data (Use "Y" or "N"): ')
data[sid]=name
while a=='Y':
    sid=int(input('Enter sid: '))
    name=input('Enter name: ')
    a=input('Do you want to enter more data (Use "Y" or "N"): ')
    data[sid]=name
    continue
if a=='N':
    print('Data has been added')
else:
    print('Error')
#part a
print('The data entered is ', data)

#part b
print('Dictionary sorted by name ', sorted(data.items(),key=lambda t:t[1]))

#part c
print('Dictionary sorted by sid ', sorted(data.items(),key = lambda t:t[0]))

#part d
s_sid=int(input('Enter the SID: '))
if s_sid in data:
     print('The name of the student is ', data.get(s_sid))
else:
    print('SID does not exist')


print()
print()
#Question 7
print('Question 7')
print()

num = int(input("Enter the number of terms: "))
num1=0
num2=1
count=0
sum=0
if num <= 0:
   print("Please enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,"is ",num1)
else:
   print("Fibonacci sequence:")
   while count < num:
       print(num1)
       r = num1 + num2
       num1 = num2
       num2 = r
       count += 1
       sum+=num1
sum1=sum-num1
avg=sum1/num
print('The average of the fibonacci series of given',num,'terms is',avg)


print()
print()
#Question 8
print()

set1={1,2,3,4,5}
set2={2,4,6,8}
set3={1,5,9,13,17}

#part a
a=set1^set2
print('Elements that are in st1 and set2 but not both are',a)

#part b
b=set1^set2^set3
print('Elements that are only in one of set1, set2 and set3 are',b)

#part c
c=(set1|set2|set3)-(set1&set2&set3)-b
print('Elements that are exactly in 2 sets are',c)

#part d
d={*()}
for i in range(1,10):
    if i not in set1:
        d.add(i)
print('Elements from 1 to 10 that are not in set1 are',d)

#part e
e={*()}
for i in range(1,10):
    if i not in set1|set2|set3:
        e.add(i)
print('Elements from 1 to 10 that are not in any of the given sets are',e)





