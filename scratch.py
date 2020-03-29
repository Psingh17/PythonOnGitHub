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



