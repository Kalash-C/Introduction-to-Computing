#Question 1
print('Question 1')

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


#Question 2
print('Question 2')

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


#Question 3
print('Question 3')

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


#Question 4
print('Question 4')

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


