a=int(input('total bill amount: '))
if a in range(1000,2000) :
    dis1=a*0.1
    print('discount :%.2f'%dis1)
    paid=a-dis1
    print('paid amount is:%d'%paid)
elif a in range(2000,3000) :
    dis2=a*0.2
    print('discount :%.2f'%dis2)
    paid=a-dis2
    print('paid amount is:%d'%paid)
elif a in range(3000,5000) :
    dis3=a*0.3
    print('discount :%.2f'%dis3)
    paid=a-dis3
    print('paid amount is:%d'%paid)
elif a > 5000 :
    dis4=a*0.4
    print('discount :%.2f'%dis4)
    paid=a-dis4
    print('paid amount is:%d'%paid)
else :
    print('no discount')
    print('paid amount is:%d'%a)


'''
 expexted output
 total bill amount: 6000
 discount: 2400.00
'''
    
    
    
