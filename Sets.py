#Write a Python program to create a set.
s1=set()
print(s1)
s1=set([1,2,3,4,5])
print(s1)
s1={1,2,3}
print(s1)
=================================================================================
#Write a Python program to iteration over sets.
num_set = set([0, 1, 2, 3, 4, 5])

for i in num_set:
  print(i)
=================================================================================
#Write a Python program to add member(s) in a set. 
s1 = set()
s1.add("Red")
s1.update(["Green" , "Black"])
print(s1)
=================================================================================
#Write a Python program to remove item(s) from set.
s1 = set([0, 1, 3, 4, 5])
s1.remove(4)
s1.pop()
print(s1)
================================================================================= 
#Write a Python program to remove an item from a set if it is present in the set.
s1 = set([0, 1, 3, 4, 5])
s1.discard(0)
s1.discard(1)
print(s1)
=================================================================================
#Write a Python program to create an intersection of sets.
x = set(["green", "blue"])
y = set(["blue", "yellow"])
print( x.intersection(y)  )
=================================================================================
#Write a Python program to create a union of sets.
x = set(["green", "blue"])
y = set(["blue", "yellow"])
print( x.union(y)  )
=================================================================================
#Write a Python program to create set difference.
x = set(["apple", "mango"])
y = set(["mango", "orange"])

print( x.difference(y)  )
print( y - x  )
=================================================================================
#Write a Python program to create a symmetric difference.
x = set(["apple", "mango"])
y = set(["mango", "orange"])

print( x.symmetric_difference(y)  )
print( x ^ y )
=================================================================================
#Write a Python program to issubset and issuperset. 
x = set(["apple", "mango"])
y = set(["mango", "orange"])
z = set(["mango"])

print( z.issubset(x)  )
print( z.issubset(y)  )

print( x.issuperset(z)  )
print( y.issuperset(z)  )
=================================================================================
#Write a Python program to create a shallow copy of sets.
p = set(["Red", "Green"])
q = set(["Green", "Red"])

print( p.copy() )
print( q.copy() )
=================================================================================
#Write a Python program to clear a set. 
p = set(["Red", "Green"])
p.clear()
print(p)
=================================================================================
#Write a Python program to use of frozensets. 
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])

x1=x.copy()
print(x.difference(y))
print(x.intersection(y))
print(x.isdisjoint(y))
print(x.issubset(y))
print(y.issuperset(x))
print(x.union(y))
print(x.symmetric_difference(y))
=================================================================================
#Write a Python program to find maximum and the minimum value in a set.
a = set([5, 10, 3, 15, 2, 20])
print(max(a))
print(min(a))
=================================================================================
#Write a Python program to find the length of a set.
a = set([5, 10, 3, 15, 2, 20])
print(len(a))
=================================================================================