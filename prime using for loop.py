#prime number using for
n = int(input('Enter number: '))
if n==1:
    print('1 is Not prime nor Composite number')    

else:
    for i in range(2, (n//2)+1):
        if (n % i) == 0:
            print('Not a prime number')
            break
        else:
            print('Prime number')
            break

'''

expected output

Enter number: 354
Not a prime number

'''
