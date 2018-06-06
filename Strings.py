#Write a Python program to calculate the length of a string.

def string_length(str1):
  return len(str1)
print(string_length('w3resource.com'))
=============================================================================
#Write a Python program to count the number of characters (character frequency) in a string. 

def char_frequency(str1):
  d1={}
  for i in str1:
    d1[i]=d1.get(i,0)+1
  return d1

print(char_frequency('google.com'))

=============================================================================
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#If the string length is less than 2, return instead of the empty string.

def stringtrim(s1):
  if len(s1)<2:
    return ''
  else:
    return s1[:2]+s1[-2:]
  
  
print(stringtrim('w3resource'))
print(stringtrim('w3r'))
print(stringtrim('w3'))
print(stringtrim('w'))
=============================================================================
#Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
def change_char(s1,n):
  if n not in s1:
    return " char {0} not found".format(n)
  else:
    s2=''
    for i in s1:
      if i not in s2:
        s2+=i
      else:
        s2+='$'
    return s2
    
print(change_char("snehas" , 's'))

=============================================================================
#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. 
def change(s1,s2):
  return s2[:2] + s1[2] , s1[:2] + s2[2]

print(change('abc', 'xyz'))


=============================================================================
#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.

def change(s1):
  if len(s1)<3:
    return s1
  else:
    if s1[-3:] =='ing':
      s1+='ly'
    else:
      s1=s1 +'ing'
    return s1
    
print(change('ab'))
print(change('abc'))
print(change('string'))
=============================================================================
#Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'bad' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
def change(s1):
  n=s1.find('not')
  p=s1.find('poor')
  if p > n:
    s1=s1[:n] + "bad" + s1[p+4:]
    
  return s1
  
print( change(" The guy is not that poor")  )
print( change(" The guy is not poor!")  )
print( change(" The guy is poor but not that much")  )

=============================================================================
#Write a Python function that takes a list of words and returns the length of the longest one.

def longest_word(list1):
  return max( list1 , key=len )
  
print(longest_word(["PHP", "Exercises", "Backend"]))
=============================================================================
#Write a Python program to remove the nth index character from a nonempty string. 
def remove_char(s1 , n):
  return s1[ : n]+ s1[n+1:]
  
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))

=============================================================================
#Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
def exchange(s1):
  return s1[-1]+s1[1:-1]+s1[0]
  
print(exchange("EXCHANGE"))
print(exchange("12345"))

=============================================================================
#Write a Python program to remove the characters which have odd index values of a given string.
def odd_values_removal(s1):
  return s1[::2]


print(odd_values_removal('abcdef'))
print(odd_values_removal('python'))
=============================================================================

# Write a Python program to count the occurrences of each word in a given sentence.
def word_count(line1):
  list1=line1.split()
  d1=dict()
  for i in list1:
    d1[i]=d1.get( i , 0) +1
  return d1

print( word_count('the quick brown fox jumps over the lazy dog.'))
=============================================================================
#Write a Python script that takes input from the user and displays that input back in upper and lower cases.

def upper_lower(s1):
  return s1.upper() , s1.lower()
  
  
print(upper_lower("Python Programming!!!!"))
=============================================================================
#Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

items = input("Input comma separated sequence of words")

items1=sorted([ i for i in items.split(',') if items.count(i) == 1 ])

print(items1)
=============================================================================
#Write a Python function to create the HTML string with tags around the word(s). 

def add_tags(tag,data):
  return "<{0}> {1} </{2}>".format(tag , data , tag)


print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
=============================================================================
#Write a Python function to insert a string in the middle of a string.

def insert_sting(s1 , s2):
  return s1[:(len(s1)//2)] + s2 + s1[(len(s1)//2):] 
  
  
print(insert_sting('[[]]', 'Python'))
print(insert_sting('{{}}', 'PHP'))
print(insert_sting('<<>>', 'HTML'))
print(insert_sting('ORORO', 'HTML'))
=============================================================================
#Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).

def copies(s1):
  if len(s1)<2:
    return "length of string is less than 2"
  else:
    return s1[-2:] * 4


print(copies('Python'))
print(copies('Exercises'))
=============================================================================
#Write a Python function to get a string made of its first three characters of a specified string.
#If the length of the string is less than 3 then return the original string.

def trim(s1):
  if len(s1)<=3:
    return s1
  else:
    return s1[:3]


print(trim('ipy'))
print(trim('python'))
print(trim('py'))

=============================================================================
#Write a Python program to get the last part of a string before a specified character.

def part(s1 ,s2):
  return s1[:s1.rfind(s2)]
  
  
str1 = 'https://www.w3resource.com/python-exercises/string'

print(part(str1,'/'))
print(part(str1,'-'))
print(part(str1,'www'))

=============================================================================
#Write a Python function to reverses a string if it's length is a multiple of 4.

def reverse_string(s1):
  if len(s1) % 4 ==0 : 
    return s1[:: -1]
  return s1
  
  
print(reverse_string('abcd'))
print(reverse_string('python'))

=============================================================================
#Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 

def convert(s1):
  c=0
  for i in s1[:4]:
    if i.isupper():
      c=c+1
      
  if c>=2:
    return s1.upper()
  return s1
  
print(convert('Python'))
print(convert('PyThon'))
=============================================================================
#Write a Python program to sort a string lexicographically.

def lexicographi_sort(s1):
  return sorted(list(s1))


print(lexicographi_sort('w3resource'))
print(lexicographi_sort('quickbrown'))
=============================================================================
#Write a Python program to remove a newline in Python. 

str1='Python\nExercises\n'
print( str1 , str1.strip('\n') )
=============================================================================
#Write a Python program to check whether a string starts with specified characters

def starts(s1,s2):
  return s1.startswith(s2)

print(starts("w3resources.com" , "w3r"))
=============================================================================
#Write a Python program to create a Caesar encryption.

def encryption(s1):
  result=''
  for i in s1:
    j=ord(i)
    j=j+2
    result +=chr(j)
  return result
    
print(encryption("abc"))
=============================================================================
#Write a Python program to display formatted text (width=50) as outpu

sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
  
width1=50 
print( "{0} < width".format(sample_text ,width=50) )

=============================================================================
#Write a Python program to remove existing indentation from all of the lines in a given text. 
import textwrap

sample_text = '''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''
output= textwrap.dedent(sample_text)
print(output)

=============================================================================
#Write a Python program to add a prefix text to all of the lines in a string

sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted,
    dynamic programming language. Its design philosophy emphasizes
    code readability, and its syntax allows programmers to express
    concepts in fewer lines of code than possible in languages such
    as C++ or Java.
    '''

for i in sample_text.strip(' ').strip('\n').split('\n'):
  print(">" + i.strip())
  
=============================================================================
#Write a Python program to set the indentation of the first line. 

import textwrap
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()
print(textwrap.fill(text1,initial_indent='',subsequent_indent=' ' * 4,width=80,))

=============================================================================
#Write a Python program to print the following floating numbers upto 2 decimal places.
x = 3.1415926
y = 12.9999

print( "%.2f %.2f" %(x,y)  )

OR

x = 3.1415926
y = 12.9999
print( "{:.2f}".format(x) + " " +  "{:.2f}".format(y))
=============================================================================
#Write a Python program to print the following floating numbers upto 2 decimal places with a sign.

x = 3.1415926
y = -12.9999

print("{:+.2f}".format(x) + " " + "{:.2f}".format(y))

OR

x = 3.1415926
y = -12.9999

def formatting(x):
  if x<=0:
    print("{:.2f}".format(x))
  else:
     print("{:.2f}".format(x))
     
formatting(x)
formatting(y)
=============================================================================
#Write a Python program to print the following floating numbers with no decimal places.

x = 3.1415926
y = -12.9999

print("{:.0f}".format(x))
print("{:.0f}".format(y))
=============================================================================
#Write a Python program to print the following integers with zeros on the left of specified width.

x = 3
y = 123

print( "{:0>2d}".format(x)  )
print( "{:0>4d}".format(y)  )
=============================================================================
#Write a Python program to print the following integers with '*' on the right of specified width.
x = 3
y = 123

print("{:*>4d}".format(x) ) # adds * towards left of x
print("{:*<4d}".format(x) ) # adds * towards right of x
=============================================================================
#Write a Python program to display a number with a comma separator. 
x=10000000
print( "{:,}".format(x) )

=============================================================================

#Write a Python program to display a number in left, right and center aligned of width 10.

x = 22

print( "{:>10d}".format(x))# Right Aligned
print( "{:<10d}".format(x))# Left Aligned
print( "{:10d}".format(x))# Right Aligned
print( "{:^10d}".format(x)) # Center Aligned


#Write a Python program to count occurrences of a substring in a string.

def occurence(s1,s2):
  return str1.count(s2)
  
str1 = 'The quick brown fox jumps over the lazy dog fox.'

print(occurence( str1 , 'fox' ) )

#Write a Python program to reverse a string.

def reverse_string(s1):
  return s1[::-1]
  
  
print(reverse_string("abcdef"))
print(reverse_string("Python Exercises."))


#Write a Python program to reverse words in a string.
def  reverse_string_words(s1):
  for i in s1.split(' ')[::-1]:
    print(i, end=' ')
  print()


reverse_string_words("The quick brown fox jumps over the lazy dog.")
reverse_string_words("Python Exercises.")


#Write a Python program to strip a set of characters from a string.
def strip_chars(s1 , s2):
  result=''
  for i in s1:
    if i not in s2:
      result=result+i
  return result
      
print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))

OR

def strip_chars(s1 , s2):
  return ''.join( [ i for i in s1 if i not in s2  ]  )
      
print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))


#Write a python program to count repeated characters in a string.


str1 = 'thequickbrownfoxjumpsoverthelazydog'

def counting(s1):
  d1=dict()
  for i in s1:
    d1[i]=d1.get(i , 0)+1
  
  for i in sorted(d1, key= d1.get , reverse=True):
    print(i , d1[i])
counting(str1)

#Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.

area = 1000.1234
volume = 1254.725
d1 = 2
d2 = 3

print("area {0:.{1}f}cm\u00b2".format(area,d1))
print("volume {0:.{1}f}cm\u00b3".format(volume,d2))

#Write a Python program to print the index of the character in a string.

def print_index(s1):
  for i in range(len(s1)):
    print(s1[i] , i)
    
str1 = "w3resource"
print_index(str1)

OR

def print_index(s1):
  for i,j in enumerate(s1):
    print(i,j)
    
str1 = "w3resource"
print_index(str1)

#Write a Python program to check if a string contains all letters of the alphabet.

input_string = 'The quick brown fox jumps over the lazy dog'

def alphabet_check(s1):
  d1=dict()
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  for i in input_string.lower():
    d1[i] = d1.get(i,0)+1
  for i in alphabet:
    if i not in d1.keys():
      return "{0} is not present".format(i)
  return "All Alphabets are present"
  
print(alphabet_check(input_string))

#Write a Python program to convert the words in string to a list.

str1 = "The quick brown fox jumps over the lazy dog."
print( str1.split( ' ')  )


#Write a Python program to lowercase first n characters in a string.
def lower_n(s1 , n):
  return s1[:n].lower() + s1[n:]
  
str1 = 'W3RESOURCE.COM'
print( lower_n( str1 , 5 ) )

#Write a Python program to swap comma and dot in a string.

def swap(s1):
  return amount.translate(amount.maketrans(',.','.,'))
    
  
print(swap("32.054,23"))

#Write a Python program to count and display the vowels of a given text.

vowels = "aeiuoAEIOU"
def count_vowels(s1):
	return len( [ i for i in s1 if i in vowels ]  )
	
print(count_vowels('w3resource'))

#Write a Python program to split a string on the last occurrence of the delimiter.

def split_string(s1,n):
	return str1.rsplit(',',n)
	
print(split_string( "r,e,s,o,u,r,c,e" , 1 ))
print(split_string( "r,e,s,o,u,r,c,e" , 2 ))
print(split_string( "r,e,s,o,u,r,c,e" , 3 ))
