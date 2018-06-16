# Write a Python program to create a tuple.
t1='a','b','c'
t2=tuple()
t3=('g','h','i')
t4=6,
===========================================================================
#Write a Python program to create a tuple with different data types. 
t1=('abc',123,False,('x',23) , [1,2,'ab'] ,{'a':'b' })
print(t1)
===========================================================================
#Write a Python program to create a tuple with numbers and print one item
t1=1,2,3,4,5
print(t1)
t2=1,
print(t2)
===========================================================================
#Write a Python program to unpack a tuple in several variables.

a,b,c,d ,e,f=('abc',123,False,('x',23) , [1,2,'ab'] ,{'a':'b' })
print(a,b,c,d,e,f)
===========================================================================
#Write a Python program to add an item in a tuple.
t1= (4, 6, 2, 8, 3, 1) 
t1=t1 + (5,)
print(t1)
===========================================================================
#Write a Python program to convert a tuple to a string.
t1=('s','n','e','h','a')
c=str()
for i in t1:
	c+=i
print(c)

OR

t1=('s','n','e','h','a')
c=''.join(t1)
print(c)
===========================================================================
#Write a Python program to get the 4th element and 4th element from last of a tuple. 
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")
print(tuplex[3])
print(tuplex[-4])
===========================================================================
#Write a Python program to create the colon of a tuple.
a=2
tuplex = ("HELLO", 5, [a], True) 
print(tuplex)
tupley=tuplex[:]
tuplex=tuplex+(False,)
print(tupley)
print(tuplex)

===========================================================================
#Write a Python program to find the repeated items of a tuple.
tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
print(set([i for i in tuplex if tuplex.count(i) >1]))
===========================================================================
#Write a Python program to check whether an element exists within a tuple.
tuplex = ("w", 3, "r", "e", "s", "o", "u", "r", "c", "e")

def elementexists(t1 , e):
  return e in t1
  
print(elementexists(tuplex,3))
print(elementexists(tuplex,'a'))
print(elementexists(tuplex,'e'))
===========================================================================
#Write a Python program to convert a list to a tuple.
l1=[5, 10, 7, 4, 15, 3] 
print(tuple(l1))
===========================================================================
#Write a Python program to remove an item from a tuple.
tuplex = "w", 3, "r", "s", "o", "u", "r", "c", "e"

def remove(t1,e):
  if e not in t1:
    return "Element NOT found!!!!"
  else:
    t1=t1[:t1.index(e)]+ t1[t1.index(e)+1:]
    return t1
    
print(remove( tuplex , 3 ))
print(remove( tuplex , 'e' ))
print(remove( tuplex , 'd' ))
===========================================================================
# Write a Python program to slice a tuple.
tuplex = (2, 4, 3, 5, 4, 6, 7, 8, 6, 1)

print(tuplex[:])
print(tuplex[:4])
print(tuplex[2:])
print(tuplex[2:6])
print(tuplex[2:7:2])
===========================================================================
#Write a Python program to find the index of an item of a tuple.
tuplex = tuple("index tuple")
def indexofitem(t1,e):
  return t1.index(e)
  
print(indexofitem(tuplex,'e') )
print(indexofitem(tuplex,2) ) #ValueError as item 2 not present in tuple tuplex.
===========================================================================
#Write a Python program to find the length of a tuple. 
tuplex = tuple("index tuple")
print(len(tuplex))
===========================================================================
#Write a Python program to convert a tuple to a dictionary. 
tuplex = ((2, "w"),(3, "r"))
d1=dict()
for i in range(len(tuplex)):
  d1[tuplex[i][0]]=tuplex[i][1]
  
print(d1)
===========================================================================
#Write a Python program to unzip a list of tuples into individual lists.
l = [(1,2), (3,4), (8,9)]

for i in zip(*l):
  print(i)
  
===========================================================================
#Write a Python program to reverse a tuple. 

x = ("w3resource")
t1=tuple(x)
t2=tuple(reversed(t1))
print(t1)
print(t2)
===========================================================================
#Write a Python program to convert a list of tuples into a dictionary.

l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]
d1=dict()

for i,j in l:
  d1.setdefault(i,[]).append(j)
  
print(d1)
===========================================================================
#Write a Python program to print a tuple with string formatting.
t = (100, 200, 300)
print( ''.join(str(t) ))
print("{0}".format(t))
  
===========================================================================
#Write a Python program to replace last value of tuples in a list. 
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

def replcaelastvalue(l1,replcaevalue):
  l2=[]
  for i in l1:
    l2.append(i[:len(i)-1]+(replcaevalue,))
  print(l2)
  
replcaelastvalue(l,100)
===========================================================================
#Write a Python program to remove an empty tuple(s) from a list of tuples.
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L1=[]
for i in L:
  if len(i)!=0:
    L1.append(i)
    
print(L1)
===========================================================================

#Write a Python program to sort a tuple by its float element.
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]

print(sorted(price,key=lambda x : x[-1]))
print(sorted(price,key=lambda x : x[-1] , reverse=True))

===========================================================================
#Write a Python program to count the elements in a list until an element is a tuple.
num = [10,20,30,(10,20),40]
count=0
for i in num:
  if isinstance(i,tuple):
    break
  count+=1
    
print(count)

===========================================================================