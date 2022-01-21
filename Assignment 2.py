# Question 1
str=('Python is a case sensitive language')     # given

# Part a
length=len(str)  
print('Length of given string is', length)      

# Part b      
rev_str=str[::-1]                     # Reversing the given string
print('Reverse of given string is: ', rev_str)

# Part c
sliced_str=str[10:26]    
print('Sliced string is: ', sliced_str)     # Storing 'a case sensitive' in a different string

# Part d
new_str=str.replace('a case sensitive', 'object oriented')
print('New string is: ', new_str)

#Part e
index=str.index('a')              # Printing index of 'a'
print('Index of "a" in string is: ', index)

#Part f
string=str.replace(' ', '')              # Replacing the white spaces
print('Given string without white spaces: ', string)


#Question 2
name='Kalash'
sid=int(21105115)
dept_name='ECE'
cgpa=float(9.9)
statement='Hey %s here! \nMy SID is %d \nI am from %s and my cgpa is %f'%(name, sid, dept_name, cgpa)
print(statement)


#Question 3
a=56
b=10
print('a&b is ',a&b)
print('a|b is ',a|b)
print('a^b is ', a^b)
print('Left Shifting "a" with 2 bits ',a<<2,' and "b" with 2 bits ', b<<2)
print('Right Shifting "a" with 2 bits',a>>2,' and "b" with 4 bits ',b>>4 )


# Question 4
num1=int(input('Enter 1st number: '))
num2=int(input('Enter 2nd number: '))
num3=int(input('Enter 3rd number: '))
num4=max(num1,num2,num3)     # To find maximum of 3 numbers is
print('Greatest of 3 numbers is: ',num4)


#Question 5
i=input('Enter a string: ')
if i=='name' :
    print('True')
else:
    print('False')

#Question 6
len1=int(input('Enter length of 1st side: '))
len2=int(input('Enter length of 2nd side: '))
len3=int(input('Enter length of 3rd side: '))
if len1+len2>len3 :
    if len1+len3>len2 :
        print('Yes')
    else:
        print('No')
else:
    print('No')




