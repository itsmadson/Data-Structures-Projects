#Types
a=4;b=6
print(a, 'is of type' , type(a)) #int
print(type(9/5)) #float
f=3+5j
print(f, 'type: ', type(f), 'real: ' , f.real, 'imag: ',f.imag)

print(bool(2),bool(-2),bool(0)) #only bool of 0 is false
#not x (-x) , x and y (if both true), x or y (if one of them is true)
see_boolean= (4*3>10) and (6+5 >= 11)
print(see_boolean)
#Representation error
r= 1-0.9
print(0.1 == r) #false cuz its 0.0999999999999998 not 0.1, some memory stuff

#membershio, identity
x=[1,2,3]
y=[1,2,3]
print(x==y, x is y) # x is not y cuz they are in different part of memory only of x=y return True

#sequences: string, list , tuple, range object
#s+r concatenate just if two sequence are same type
#list:
list1 = [1,2,4,5]
list1.append(1) # append balue end of list
print(list1 *2 )#make copy of each item of list1
print(min(list1), max(list1)) #find min and max
list1.insert(2,3) # insert 3 in index 2, so (index, obj)
list1.reverse() #reverse list
list1.extend([6,42,6]) # add two list objects together
print(list1)
print(sum(list1)) # add all objects in list if they are same type
print(len(list1)) #length list
list1.sort() #sort list
list1.remove(42) #find and remove this
print(list1)

#tuple:
t = tuple()
print(type(t)) #class tuple
t = ('a',) #tuple with 1 element
tpl = ('s', 'e', 'q', 'u', 'e', 'n', 'c', 'e')
print('a' in tpl, 'z'in tpl) #check membership