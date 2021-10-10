'''
* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing
'''
from collections import OrderedDict,deque,defaultdict
'''1.OrderDict'''
# O = OrderedDict()
# O[1] = 2
# O[4] = 3
# O[3] = 1
# print(O)
# O.move_to_end(4)
# print(O)
# O[5] = 1
# print(O)
# O.popitem(last=False)
# print(O)

'''2.deque'''
q = deque()
q.append(3)
print(q)
q.append(4)
q.append(5)
q.append(6)
print(q)
q.pop()
print(q)
for i in q:
    print(i)
'''3.defaultdict'''
dict_s1 = defaultdict(int)
for i in range(ord("A"), ord("Z") + 1):
    dict_s1[chr(i)] = 0
print(dict_s1)