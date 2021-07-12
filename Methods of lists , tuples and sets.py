#!/usr/bin/env python
# coding: utf-8

# In[2]:


List1 = ['python','c']
List1.append('java')
print(List1)


# In[4]:


List1 = ["python","c","java"]
List2 = ["Mysql","Html","tableau"]
List1.append(List2)
print(List1)


# In[5]:


List = ['python','c','java']
List.clear()
print(List)


# In[6]:


List = ['python','c','java']
x = List.copy()
print(x)


# In[7]:


List = ['python','c','java']
x = List.count('java')
print(x)


# In[9]:


nums = [1,2,3,4,5,6,2,4,6,8,4,2]
x = nums.count(4)
print(x)


# In[10]:


fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)


# In[11]:


fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)
print(fruits)


# In[13]:


List = ['python','c','java']
x = List.index("c")
print(x)


# In[14]:


List = ['python','c','java']
List.insert(3,'c++')
print(List)


# In[16]:


List = ['python','c','java']
x = List.pop(1)
print(x)


# In[17]:


List = ["python","c","java"]
List.remove("python")
print(List)


# In[18]:


List = ["python","c","java"]
List.reverse()
print(List)


# In[20]:


List = ["python","c","java"]
List.sort()
print(List)


# In[21]:


#Tuple methods
Tuple = (1,2,4,8,9,6,4,2,8,6,9)
x = Tuple.count(8)
print(x)


# In[22]:


Tuple = (1,2,4,8,9,6,4,2,8,6,9)
x = Tuple.index(8)
print(x)


# In[23]:


#sets methods
sub = {"phy","math","bio"}
sub.add("chem")
print(sub)


# In[24]:


set = {"phy","math","bio"}
set.clear()
print(set)


# In[25]:


set = {"phy","math","bio"}
x = set.copy()
print(x)


# In[26]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.difference(y)

print(z)


# In[27]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = y.difference(x)

print(z)


# In[28]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y)

print(x)


# In[29]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) 

print(z)


# In[31]:


x = {2,4,6,8,9,12,14,24}
y ={2,6,8}
z = y.issubset(x)
print(z)


# In[32]:


x = {2,6,8}
y = {2,4,6,8,9,12,14,16}
z = x.issubset(y)
print(z)


# In[33]:


set = {"phy","math","chem"}
set.discard("math")
print(set)


# In[34]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)

print(z)


# In[35]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


# In[36]:


x = {2,6,8}
y = {2,4,6,8,9,12,14,16}
z = y.issuperset(x)
print(z)


# In[37]:


x = {2,4,6,8,9,12,14,24}
y ={2,6,8}
z = x.issuperset(y)
print(z)


# In[38]:


set={"phy","math","bio"}
set.pop()
print(set)


# In[39]:


set = {"phy","math","bio"}
set.remove("bio")
print(set)


# In[40]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# In[41]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)


# In[42]:


x = {1,2,4,6,8,}
y = {2,4,6}
z = x.union(y)
print(z)


# In[43]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)

print(x)


# In[ ]:




