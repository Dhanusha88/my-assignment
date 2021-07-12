#!/usr/bin/env python
# coding: utf-8

# In[5]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
dict.clear()
print(dict)


# In[6]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.copy()
print(x)


# In[7]:


x = ('key1', 'key2', 'key3')
y = 0

dict = dict.fromkeys(x, y)

print(dict)


# In[8]:


x = ('key1', 'key2', 'key3')
dict = dict.fromkeys(x)
print(dict)


# In[9]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.get("sec")
print(x)


# In[10]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.get("course", "BE")
print(x)


# In[11]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.items()
print(x)


# In[12]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.items()
dict["year"] = 3
print(x)


# In[13]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.keys()
print(x)


# In[14]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.keys()
dict["batch"] = 2019
print(x)


# In[18]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
dict.pop("Name")
print(dict)


# In[17]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.pop("Name")
print(x)


# In[19]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
dict.popitem()
print(dict)


# In[20]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.popitem()
print(x)


# In[21]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.setdefault("Name","Dhanusha")
print(x)


# In[22]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.setdefault("batch","2019")
print(x)


# In[23]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
dict.update({"batch": 2019})
print(dict)


# In[24]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.values()
print(x)


# In[25]:


dict = {
    "Name": "Dhanusha",
    "year": 2,
    "sec": "A"
}
x = dict.values()
dict["year"] = 2023
print(x)


# In[ ]:




