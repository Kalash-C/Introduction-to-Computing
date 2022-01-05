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
