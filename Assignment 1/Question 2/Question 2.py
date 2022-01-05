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


