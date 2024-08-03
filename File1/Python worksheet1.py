#!/usr/bin/env python
# coding: utf-8

#                        PYTHON WORKSHEET 1

# ***Q11 to Q15 are programming questions. Answer them in Jupyter Notebook.
# 

# 11.	Write a python program to find the factorial of a number.
# 

# In[15]:


num= int(input("Enter any number of which you want to find the factorial\n"))

factorial=1

#lets check if the number is positice negative or zero.
if num<0:
    print("sorry, factorial doesn't exist for negative number.")
elif num==0:
        print("The factorial of 0 is 1.")
else:
    for i in range(1, num+1):
            factorial = factorial*i
    print("The Factorial of ", num, "is", factorial)   


#   

# 12.	Write a python program to find whether a number is prime or composite.

# In[16]:


num= int(input("Enter any number:"))
count=0
i=1
while i<=num:
    if num%i==0:
        count=count+1
    i=i+1    

if(count==2):
    print(num, "is a Prime number")

elif(count>=3):
    print(num, "is a composite number")

else:
    print(num, "is neither prime nor composite")
        


#   

# 13.	Write a python program to check whether a given string is palindrome or not.

# In[2]:


string= input("Enter string:")

if (string == string[::-1]):
     print("The String is a Palindrome")
else:
     print("The String isn't a Palindrome")


#    

#  14. Write a Python program to get the third side of right-angled triangle from two given sides.

# In[3]:


# lets take the sides of right angled traingle as Perpendicular(P), base(b) and hypotenuse(h)

import math
P= float(input("Enter height of traingle:"))
B= float(input("Enter base lenght of triangle:"))

H= math.sqrt(P**2 + B**2)

print("Hypotenuse of Traingle is", H)



#      

# 15. Write a python program to print the frequency of each of the characters present in a given string.

# In[4]:


# Taking string as a input
str= input("Enter String:")
# print(str)

#Transferring that particular string into a list
l=list(str)

# print list of occurance of each character
freq = [l.count(ele) for ele in l]
#print(freq)

# creating disctionary to store a word and its occurances

d= dict(zip(l, freq))
print(d)


# In[ ]:




