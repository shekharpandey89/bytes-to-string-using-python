#!/usr/bin/env python
# coding: utf-8

# # Method 1: Using the map () function

# In[4]:


byte = [97, 99, 100]
  
s = ''.join(map(chr, byte))
print(s)


# # Method 2: Using decode () function

# In[5]:


#convert bytes to string using decode()
 
str = b'blogs linuxhint'
print(str)
print(type(str))
 
# now converting bytes to string
output = str.decode()

print('\nOutput:')
print(output)
print(type(output))


# # Method 3: Using codecs () function to convert the bytes to string

# In[12]:


#convert bytes to string using codecs()
import codecs
str = b'blogs linuxhint'
print(str)
print(type(str))
 
# now converting bytes to string
output = codecs.decode(str)

print('\nOutput:')
print(output)
print(type(output))

