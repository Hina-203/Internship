#!/usr/bin/env python
# coding: utf-8

#                                   Regular Expressions

# Question 1- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
# Sample Text- 'Python Exercises, PHP exercises.'
# Expected Output: Python:Exercises::PHP:exercises:
# 

# In[ ]:


import re
str= input("Enter any string:")
replace_str= re.sub(r"[, .]", ":", str)
print(replace_str)



#   

# Question 2-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
# Dictionary- {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
# Expected output-
# 0      hello world
# 1             test
# 2    four five six
# 

# In[ ]:


import pandas as pd
d1={
     'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']
     }
df = pd.DataFrame(d1)
df['SUMMARY'] = df['SUMMARY'].apply(lambda x: re.sub(r'[^a-zA-Z\s]', '', x))
df['SUMMARY']


#   

# Question 3- Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory.

# In[ ]:


def four_words_long(text):
    pattern= re.compile(r'\b\w{4,}\b')
    matches= pattern.findall(text)
    return matches
    


# In[38]:


four_words_long("here is the Superhero spiderman")


#    

# Question 4- Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

# In[ ]:


def words_length(text):
    pattern= re.compile(r'\b\w{3,5}\b')
    matches= pattern.findall(text)
    return matches


# In[43]:


words_length("here is the Superhero spiderman")


#    
#    

# In[ ]:


Question 5- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output:
example.com
hr@fliprobo.com
github.com
Hello Data Science World


# In[79]:


import re

def remove_pare(strings):
    pattern = re.compile(r"\(\)")
    return [pattern.sub('', string).strip() for string in strings]


# In[ ]:





# In[71]:


Question 6- Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
Sample Text: ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
Expected Output: ["example", "hr@fliprobo", "github", "Hello", "Data"]
Note- Store given sample text in the text file and then to remove the parenthesis area from the text.


# In[ ]:


import re

# Read the text file and store its content in a variable
with open('filename.txt', 'r') as file:
     text = file.read()

# Use regular expressions to remove the parenthesis area
modified_text = re.sub(r'\([^()]*\)', '', text)

# Save the modified text back to the text file
with open('filename.txt', 'w') as file:
    file.write(modified_text)
    


#   
#   

# Question 7- Write a regular expression in Python to split a string into uppercase letters.
# Sample text: “ImportanceOfRegularExpressionsInPython”
# Expected Output: [‘Importance’, ‘Of’, ‘Regular’, ‘Expression’, ‘In’, ‘Python’]
# 

# In[82]:


import re
text = input("Enter any string:")
print(re.findall('[A-Z][^A-Z]*', text))


#   

# Question 8- Create a function in python to insert spaces between words starting with numbers.
# Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython"
# Expected Output: RegularExpression 1IsAn 2ImportantTopic 3InPython
# 

# In[9]:


import re

def insert_spaces(text):
  # Use regular expression to find words starting with numbers
  pattern = r'(\d+)([A-Za-z]+)'
  result = re.sub(pattern, r'\1 \2', text)
  return result


# In[4]:


insert_spaces("RegularExpression1IsAn2ImportantTopic3InPython")


#   

# Q9:Create a function in python to insert spaces between words starting with capital letters or with numbers. Sample Text: “RegularExpression1IsAn2ImportantTopic3InPython" Expected Output:  RegularExpression 1 IsAn 2 ImportantTopic 3 InPython 

# In[14]:


import re

def insert_spaces(text):
  # Use regular expression to find words starting with capital letters or numbers
  pattern = r'([A-Z][a-z0-9]+|\d+)'
  # Replace the matched words with a space followed by the word
  result = re.sub(pattern, r' \1', text)
  # Remove any leading or trailing spaces
  result = result.strip()
  return result


#  

# Question 10- Use the github link below to read the data and create a dataframe. After creating the dataframe extract the first 6 letters of each country and store in the dataframe under a new column called first_five_letters.
# Github Link-  https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv
# 

# In[16]:


import pandas as pd

url = "https://raw.githubusercontent.com/dsrscientist/DSData/master/happiness_score_dataset.csv"
df = pd.read_csv(url)

df['first_five_letters'] = df['Country'].apply(lambda x: x[:6])


# In[17]:


df['first_five_letters']


#   

# Question 11- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

# In[21]:


import re

def match_string(string):
  pattern = r'^[a-zA-Z0-9_]+$'
  if re.match(pattern, string):
    print("String matches the pattern")
  else:
     print("String does not match the pattern")



# In[22]:


# Example usage
match_string("Hello_World123")  
match_string("Hello World")   


#     

# Question 12- Write a Python program where a string will start with a specific number. 

# In[26]:


def check_starting_number(string, number):
  if string.startswith(str(number)):
    return True
  else:
    return False

# Example usage
string = "123abc"
number = 123

if check_starting_number(string, number):
    print("The string starts with the specified number.")
else:
    print("The string does not start with the specified number.")


#  

# Question 13- Write a Python program to remove leading zeros from an IP address
# 

# In[27]:


def remove_leading_zeros(ip_address):
    # Split the IP address into its octets
    octets = ip_address.split('.')
    # Remove leading zeros by converting each octet to an integer and back to a string
    cleaned_octets = [str(int(octet)) for octet in octets]
    # Join the cleaned octets back into a single IP address string
    cleaned_ip_address = '.'.join(cleaned_octets)
    return cleaned_ip_address


# In[28]:


ip = "192.168.001.002"
print(remove_leading_zeros(ip))  # Output: 192.168.1.2


#   

# Question 14- Write a regular expression in python to match a date string in the form of Month name followed by day number and year stored in a text file.
# 
# Sample text :  ' On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’.
# Expected Output- August 15th 1947
# Note- Store given sample text in the text file and then extract the date string asked format.
# 

# In[30]:


import re

text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country."

pattern = r"\b([A-Z][a-z]+ \d{1,2}(?:st|nd|rd|th)? \d{4})\b"

matches = re.findall(pattern, text)
date_string = matches[0] if matches else None

print(date_string)


#   

# Question 15- Write a Python program to search some literals strings in a string. 
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox', 'dog', 'horse'
# 
# 

# In[34]:


# Sample text
text = 'The quick brown fox jumps over the lazy dog.'

# Searched words
searched_words = ['fox', 'dog', 'horse']

# Iterate over each searched word
for word in searched_words:
  # Check if the word is present in the text
  if word in text:
    print(f"The word '{word}' is found in the text.")
else:
    print(f"The word '{word}' is not found in the text.")


#   

# Question 16- Write a Python program to search a literals string in a string and also find the location within the original string where the pattern occurs
# Sample text : 'The quick brown fox jumps over the lazy dog.'
# Searched words : 'fox'
# 
# 

# In[35]:


import re
pattern = 'fox'
text = 'The quick brown fox jumps over the lazy dog.'
match = re.search(pattern, text)
s = match.start()
e = match.end()
print('Found "%s" in "%s" from %d to %d ' % \
    (match.re.pattern, match.string, s, e))


#   

# Question 17- Write a Python program to find the substrings within a string.
# Sample text : 'Python exercises, PHP exercises, C# exercises'
# Pattern : 'exercises'

# In[36]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.findall(pattern, text):
    print('Found "%s"' % match)


#   

# Question 18- Write a Python program to find the occurrence and position of the substrings within a string.

# In[37]:


import re
text = 'Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))



#   

# Question 19- Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.
# 

# In[38]:


import re
def change_date_format(dt):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
dt1 = "2026-01-02"
print("Original date in YYY-MM-DD Format: ",dt1)
print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


#   

# Question 20- Create a function in python to find all decimal numbers with a precision of 1 or 2 in a string. The use of the re.compile() method is mandatory.
# Sample Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
# Expected Output: ['01.12', '145.8', '3.01', '27.25', '0.25']
# 

# In[41]:


import re

def find_decimal_numbers(string):
  pattern = re.compile(r'\d+\.\d{1,2}')
  decimal_numbers = re.findall(pattern, string)
  return decimal_numbers

sample_text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
output = find_decimal_numbers(sample_text)
print(output)


#   

# Question 21- Write a Python program to separate and print the numbers and their position of a given string.
# 

# In[43]:


import re
# Input.
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."

for m in re.finditer("\d+", text):
    print(m.group(0))
    print("Index position:", m.start())


#  

# Question 22- Write a regular expression in python program to extract maximum/largest numeric value from a string.
# Sample Text:  'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'
# Expected Output: 950
# 

# In[44]:


import re

input_string = 'My marks in each semester are: 947, 896, 926, 524, 734, 950, 642'

numeric_values = re.findall(r'\d+', input_string)
numeric_values = [int(value) for value in numeric_values]

max_value = max(numeric_values)

print(max_value)


#   

# Question 23- Create a function in python to insert spaces between words starting with capital letters.
# Sample Text: “RegularExpressionIsAnImportantTopicInPython"
# Expected Output: Regular Expression Is An Important Topic In Python

# In[46]:


import re

def insert_spaces(text):
  # Use regular expression to find words starting with capital letters
  pattern = r'([A-Z][a-z]+)'
  # Replace the found words with the same word followed by a space
  result = re.sub(pattern, r' \1', text)
  # Remove any leading or trailing spaces
  result = result.strip()
  return result

sample_text = "RegularExpressionIsAnImportantTopicInPython"
output = insert_spaces(sample_text)
print(output)


#    

# Question 24- Python regex to find sequences of one upper case letter followed by lower case letters
# 

# In[50]:


import re
def text_match(text):
        patterns = '[A-Z]+[a-z]+$'
        if re.search(patterns, text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("Human"))
print(text_match("Hooman"))
print(text_match("hooman"))
print(text_match("HOOMAN"))


#   

# Question 25- Write a Python program to remove continuous duplicate words from Sentence using Regular Expression.
# Sample Text: "Hello hello world world"
# Expected Output: Hello hello world

# In[51]:


import re

def remove_duplicates(sentence):
  pattern = r'\b(\w+)(\s+\1\b)+'
  result = re.sub(pattern, r'\1', sentence)
  return result

# Example usage
sentence = "Hello hello world world"
output = remove_duplicates(sentence)
print(output)


#  

# Question 26-  Write a python program using RegEx to accept string ending with alphanumeric character.

# In[78]:


import re

def check_string(string):
    pattern = r"\w$"
    match = re.search(pattern, string)
    if match:
        return True
    else:
        return False

# Example usage
input_string = input("Enter a string: ")
if check_string(input_string):
    print("String ends with an alphanumeric character")
else:
    print("String does not end with an alphanumeric character")


#    

# Question 27-Write a python program using RegEx to extract the hashtags.
# Sample Text:  """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
# Expected Output: ['#Doltiwal', '#xyzabc', '#Demonetization']
# 
# 

# In[70]:


import re

def extract_hashtags(text):
  hashtags = re.findall(r'#\w+', text)
  return hashtags

# Sample text
text = 'RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo'

# Extract hashtags
hashtags = extract_hashtags(text)

# Print the extracted hashtags
print(hashtags)


#   

# Question 28- Write a python program using RegEx to remove <U+..> like symbols
# Check the below sample text, there are strange symbols something of the sort <U+..> all over the place. You need to come up with a general Regex expression that will cover all such symbols.
# Sample Text: "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
# Expected Output: @Jags123456 Bharat band on 28??<ed><ed>Those who  are protesting #demonetization  are all different party 

# In[71]:


import re

input_text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who are protesting #demonetization are all different party leaders"

pattern = r"<U\+\w{4}>"
output_text = re.sub(pattern, "", input_text)

print(output_text)


#  

# Question 29- Write a python program to extract dates from the text stored in the text file.
# Sample Text: Ron was born on 12-09-1992 and he was admitted to school 15-12-1999.
# Note- Store this sample text in the file and then extract dates.

# In[74]:


import re
def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/"
print(extract_date(url1))


#   

# Question 30- Create a function in python to remove all words from a string of length between 2 and 4.
# The use of the re.compile() method is mandatory.
# Sample Text: "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
# Expected Output:  following example creates ArrayList a capacity elements. 4 elements added ArrayList ArrayList trimmed accordingly.
# 

# In[77]:


import re

def remove_words(string):
    pattern = re.compile(r'\b\w{2,4}\b')
    modified_string = re.sub(pattern, '', string)
    return modified_string

sample_text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
output = remove_words(sample_text)
print(output)


# In[ ]:





# In[ ]:




