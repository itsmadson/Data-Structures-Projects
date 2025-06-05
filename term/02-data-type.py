#Types
from sympy.physics.units import length

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

#Membershio, identity
x=[1,2,3]
y=[1,2,3]
print(x==y, x is y) # x is not y cuz they are in different part of memory only of x=y return True

#sequences: string, list , tuple, range object
#s+r concatenate just if two sequence are same type

#List:
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

#Tuple:
t = tuple()
print(type(t)) #class tuple
t = ('a',) #tuple with 1 element
tpl = ('s', 'e', 'q', 'u', 'e', 'n', 'c', 'e')
print('a' in tpl, 'z'in tpl) #check membership
tpl3 = t + tpl # tuple concatenation
tpl4 = tpl*2 #repetition
print('Length: ',len(tpl3),'Max: ',max(tpl3),'Min: ',min(tpl3))
#tpl3[1] = 2  tuple is not allowed to do this, its immutable

#Dictionary (Key/Value)
#Hints: Keys should be unique, Values can be changed
dic = {'monday':1,'tuesday':2,'wednesday':3}
con = dict(zip(['monday','tuesday','wednesday'],[1,2,3])) # Convert two list into dictionary using ZIP
con['Thursday']=4 # Add an item (Just one item)
con.update({'friday':5,'Saturday':6}) # Add multiple items
con.update(friday=7) #update the value of key 'friday'
print ('wednesday' in con) #Check membership (only key) if its (5 in con) it will return False (cant use for values)
zdic = dict(zip('test',range(5))) #make t:0 , e:1...
print(zdic['e'],zdic.pop('s')) # return value of that key
bdic = con.copy() # Make copy of con
print('Just Values: ',bdic.values(),'Key/Value :',bdic.items())

#Text Analysis with Dictionaries
def wordcount (fname):
    try:
        fhand=open(fname)
    except:
        print('file cant opened')
        return
    count=dict()
    for line in fhand:
        words=line.split()
        for word in words:
            if word not in count:
                count[word]=1
            else:
                count[word]+=1
    return(count)

count= wordcount('alice.txt')
print(count)

#Sets
#set types do not provide any indexing or slicing operations
s1 = set()
s1.add(1) # add() is specific method for sets
s1.add(2)
s1.add(3)
print(s1)
s1.remove(2) #Remove that element
s1.discard(1) #Remove do the same remove done.
s1.clear() #Clear set when u return that: set() with no element
#Sets Methods
s2 = {5,'a',4,'m',12,'idk'}
s3 = {4,15,28,'idk'}
print('sub: ',s2-s3, 'use diffetence(): ', s2.difference(s3) , 'intersection: ',s2.intersection(s3), 'Union: ', s2.union(s3)) #So s2-s3 and s2.difference(s3) is the same
print('idk' in s3, 'm' not in s2) #Check Membership
for element in s2: print(element) #we can loop through elements
