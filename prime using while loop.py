#prime number using while loop
n=int(input('enter number: ')) 
cnt = 0
i = 2
if n==1:
    print('1 is neither prime nor composite')
else :
    while i <= n // 2:
        if n % i == 0:
            cnt=1
            break
        i=i+1
    
if cnt==0:
    print("Prime number")
else:
    print("Not a Prime number")


'''
expected output
enter number: 1
1 is neither prime nor Composite number
'''
