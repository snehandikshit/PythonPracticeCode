#Dictonary:
=================================================================================
#Write a Python script to sort (ascending and descending) a dictionary by value.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def sorting(d1):
  print("Ascending") 
  for i in sorted(d1 , key=d1.get):
    print(i , d1[i])
  print("Desending")  
  for i in sorted(d1 , key=d1.get , reverse=True):
    print(i,d1[i])
    
sorting(d)
=================================================================================
#Write a Python script to add a key to a dictionary.
d = {0:10, 1:20}

def add_key(d, k , value):
  d[k]=value
  return d

print(add_key(d,2,30))
=================================================================================
#Write a Python script to concatenate following dictionaries to create a new one.
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}

dict_new=dict()
for i in (dic1,dic2,dic3,dic4):
  dict_new.update(i)
  
print(dict_new)
  
=================================================================================
#Write a Python script to check if a given key already exists in a dictionary. 
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def iskey(d,key):
  if key in d.keys():
    return "Key {0} is present".format(key)
  return "Key {0} NOT present".format(key)

print( iskey(d, 2)  )
print( iskey(d, 10)  )

=================================================================================
#Write a Python program to iterate over dictionaries using for loops.
d = {'x': 10, 'y': 20, 'z': 30} 

for key,values in d.items():
  print(key,values)
  
OR

d = {'x': 10, 'y': 20, 'z': 30} 

{print(key,values) for key,values in d.items()}
=================================================================================
#Write a Python script to generate and print a dictionary that contains a number
#(between 1 and n) in the form (x, x*x).
def nsquare(n):
  {print(i,i*i) for i in range(n)}
  
nsquare(10)
=================================================================================
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15
#(both included) and the values are square of keys. 
{print(i,i*i) for i in range(1,15)}
=================================================================================
#Write a Python script to merge two Python dictionaries.
 d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d1.update(d2)
print( d1 )

OR

d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}

for (key,values) in d2.items():
  d1[key]=values
  
print(d1)
=================================================================================
#Write a Python program to iterate over dictionaries using for loops.
d = {'Red': 1, 'Green': 2, 'Blue': 3} 
for k in d.keys():
  print(k,d[k])
=================================================================================
#Write a Python program to sum all the items in a dictionary.
 d = {'data1':100,'data2':-54,'data3':247}

print(sum([ v for v in d.values() ]))


=================================================================================
#Write a Python program to multiply all the items in a dictionary. 
d = {'data1':100,'data2':-54,'data3':247}
result=1
for v in d.values():
  result*=v
  
print(result)
=================================================================================
#Write a Python program to remove a key from a dictionary.
d = {'a':1,'b':2,'c':3,'d':4}
k='a'
def deletekey(d,k):
  if k not in d.keys():
    return "Key {0} not present".format(k)
  else:
    d.pop(k)
    return d
  
print(deletekey(d,k)  )
    
=================================================================================
#Write a Python program to map two lists into a dictionary.
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
d=dict()
for i in range(len(keys)):
  d[keys[i]]=values[i]
  
print(d)

OR

keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
print(dict(zip( keys, values )))
=================================================================================
#Write a Python program to sort a dictionary by key.
color_dict = {'red':'#FF0000','green':'#008000','black':'#000000','white':'#FFFFFF'}
for i in sorted(color_dict):
  print( i,color_dict[i]  )
=================================================================================
#Write a Python program to get the maximum and minimum value in a dictionary.
my_dict = {'x':500, 'y':5874, 'z': 560}
max([ i for i in my_dict.values() ] )
min([ i for i in my_dict.values() ] )
=================================================================================
#Write a Python program to get a dictionary from an object's fields.

class dict(object):
	def __init__(self,key,value):
		self.key=key
		self.value=value
	def __str__(self):
		return "{0}:{1}".format(self.key,self.value)

d1=dict('1','a')
print(d1)
=================================================================================
#Write a Python program to remove duplicates from Dictionary. 
student_data = {'id1':{'name': ['Sara'], 'class': ['V'],'subject_integration': ['english, math, science']},
 'id2': {'name': ['David'], 'class': ['V'], 'subject_integration': ['english, math, science']},
 'id3': {'name': ['Sara'], 'class': ['V'], 'subject_integration': ['english, math, science']},
 'id4': {'name': ['Surya'], 'class': ['V'], 'subject_integration': ['english, math, science']},}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
=================================================================================
#Write a Python program to check a dictionary is empty or not. 
d1=dict()
d2={'1':'a'}
print( bool(d1) )
print( bool(d2))

=================================================================================
#Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3=dict()
for i in d1:
  if i not in d2:
    d3[i] = d1[i]
  else:
    d3[i]=d1[i]+d2[i]

for i in d2:
  if i not in d3:
    d3[i]=d2[i]
    
print(d3)
=================================================================================
#Write a Python program to print all unique values in a dictionary. 
d1 = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
l1=[]
d2=[list(d1[i].values()) for i in range(len(d1))]
for i in d2:
  if i not in l1:
    l1.append(i)
print(l1)

  
=================================================================================
# Write a Python program to create and display all combinations of letters,
#selecting each letter from a different key in a dictionary.
d ={'1':['a','b'], '2':['c','d']}
def combination(g):
     list1 = list(g.values())[0]
     list2 = list(g.values())[1]
     for i in list1:
         for j in list2:
              print(i+j)
combination(d)
=================================================================================
#Write a Python program to find the highest 3 values in a dictionary.
d = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  

def first_n_largest(d,n):
  l1=sorted(d,key=d.get)
  for i in range(len(d)-3 , len(d)):
    print(l1[i],d[l1[i]])
    
first_n_largest(d,3)
=================================================================================
#Write a Python program to combine values in python list of dictionaries.
list1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#print(list1)
d1=dict()
for i in list1:
  d1[list(i.values())[0]]=d1.get(list(i.values())[0],0)+list(i.values())[1]

print(d1)

=================================================================================

#Write a Python program to create a dictionary from a string.Note: Track the count of the letters from the string.

str1 = 'w3resource'

def counters(s1):
  d1=dict()
  for i in s1:
    d1[i]=d1.get(i,0)+1
  return d1
  
print(counters(str1))

=================================================================================
#Write a Python program to print a dictionary in table format.
my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}

z1=([k] + v for k,v in my_dict.items())
z2=zip(*z1)
for i in z2:
  print(*i)

=================================================================================
#Write a Python program to count the values associated with key in a dictionary.
student = [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]

print(sum([d['id'] for d in student ]))
print(sum([d['success'] for d in student ]))

=================================================================================
#Write a Python program to convert a list into a nested dictionary of keys.

num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
    print(new_dict)
=================================================================================
#Write a Python program to sort a list alphabetically in a dictionary.
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
for k in num.keys():
  num[k]=sorted(num[k])

OR
num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}  
print({ k:sorted(num[k]) for k in num.keys() })

=================================================================================
#Write a Python program to remove spaces from dictionary keys.

d1 = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
def removal(k):
  result=''
  for i in k:
    if i != ' ':
      result+=i
  return result
  
d2={}  
for k,v in d1.items():
  d2[removal(k)] = v
  
print(d2)

=================================================================================
#Write a Python program to get the top three items in a shop.

items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
def topvalues(l1,n):
  l2=sorted(l1, key=l1.get ,reverse=True)
  for i in range(n):
    print(l1[l2[i]])
    
topvalues(items,3)

=================================================================================
#Write a Python program to get the key, value and item in a dictionary.
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
for (k,v) in enumerate(dict_num.items()):
  print(k,*v)
  
=================================================================================
#Write a Python program to print a dictionary line by line.

students = {'Aex':{'class':'V','rolld_id':2},'Puja':{'class':'V','roll_id':3}}
for k,v in students.items():
  print(k)
  for i,j in v.items():
    print(i,j)
	
=================================================================================
#Write a Python program to check multiple keys exists in a dictionary.
student = {  'name': 'Alex', 'class': 'V','roll_id': '2'}

def checkkeys(*args):
  for i in args:
    if i not in list(student.keys()):
      return False
  return True
  
print( checkkeys( "name","class" )  )
print( checkkeys( "name","cv" )  )
=================================================================================
#Write a Python program to count number of items in a dictionary value that is a list.
d1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
count=0
for v in d1.values():
  count+=len(v)
print(count)
=================================================================================
#Write a Python program to sort Counter by value.

l1=[('Chemistry', 87), ('Physics', 83), ('Math', 81), ('Chemistry', 87),  ('Math', 81), ('Math', 81)]
from collections import Counter
print(Counter(l1).most_common())
=================================================================================
#Write a Python program to create a dictionary from two lists without losing duplicate values.

class_list = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
id_list = [1, 2, 2, 3]
d1={}
for k,v in zip(class_list,id_list):
  d1[k]=v
print(d1)	

=================================================================================
#Write a Python program to replace dictionary values with their sum.

student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]

def average(d1):
  for i in student_details:
    i['average'] = (i['V']+i['VI'])/2
    i.pop('V')
    i.pop('VI')
  return d1
    
print(average(student_details))

=================================================================================

#Write a Python program to match key values in two dictionaries.
x = {'key1': 1, 'key2': 3, 'key3': 2}
y = {'key1': 1, 'key2': 2}

for k,v in y.items():
  if (k,v) in x.items():
    print("{0}:{1} is present in both dict".format(k,v))
