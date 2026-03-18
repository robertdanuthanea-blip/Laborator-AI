#LIST

'''my_list = [1, 2,'3', True]
len(my_list) 
print(my_list.index('3'))
print(my_list.count(2))

print(my_list[3])
print(my_list[1 :])
print(my_list[ :1])
print(my_list[-1])
print(my_list[::1])
print(my_list[::-1])
print(my_list[0:3:2])
my_list.append(4)
print(my_list*2)
print(my_list + [100])
print(my_list.append(100))
print(my_list.extend([100, 200]))
print(my_list.insert(2, '!!!'))
print(''.join(['Hello', 'World']))
print(basket := ['apple', 'banana', 'orange']   )\


print([1,2,3].pop())
print([1,2,3].remove(2))
print([1,2,3].pop(2))
print([1,2,3].clear())
del [1,2,3][0]
print([1,2,5,3].sort())    
print([1,2,5,3].sort(reverse=True))    
print(sorted([1,2,5,3]))
print(sorted([1,2,5,3], reverse=True))
print(list(reversed([1,2,5,3])))
print(1 in [1,2,5,3])
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))
print(sum([1,2,3,4,5]))
mList=[63, 21, 30, 14, 35, 26, 77,18,49,10]
first, *x ,last=mList
print(first)
print(last)
with open('file.txt', 'w') as f:
    line= [line.strip() for line in f]'''

#DICTIONARY

'''my_dict={'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['name'])
print(len(my_dict))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())
my_dict['favorite_snack'] = 'Chips'
print(my_dict['age'] ) 
print(my_dict.get('age', 0))
del my_dict['city']
my_dict.pop('name', None)'''

#SET
my_set=set()
print(my_set.add(1))
print(my_set.add(100))
new_list=[1,2,3,4,5]
set(new_list)
my_set.remove(100)
my_set.discard(100)
my_set.clear()
new_sey={1,2,3}.copy()
set1={1,2,3}    
set2={3,4,5}
set3=set1.union(set2)
set4=set1.intersection(set2)            
set5=set1.difference(set2)
set6=set1.symmetric_difference(set2)
set1.issubset(set2)
set1.issuperset(set2)
set1.isdisjoint(set2)   



#NONE
type(None)
a=  None
