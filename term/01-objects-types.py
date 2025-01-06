from more_itertools.more import substrings

a = [2,4,6]
b = a
a.append(8)
print(b)
#___________________
print(type (a))
#___________________
a=15
b=25
def my_func():
    global a #change global var, scope inside this function
    a=11
    b=21 # we cant change this
my_func()
print (a)
print(b)
#___________________
c= 10
def my_func2():
    print(c) #printble even if its not global
my_func2()
d= 10
def my_func3():
    global d
    d = d + 1 #we cant change it if its not global, now its changeble with global
    print(d)
my_func3()
#___________________
x=0
while x<3 : print(x); x+=1
#___________________
words = ['cat','dog','elephant']
for w in words:
    print(w) #print list
# ___________________
#all data types in py are objects | numeric types: int, float, complex, bool | sequence type: str, list, tuple, range | mapping type: dict
if a==b:
    print("a & b are equal, same value")
if a is b:
    print("a & b are same object")
if type(a) is type(b):
    print("a & b are the same type")
# ___________________
# Objects: 1) Mutable (like list) value is not fixed and can change, they have methods like insert() & append()
# 2) immutable (like string) can't have their values change, ex: int class is immutable, strings
#String Methods:
s = "test"
t = "hey"
print(s.capitalize()) #Captilize first charecter
print(s.isalnum()) #Returns true if all alphanumeric
print(s.isalpha()) #Return true if all alphabetic, space is not alphabetic
print(s.isdigit()) #Return true if all digits in string
print(s.split('s',1)) # split where 's' if u dont what maxspilit parm u can set it -1
print(s.join(t)) #Insert s between each character of t
print(s.lower()) #Convert all character to small letter
print(s.upper()) #Convert all character to captilize
print(s.replace('s','f')) #replace s with f
print(s.startswith('t')) #Return True if start with this char
print(s.endswith('t')) #Return True if end with this char
print(s.strip('t')) #Remove whitespace or char u set
print(s.lstrip('t'))#Return string with leading character removed (only first one)
print(s.swapcase()) #Swap if something is small to cap or cap to small
greet = 'hello world'
print(greet[1], greet[0:8], greet[0:8:2], greet[0::2]) # Return [second index | index 0 to 8 | index 0to 8 with 2 step | index 0 to end with 2 step]
print(greet[len(greet)-1]) #len greet is 11 and its last index
n=0
for i in greet:  #pring index and value without using enumerate
    print(f"{i}{n} |")
    n+=1
for i in enumerate(greet[0:5]):print(i) #enumerate return value and index
print (greet[:5] + ' fucking' + greet[5:])

x='3';y='2'
print(x+y) #concatenation, they are string it just join strings
print(int(x)+int(y)) #now its int and addition
#_________________
#in list we can store different type of data
#List Methods:
print(list(s)) #Return a list of sequence
s = list(s)
nl = [1,2,3]
s.append("F") #insert "F" at the end of list
s.extend(nl) #extend list nl at the end of list s
print(s.count("t")) #count of 't' in this list
s.insert(0,'I') #insert X in index i
print(s.pop()) #pop last index
s.remove('I') #remove this value from list
s.reverse() #reverse order
print(s)
#mutable compound objects
x=1; y=2 ;z=3
list1 = [x,y,z]
list2 = list1
list2 [1] = 4
print(list1) # 1,4,3 because they are pointing to each other
#list inside list
items = [['rice',2.3,10],['test2',1.5,2],['test3',4.4,6]]
items[1][1] = items[1][1] * 2 #change value inside list with 2 dimension
for item in items:
    print('Product: %s Price: %.2f Quality: %i' % (item[0], item[1], item[2])) #%s string, %.2f float with 2 digit limit, %i int
#list comprehensions
l= [1,2,3,4,5]
print([i**3 for i in l])
l2=[[1,2,4],[3,1,6]]
print([i*j for i in l2[0] for j in l2[1]])
#list comprehensions for strings
words= 'idk wtf is this'.split()
print([[word,len(word)]for word in words])
#func
def greeting (language):
    if language=='eng':
        return('hello')
    elif language=='persian':
        return('salam')
    else: return('language not supported')
#lang = input("Enter language: ")
#print(greeting(lang))

#use list to call func
langs=[greeting('eng'), greeting('persian'),greeting('test else')]
print(langs[1],langs[2])

#higher order func like lambda + map + filter + sorted , etc...
l4 = [1,2,23,4,532]
for item in map(lambda n: n*2,l4): #using map ro walk in list
    print(item)

for item in filter(lambda n: n>3,l4): #using filter to filter list (=
    print(item)

print (sorted(words,key=len)) #using sorted but with key=len,lower,etc...

#sort more complex structures with lambda
items2 = [['test',2.45,10],['test2',1.5,2],['test3',4.4,6]]
items2.sort(key=lambda items2:items2[1]) #sort from lower
print(items2)

