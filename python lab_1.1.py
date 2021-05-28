'''Write a program that asks the user to enter three numbers (use three separate input statements). Create variables called total and average that hold the sum and average of the three numbers and print out the values of total and average.'''


a=int(input('enter value: '))
b=int(input('enter value: '))
c=int(input('enter value: '))
total=a+b+c
avg=total/3
print('sum = %d'%total)
print('avarage = %.2f'%avg)


'''
expected output
enter value: 1
enter value: 2
enter value: 3
total = 6
average = 2.00
'''
