#if-else
#program to read age and check if the student is eligable for vote ot not
name=input('enter name: ')
age=int(input('enter age: '))
if age>=18 :
    print('Hello',name)
    print('eligible for vote')
else :
    print('sorry!',name)
    print('not eligible for vote')
    
'''
expected output
enter name: sanjana
enter age: 19
Hello sanjana
eligible for vote
'''
