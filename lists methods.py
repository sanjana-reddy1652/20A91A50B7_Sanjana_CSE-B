#lits methods
a_list=[10,56,76,45,13,29]
b_list=[18,8.9,"yeonjun",12,90]
#len() : length of the list
>>> len(a_list)
6
#max() : returns the max element in the list
>>> max(a_list)
76
>>> max(b_list)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    max(b_list)
TypeError: '>' not supported between instances of 'str' and 'int'

 #min() : returns the min element in the list
>>>min(a_list)
10
>>> min(b_list)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    max(b_list)
TypeError: '>' not supported between instances of 'str' and 'int'

 #append() : adds an object into the list at the last index
>>>a_list.append(1)
print(a_list)
[10, 56, 76, 45, 13, 29, 1]
>>>b_list.append("15")
[18, 8.9, 'yeonjun', 12, 90, 15]

#count() : returns the count of how many times an object occurs in the list
>>>a_list.count(10)
1
>>> b_list.count("yeonjun")
1

#index() : it returns the lowest index in the list where the object occurs
>>>a_list.index(10)
0
>>> b_list.index("yeonjun")
2

#pop() : removes the specfied object and returns the value
>>> a_list.pop(5)
29
>>> b_list.pop(5)
'sanjana'

#insert() : inserts a specfied object at specfied index
>>> a_list.insert(3,45)
>>>print( a_list)
[10, 56, 76, 45, 45, 13, 1]
>>> b_list.insert(3,"sanjana")
>>> print(b_list)
[18, 8.9, 'yeonjun', 'sanjana', 12, 90]

#sort() : sorts the given list
>>> a_list.sort()
>>> print(a_list)
[1, 10, 13, 45, 56, 76]
>>> b_list.sort()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    b_list.sort()
TypeError: '<' not supported between instances of 'str' and 'float'
  
#reverse() : reverses the given list
>>> a_list.reverse()
>>> print(a_list)
[76, 56, 45, 13, 10, 1]
>>> b_list.reverse()
>>> print(b_list)
[90, 12, 'sanjana', 'yeonjun', 8.9, 18]

#remove() : removes the specfied object
>>> b_list.remove(8.9)
>>> print(b_list)
[90, 12, 'sanjana', 'yeonjun', 18]

#extend() : appends the specfied contes to the list
>>> a_list.extend(b_list)
>>> print(a_list)
[76, 56, 45, 13, 10, 1, 90, 12, 'sanjana', 'yeonjun', 18]


  





