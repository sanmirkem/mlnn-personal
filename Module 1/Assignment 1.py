#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[8]:


a = "hello "
b = "world "
c = " what's up?"


# In[10]:


print(a + b + c)


# In[2]:


import numpy
import pandas
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pylab as plt


# In[ ]:





# In[3]:


plt.scatter([3,2,5], [1,2,3])


# In[1]:


x = float(input("Enter a number for x:"))
y = float(input("Enter a number for y:"))
if x==y:
    print("Yay they are equal")
if y!=x:
    print ("Therefore x/y is", x/y)

