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

def subsets(s):
    if s == []:
        return [s]
    sets = [s]
    for i in range(0, len(s)):
        tmp_subsets = subsets(s[:i] + s[i+1:])
        for subset in tmp_subsets:
            if subset not in sets:
                sets.append(subset)
    return sets
    
print(subsets([1,2,3,4,-5]))
  
  
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

=============================================================
#Write a Python program to get first prime_number after the provided number.
#python 3.5.2

def prime(num):
    for i in range(2,num):
        if num%i ==0:
            return False
    return True

def next_prime(num1):
    results=[]
    for i in range(num1,num1*2):
        if prime(i):
            results.append(i)
    print(results[0])
  
print(next_prime(100))
===================================================================
#Write a Python program to merge sorted list/array

arr1 = [ 1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

def merge(l1,l2):
    l3=l1+l2
    l3.sort()
    return set(l3)

print(merge(arr1,arr2))
====================================================================
#Write a Python program to find the max occurence of a character in a string.

def count(string1):
    d1=dict()
    for i in string1:
        if 'a' <= i <= 'z' or 'A' <= i <= 'Z':
            d1[i]=d1.get(i,0)+1
    for i,j in d1.items():
        if j == max(d1.values()):
            return i
    

print(count("Given two sorted arrays, the task is to merge them in a sorted manner"))
=====================================================================
#Write a python program to print all sub array or list that sum upto 0.

def subsets(s):
    sets = [s]
    for i in range(0, len(s)):
        #print(s[:i] + s[i+1:])
        tmp_subsets = subsets(s[:i] + s[i+1:])
        #print(tmp_subsets)
        for subset in tmp_subsets:
            if subset not in sets:
                sets.append(subset)
    return sets
    
def subsets_s(list1):
    for i in subsets(list1):
        if sum(i) == 0:
            print(i)
    
print(subsets_s([1,2,3,-3]))
========================================================================
#Anagram Program.

def anagram(str1,str2):
    result=True
    if len(str1) != len(str2):
        result=False
    else:
        for i in str1:
            if i not in str2:
                result=False
                
    return result

print(anagram("sneha","anehs"))

==========================================================================
#Boolean matrix problem  make all the values in a row or column as 1 if there are atleat one 1 in that row or column

def matrix(list1):
    row=[0]* len(list1[0])
    col=[0] * len(list1)
    #print(row,col)
    for i in range(len(list1)):
        for j in range(len(list1[i])):
            if list1[i][j]==1:
                row[i]=col[j]=1
    print(row,col)
    for i in range(len(row)):
        for j in range(len(col)):
            if row[i]==1 or col[j]==1:
                list1[i][j]=1
                
    return list1

list1=[[0,1,0],[0,0,0],[0,1,0]]
print(matrix(list1))

==========================================================================         
#Write a python program for given array where consecutive digits difference out to particular set of values and Number N.

def pair(list1 , n ):
    for i in range(len(list1)):
        for j in range(i+1 , len(list1)):
            if list1[i]-list1[j] == n or list1[j]-list1[i] ==n:
                return list1[i],list1[j]
    return None   
        
        
list1= [5, 20, 3, 50, 80 , 42]
n = 78
print(pair(list1,n))

========================================================================== 

#Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.

a = 10
b = 20
def countSetBits( n ):
    count = 0
    while n:
        count =count + (n & 1)
        n >>= 1
    return count

print(countSetBits(a^b))
========================================================================== 

