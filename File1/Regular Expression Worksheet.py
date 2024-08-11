#!/usr/bin/env python
# coding: utf-8

# # RE PRACTICE QUESTIONS

# In[13]:


import re


# Question 1- Write a RegEx pattern in python program to check that a string 
# contains only a certain set of characters (in this case a-z, A-Z and 0-9).

# In[ ]:


# As the above question states to search whether the string contains
# a-z, A-Z and 0-9, so its output will be true or False if the codition is true

string= input("Enter any string: ")
matches= bool(re.search("^[\w+]*$", string))

print(matches)


# Note: The above program only checks for alphabets abd numbers excluding spaces

#    

# Question 2- Write a RegEx pattern that matches a 
# string that has an a followed by zero or more b's

# In[ ]:


string= input("Enter any string: ")
pattern= r'^a(b*)$'
matches= bool(re.search(pattern, string))

print(matches)


#   

# Question 3-  Write a RegEx pattern that matches a string that has
# an a followed by one or more b's

# In[ ]:


string= input("Enter any string: ")
pattern= r'ab+'
matches= bool(re.search(pattern, string))

print(matches)


#    

# Question 4- Write a RegEx pattern that matches a string that has an a followed by zero or one 'b'.

# In[ ]:


string= input("Enter any string: ")
pattern= r'ab?'
matches= bool(re.search(pattern, string))

print(matches)


#   

# Question 5- Write a RegEx pattern in python program that matches a string that has an 'a' followed by three 'b'.

# In[ ]:


string= input("Enter any string: ")
pattern= r'ab{3}?'
matches= bool(re.search(pattern, string))

print(matches)


#    

# Question 6- Write a RegEx pattern in python program that matches a string that has an 'a' followed by two to three 'b'.

# In[ ]:


string= input("Enter any string: ")
pattern= r'ab{2,3}?'
matches= bool(re.search(pattern, string))

print(matches)


#   

# Question 7- Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# In[ ]:


string= input("Enter any string: ")
pattern= r'a.*?b$'
matches= bool(re.search(pattern, string))

print(matches)


#   

# Question 8- Write a RegEx pattern in python program that matches a word at the beginning of a string.

# In[ ]:


string= input("Enter any string: ")
pattern= r'^\w+'
matches= bool(re.search(pattern, string))

print(matches)


# In[ ]:


#Note: Above program make sure the string staring should not be blank or space. It should be start with the word.


#   

# Question 9- Write a RegEx pattern in python program that matches a word at the end of a string.

# In[ ]:


import re
string= input("Enter any string: ")
pattern= r'.*\w+$'
matches= bool(re.search(pattern, string))

print(matches)


# In[ ]:


#Note: The above program make sures that the string we enter should end with any word instead of any space, symbol or special character


#   

# Question 10- Write a RegEx pattern in python program to find all words that are 4 digits long in a string.
# Sample text- '01 0132 231875 1458 301 2725.'
# Expected output- ['0132', '1458', '2725']
# 

# In[ ]:


import re
string= input("Enter any string:")
pattern= '\d{4}'


matches= re.findall(pattern, string)
print(matches)


# In[ ]:





# In[ ]:




