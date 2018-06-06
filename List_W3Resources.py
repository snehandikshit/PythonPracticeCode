LISTS:
============================================================
#Write a Python program to sum all the items in a list

def sumlist(l):
  return sum(l)
  
print(sumlist([]))
print(sumlist([0]))
print(sumlist([1,2,3,4,-5]))
print(sumlist([1,'sneha']))

============================================================
#Write a Python program to multiplies all the items in a list.

def multiple_items(l):
  result=1
  if len(l) is 0:
    result="Empty List"
  else:
    for i in l:
      result*=i
  return result
  
print(multiple_items([]))
print(multiple_items([1]))
print(multiple_items([0]))
print(multiple_items([1,-2,3,4]))
print(multiple_items([2,'sneha']))
print(multiple_items([1,'sneha','abc']))

============================================================
#Write a Python program to get the largest number from a list.

def largest_number(l):
 return max(l)
  
#print(largest_number([])) -> Value Error
print(largest_number([1, 2, -8, 0]))
#print(largest_number([1,'sneha']))-> Type Error

============================================================
#Write a Python program to get the smallest number from a list.
def smallest_number(l):
 return min(l)
  
#print(smallest_number([])) -> Value Error
print(smallest_number([1, 2, -8, 0]))
#print(smallest_number([1,'sneha']))-> TypeError

============================================================
#Write a Python program to count the number of strings where the string length is 2
#or more and the first and last character are same from a given list of strings.

def match_words(l):
  result=[]
  for i in l:
    if len(i)>2 and i[0] == i[-1]:
      result.append(i)
  return result
  
  
print(match_words(['abc', 'xyz', 'aba', '1221' , 'a']))

============================================================

#Write a Python program to get a list, sorted in increasing order
#by the last element in each tuple from a given list of non-empty tuples.

last=lambda x:x[-1]

def sort_list_last(l):
  return sorted(l , key=last)


print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

============================================================
#Write a Python program to remove duplicates from a list.


def duplicates_removal(l1):
  l2=[ i for i in l1 if l1.count(i) == 1]
  return l2

l1 = [10,20,30,20,10,50,60,40,80,50,40]
print(duplicates_removal(l1))

OR

def duplicates_removal(l1):
  result=[]
  for i in l1:
    if l1.count(i) == 1:
      result.append(i)
  return result


l1 = [10,20,30,20,10,50,60,40,80,50,40]
print(duplicates_removal(l1))


============================================================
#Write a Python program to check a list is empty or not.

def is_empty(l1):
  if len(l1) == 0:
    return "List is Empty"
  else:
    return "List NOT Empty"
    
print(is_empty([]))
print(is_empty([0]))
print(is_empty(["s"]))

============================================================
#Write a Python program to clone or copy a list.

original_list = [10, 22, 44, 23, 4]
copy_list=list(original_list)

print(original_list)
print(copy_list)

OR

original_list = [10, 22, 44, 23, 4]
print(original_list)
print([ i for i in original_list])

============================================================
#Write a Python program to find the list of words that are
#longer than n from a given list of words.


def long_words(n, str1):
  l1=str1.split()
  results=[]
  for i in l1:
    if len(i) > n:
      results.append(i)
  return results
  
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
  
  
OR

def long_words(n, str1):
  l1=str1.split()
  results=[i for i in l1 if len(i) > n]
  return results
  
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
  
============================================================
#Write a Python function that takes two lists and
#returns True if they have at least one common member.

def common_data(list1, list2):
  for i in list1:
    if i in list2:
      return "Common Element"
  return "No Common Element"
  
print(common_data([1,2,3,4,5], [5,6,7,8,9]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

============================================================
#Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

def after_removal(color):
  results=[ color[i] for i in range(0,len(color)) if i not in (0,4,5) ]
  return results  

color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(after_removal(color))

============================================================
#Write a Python program to generate a 3*4*6 3D array whose each element is *.

def matrix():
  result= [[[ '*' for i in range(6)] for i in range(4)] for i in range(3)]
  return result
  
print(matrix())
============================================================
#Write a Python program to print the numbers of a specified list after removing even numbers from it.

def evennumber_deletion(num):
  results=[]
  for i in num:
    if i%2 == 0:
      results.append(i)
  return results

  
num = [7,8, 120, 25, 44, 20, 27]
print(evennumber_deletion(num))

OR

def evennumber_deletion(num):
  results=[ i for i in num if i % 2 != 0]
  return results

  
num = [7,8, 120, 25, 44, 20, 27]
print(evennumber_deletion(num))

============================================================
#Write a Python program to shuffle and print a specified list.
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)

============================================================
#Write a Python program to generate and print a list of first
#and last 5 elements where the values are square of numbers between 1 and 30 (both included).

def printValues():
  results1=[ x*x for x in range(1,6)]
  results2=[y*y for y in range(26,31)]
  return results1 , results2
  
print(printValues())

OR

def printValues():
  results1=[ x*x for x in range(1,31)]
  return results1[:5] + results1[-5:]
 
print(printValues())

============================================================
#Write a Python program to generate all permutations of a list in Python.

import itertools
print(list(itertools.permutations([1,2,3])))

OR

============================================================
#Write a Python program to get the difference between the two lists.

list1 = [1, 2, 3, 4]
list2 = [1, 2,5]

def difference(list1 , list2):
  return [ i for i in list1 if i not in list2] +[ i for i in list2 if i not in list1] 
    
print(difference(list1 , list2))

============================================================
#Write a Python program access the index of a list.
nums = [5, 15, 35, 8, 98]

def index_list(num):
  d1=dict()
  for i,j in enumerate(num):
    d1[i]=j
  return d1
  
print(index_list(nums))

============================================================
#Write a Python program to convert a list of characters into a string.

s = ['a', 'b', 'c', 'd']
str1=''
for i in s:
  str1+=i
print(str1)

OR

s = ['a', 'b', 'c', 'd']
str1=''.join(s)
print(str1)

============================================================

#Write a Python program to find the index of an item in a specified list.
num =[10, 30, 4, -6]
print(num.index(30))
============================================================

# Write a Python program to flatten a shallow list.
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
result=[]
for i in original_list:
  result+=i
print(result)

============================================================
#Write a Python program to append a list to the second list.

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
list3=list1+list2
print(list3)

============================================================
#Write a Python program to select an item randomly from a list.
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(random.choice(color_list))

OR
import random
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']
print(color_list[random.randint(0,len(color_list))])

============================================================

#Write a python program to check whether two lists are circularly identical.
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
print('list1 and list2')
list2_S=map(str, list2)
l2=' '.join(list2_S) 
list1_S=map(str, list1 * 2)
l1=' '.join(list1_S)
print(l2 in l1)


print('list1 and list3')
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))

print('list2 and list3')
print(' '.join(map(str,list2)) in ' '.join(map(str,list3)))

============================================================

#Write a Python program to find the second smallest number in a list.

def second_smallest(list1):
  first_smallest=min(list1)
  for i in range(0,len(list1)):
    if first_smallest in list1:
      list1.remove(first_smallest)
  second=min(list1)
  print(list1)
  return second
  
print(second_smallest([1, 2, -8, -2, 0 ,-8,-2]))

OR

def second_smallest(numbers):
    a1, a2 = float('inf'), float('inf')
    for x in numbers:
        if x <= a1:
            a1, a2 = x, a1
        elif x < a2:
            a2 = x
    return a2
print(second_smallest([1, 2, -8, -2, 0]))

============================================================
#Write a Python program to find the second largest number in a list.

def second_largest(numbers):
  first_largest=max(numbers)
  for i in range(0,len(numbers)):
    if first_largest in numbers:
      numbers.remove(first_largest)
  second=max(numbers)
  return second
  
print(second_largest([1, 2, -8, -2, 0,3,3]))

OR

def second_largest(numbers):
  a1,a2=-float('inf') , -float('inf')
  for x in numbers:
    if x>a1:
      a1, a2 = x, a1
    elif x<a2:
      a2=x
  return a2
  
print(second_largest([1, 2, -8, -2, 0,3,3,2]))

============================================================
#Write a Python program to get unique values from a list.

def unique_values(list1):
  result1=[]
  for i in list1:
    if list1.count(i)>1:
      pass
    else:
      result1.append(i)
  return result1
  
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print(unique_values(my_list))

OR

def unique_values(list1):
  result1=[x for x in list1 if list1.count(x)==1]
  return result1
  
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print(unique_values(my_list))

============================================================

#Write a Python program to remove duplicates values from a list.

def unique(list1):
  result1=set(list1)
  return result1
  
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print(unique(my_list))

OR

def unique(list1):
  result1=[]
  for x in list1:
    if x not in result1:
      result1.append(x)
  return result1
  
my_list = [10, 20, 30, 40, 20, 50, 60, 40]
print(unique(my_list))

============================================================

#Write a Python program to get the frequency of the elements in a list.

def frequency(list1):
  d1=dict()
  for i in list1:
    d1[i]=d1.get(i,0)+1
  return d1
    
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print(frequency(my_list))

============================================================

#Write a Python program to count the number of elements in a list within a specified range.

def count_range_in_list(list3, min, max):
  count=0
  for i in list3:
    if min<= i <max:
      count+=1
  return count
  
list1 = [10,20,30,40,40,40,70,80,99]
print(count_range_in_list(list1, 40, 100))

list2 = ['a','b','c','d','e','f']
print(count_range_in_list(list2, 'a', 'e'))

============================================================
#Write a Python program to check whether a list contains a sublist.

def is_Sublist(l, s):
  sub_set = True
  if s == []:
	  sub_set = True
  elif s == l:
    sub_set = True
  elif len(s) > len(l):
	  sub_set = False
  else:
	  for s1 in s:
	    if s1 not in l:
	      sub_set=False
  return sub_set
  
a = [2,4,3,5,7]
b = [4,3]
c = [3,7]
print(is_Sublist(a, b))
print(is_Sublist(a, c))


============================================================
#Write a Python program to generate all sublists of a list.

def sub_lists(my_list):
  for i in range(len(my_list)):
    n=i+1
    while n < len(my_list):
      sublist=my_list[i:n]
      print(sublist)
      n+=1
  
  
l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print(sub_lists(l1))
print(sub_lists(l2))

============================================================

#Write a Python program using Sieve of Eratosthenes method
#for computing primes upto a specified number.


def prime_numbers(num):
  numbers=[]
  result=[]
  for i in range(2,num+1):
    if i not in numbers:
      result.append(i)
      for x in range(i*i , num+1 , i):
        numbers.append(x)
  return result
        
print(prime_numbers(100))

============================================================

#Write a Python program to create a list by concatenating
#a given list which range goes from 1 to n.

my_list = ['p', 'q']
result=[]
for i in my_list:
  for j in range(1,5):
    result.append(i+str(j))
print(result)

OR

my_list = ['p', 'q']
n=4
result=[i+str(j) for i in my_list for j in range(1,n+1)]
print(result)


============================================================

#Write a Python program to get variable unique identification number or string.
#the id() function: Return the “identity” of an object. This is an integer (or long integer)
#which is guaranteed to be unique and constant for this object during its lifetime.
#Two objects with non-overlapping lifetimes may have the same id() value.

def function1(str1):
  return (id(str1))
    
print(function1(100))
print(function1("w3resources.com"))
print(function1("w3resources.com"))
x=100
print(function1(x))
============================================================
#Write a Python program to find common items from two lists.

color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
print(set(color1).intersection(set(color2)))
============================================================
#Write a Python program to change the position of every n-th value with the (n+1)th in a list.

def replace2copy(n):
  for i in range(0,len(n),2):
    n[i] , n[i+1]=n[i+1] , n[i]
  return n



n = [0,1,2,3,4,5]
#output : [1, 0, 3, 2, 5, 4]
print(replace2copy(n))
============================================================
#Write a Python program to convert a list of multiple integers into a single integer.
L = [11, 33, 50]
print("Original List: ",L)
str1=''
for i in L:
  str1+=str(i)
print("Combined List: ", str1)

OR

L = [11, 33, 50]
print("Original List: ",L)
L1=map(str,L)
print("Combined String: " ''.join(L1))

============================================================
#Write a Python program to split a list based on first character of word.

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
	 
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
     
     
def split(list1):
  d1=dict()
  list2=list()
  for i in list1:
    j=i[0]
    if j in d1.keys():
      d1[j].append(i)
    else:
      d1[j]=[i]
  return d1
      
      
print(split(word_list))

============================================================
#Write a Python program to create multiple lists.
obj=dict()
for i in range(1, 21):
    obj[str(i)] = []
print(obj)


============================================================

#Write a Python program to find missing and additional values in two lists.

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

def unique_values(list1,list2):
  missing=[]
  extra=[]
  for i in list1:
    if i not in list2:
      extra.append(i)
  for j in list2:
    if j not in list1:
      missing.append(j)
  return(missing,extra)
  
print(unique_values(list1,list2))

OR

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']

def unique_values(list1,list2):
  set1=set(list1)
  set2=set(list2)
  return (set1.difference(set2) , set2.difference(set1))
  
print(unique_values(list1,list2))

============================================================

#Write a Python program to split a list into different variables. 	
color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
         
for i in color:
  print(i)
  
OR

color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
         ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
var1,var2,var3 = color
print(var1,var2,var3)

============================================================

#Write a Python program to generate groups of five consecutive numbers in a list.

list1=[[ 5*i+j for j in range(1,6)] for i in range(0,5)]
print(list1)
============================================================
#Write a Python program to convert a pair of values into a sorted unique array.
Original List:  [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]             
Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  

List1=[(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]  

def unique_list(list1):
  list2=[]
  for i in list1:
    for j in i:
      if j not in list2:
        list2.append(j)
  return list2
  
print(unique_list(List1))


============================================================
#Write a Python program to select the odd items of a list.

x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print([i for i in x if i%2 != 0 ])

OR


x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x[::2]

============================================================
#Write a Python program to insert an element before each element of a list.

List1=['Red', 'Green', 'Black']
List2=[]
for i in List1:
  List2.append('c')
  List2.append(i)
  
print(List2)

OR

List1=['Red', 'Green', 'Black']
List2=[j for i in List1 for j in ('c' , i)] 

print(List2)

============================================================
#Write a Python program to print a nested lists (each list on a new line) using the print() function.

colors = [['Red'], ['Green'], ['Black']]
for i in colors:
  print(i)
  
============================================================
#Write a Python program to convert list to list of dictionaries.

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result=[{'color_name' : n , 'color_code' : c } for n,c in zip(color_name , color_code)]
print(result)

OR

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

result=[]
for i in range(len(color_name)):
  result.append({'color_name' : color_name[i] , 'color_code' : color_code[i] })
print(result)

============================================================

#Write a Python program to sort a list of nested dictionaries.

my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)

=============================================================
#Write a Python program to split a list every Nth element.
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n=4
list1=[[] for k in range(n)]
for j in range(n):
  count=0
  for i in range(len(C)):
    if i%n == j:
      print(j)
      list1[j].append(C[i])
      count+=1
      
print(list1)


OR

C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n=4
list1=[C[i::n] for i in range(n)]
print(list1)

=============================================================
#Write a Python program to compute the similarity between two lists. 

color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

print(set(color1).difference(set(color2)))
print(set(color2).difference(set(color1)))
=============================================================
#Write a Python program to create a list with infinite elements.

import itertools
c = itertools.count()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

=============================================================
#From 54 till 71
#Write a Python program to concatenate elements of a list.
color = ['red', 'green', 'orange']
string1=''
for i in color:
  string1+=i
print(string1)

OR

color = ['red', 'green', 'orange']
string1=''
print('-'.join(color))

#Write a Python program to remove key values pairs from a list of dictionaries.

list1=[{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

list2=[ { j:k for j,k in i.items() if j!= 'key1' } for i in list1   ]
print(list2)
============================================================================

#Write a Python program to convert a string to a list.

s1 ="['Red', 'Green', 'White']"
list1=[]
for i in s1[1:-1].split(','):
  list1.append(i.strip()[1:-1])
  
print(list1)

====================================================================================
#Write a Python program to check if all items of a list is equal to a given string.
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]

print(all( i=='blue' for i in color1  ))
print( all( j=='green' for j in color2 ) )

====================================================================================
#Write a Python program to replace the last element in a list with another list.
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

print( num1[:-1] + num2 )

====================================================================================
#Write a Python program to check if the n-th element exists in a given list.
x = [1, 2, 3, 4, 5, 7]

def nthelement(x):
  n=len(x)
  for i in x:
    if i ==n:
      return True
  return False
  
print(nthelement(x) )
====================================================================================
#Write a Python program to find a tuple, the smallest second index value from a list of tuples.

x = [(4, 1), (1, 2), (6, 0)]
x.sort( key= lambda n : (n[1] , n[0]))
print(x)
====================================================================================
#Write a Python program to create a list of empty dictionaries.
n=int(input("Enter a number:"))
list1=[ {} for i in range(n) ]
print(list1)
====================================================================================
#Write a Python program to print a list of space-separated elements.
# * symbol is use to print the list elements in a single line with space.
#To print all elements in new lines or separated by space use sep=”\n” or sep=”, ” respectively.
#The *args parameter provides for 0 or more positional arguments, which are accessible inside the function via a list named args.
num = [1, 2, 3, 4, 5]
for i in num:
  print(i , end=' ')
  
OR

num = [1, 2, 3, 4, 5]
print(*num)
  
====================================================================================
#Write a Python program to insert a given string at the beginning of all items in a list.
num = [1,2,3,4]
string1="emp"
print( [ string1+str(i) for i in num  ]  )

OR

num = [1,2,3,4]
print( [ 'emp{0}'.format(i) for i in num  ]  )
====================================================================================
#Write a Python program to iterate over two lists simultaneously.
num = [1, 2, 3]
color = ['red', 'while', 'black']
print(zip(num,color))
for i,j in zip(num,color ):
  print(i,j)

====================================================================================
#Write a Python program to access dictionary keys element by index.
num = {'physics': 80, 'math': 90, 'chemistry': 86}
print(list(num)[0])

====================================================================================
#Write a Python program to find the list in a list of lists whose sum of elements is the highest.
num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]

print(max(num , key=lambda x : sum(x)))
OR

num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(num , key=sum))

====================================================================================
#Write a Python program to find all the values in a list are greater than a specified number.
list1 = [220, 330, 500]
list2 = [12, 17, 21]
n=int(input("Enter a Number: "))

print( [ x for x in list1 if x > n]  )
print( [ x for x in list1 if x > n]  )

====================================================================================
#Write a Python program to extend a list without append. 
x = [10, 20, 30]
y = [40, 50, 60]
x[-1:]=y 
print(x)

OR
x = [10, 20, 30]
y = [40, 50, 60]
x[:0]=y 
print(x)

OR

x = [10, 20, 30]
y = [40, 50, 60]
print(x+y)
====================================================================================

#Write a Python program to remove duplicates from a list of lists.
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
num1=list()
for i in num:
  if i not in num1:
    num1.append(i)
    
print(num1)


====================================================================================
#Write a Python program to get the depth of a dictionary.

def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {'e' :{}}}}}
print(dict_depth(dic))

====================================================================================
#Write a Python program to check if all dictionaries in a list are empty or not

my_list = [{},{},{}]
my_list1 = [{1,2},{},{}]

def emptylist(list1):
  for i in list1:
    if i != {}:
      return False
      
print( emptylist(my_list)  )
print( emptylist(my_list1)  )

=============================================================