i=10
print(i)
mylist=[10,20,40]
mylist.insert(2,30)
print(mylist)

"""collections
"""
from collections import namedtuple
a = namedtuple('city','sector ,pin_code')
#s=a('143','201306')
#take input as list
s= a._make(['144','201303'])
print(s)

"""deque is an optimised list to perform
insertion and deletion easily
"""
#deque
from collections import deque
a=['p','r','a','n','a','v']
d= deque(a)
print(d)
d.append('singh')
print(d)
d.appendleft('asmika')
print(d)
d.pop()   #use popleft
print(d)


"""chainmap is a dictionary like class for creating a single view
of multiple mappings
"""
#Chainmap

from collections import ChainMap

a={1:'Hadoop', 2:'BigData'}
b={3:'Java', 4:'Python'}
temp= ChainMap(a,b)
print(temp)

"""Counter is a dictionary subclass for counting hashable objects
"""
#Counter
from collections import Counter
a=[1,2,1,3,4,2,5,1,3,7,3,1,5,7,2]
count= Counter(a)
print(count)
print(list(count.elements()))

print(count.most_common())
sub={2:1,6:1}
print(count.subtract(sub))
print(count.most_common())

'''
OrderedDict is a dictionary subclass which remembers the order
in which the entries were done'''

#OrderedDict
from collections import OrderedDict
d= OrderedDict()
d[1]='p'
d[2]='r'
d[3]='a'
d[4]='n'
d[5]='a'
d[6]='v'
print(d)
# d.pop(5)
# print(d)
print(d.keys())

'''defaultdict is a dictionary subclass which calls a factory function
to supply missing value'''
#defaultDict
from collections import defaultdict
d=defaultdict(int)
d[1]= 'pranav'
d[2]='asmika'
print(d)
print(d[3])
a={1:'Pranav', 2:'Asmika'}
print(a)
print(a[2])

'''UserDict is a wrapper around dictionary objects for easier sub-classing 
   UserList wrapper around list objects for easier sub-classing
   UserString wrapper around String objects for easier sub-classing'''


'''
An Array is basically a data structure which can hold morethan one value
at a time. It is a collection or ordered series of elements of the same type'''

#create arrays in Python
#1---> import array
#2----> import array as arr
#3----> from array import *

import array
a= array.array('f',[1,2,3,4,5,6])
print(a)

# import array as arr
# a= arr.array('i',[1,2,3,4])
# print(a)

# from array import *
# a= array('i',[12,12,133])
# print(a)

#accessing Array element
print(a[2])

#Basic Operation

#length of an array
print(len(a))

#adding elements to an array (append(), insert(), extend())

# using append
# a.append(2.5)
# print("added 2.5 using append-->",a)

#using extend (similar to append but you can add more number of elements
#
# a.extend([2.5,3.0,3.5])
# print("adding values using extend",a)

#using insert--> can add value to specific place
# a.insert(1,1.5)
# print(a)


'''removing elements
either use pop()-- remove and return it or- can take no or 1 param
        remove()-- remove and don't return it , takes one param
'''
#current values---> array('f', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
# a.pop() print (a.pop()) will return the element it is removing--> 6.0 in this case
# print("removing last value-->",a)
# a.pop(1)
# print("remove 1st pos element--->",a)
# a.remove(3.0)
# print("will remove specific element",a)

'''array concat--> use plus symbol (should be of same data type)'''

'''slicing of array'''
# current values- array('f', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
#print(a[0:3])  # o/p will be array('f', [1.0, 2.0, 3.0])
#(::-1) will revers the array
#print(a[::-1]) #--> array('f', [6.0, 5.0, 4.0, 3.0, 2.0, 1.0])


'''
Looping --> For and While'''
#input-->array('f', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
# print("All values-->")
# # for x in a:
# #     print(x)

#slicing
# print("using slicing")
# for x in a[:3]:
#     print(x)

'''Using WHILE'''
#input-->array('f', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
# temp=0
# while temp <a[3]:   #(temp<len(a)):
#     print("using while",a[temp])
#     temp=temp+1

'''
HashTable and HashMap
'''
# new_dict=dict(Pranav='001',Asmika='002')
# print(new_dict)
# print(type(new_dict))

#nested dictionary
emp_details={'Employee':{
                          'Pranav':{'ID':'001','Salary':'200000000','Designation':'Test Lead'},
                          'Asmika':{'ID':'002','Salary':'200000000','Designation':'Dev Lead'}
                         }
             }
# print(emp_details['Employee']['Asmika']['ID'])

#accessing dictioanlry's ley and value

#my_dict_temp={'Pranav':'01','Asmika':'02','Danu':'03','Anurag':'04', 'Vishal':'05'}
# print(my_dict_temp)
# #return value using key
# print(my_dict_temp.get('Pranav'))
# #get all values
# print(my_dict_temp.values())
# #using For loop
# for x in my_dict_temp:
#     print (x)
# # print all values using for loop
# for x in my_dict_temp.values():
#     print(x)
# # get all the items
# for x,y in my_dict_temp.items():
#     print(y,x)4

#updating
# my_dict_temp['Pranav']='007'
# print(my_dict_temp)
# my_dict_temp['Ankur']='000'
# print(my_dict_temp)

#deleting
#print(my_dict_temp.pop('Vishal')) #popitem()
# print(my_dict_temp)
# del my_dict_temp['Vishal']
# print(my_dict_temp)

'''Dict to DataFrame'''
# import pandas as pd
# df= pd.DataFrame(emp_details['Employee'])
# print(df)


'''OPERATORS
add-- x+y
minus- x-y
exp-- x**y
div-- x/y
remainder- x%y
'''
#Logical operator (conditional)
# temp1= 40
# temp2=30
# if(temp1==temp2):
#     print('temp1 and temp 2 are equal')
# elif(temp1<temp2):
#     print('temp1 is smaller than temp2')
# else:
#     print('temp1 is greater')
'''
WHILE loop guess the random number b/w 0-20'''

# import random
# print('Game')
# limit =20
# to_be_guessed= int(limit*random.random())+ 1
# print(to_be_guessed)
# guess=0
# while guess != to_be_guessed:
#     guess=int(input("New Number: "))
#     if guess > 0:
#         if guess > to_be_guessed:
#             print('Too Large')
#         elif guess < to_be_guessed:
#             print('Too Small')
#     else:
#          print('sorry that you are giving up!')
#          break
# else:
#         print('You guessed it correct!')


'''
FACTORIAL using FOR Loop
'''
# fact_temp=1
# input_number= int(input("Enter the number-->"))
# for i in range(1,input_number+1):
#     fact_temp=fact_temp*i
# print(fact_temp)
