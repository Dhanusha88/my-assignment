#!/usr/bin/env python
# coding: utf-8

# In[1]:


Str = "hello, my name is dhanusha."
x = Str.capitalize()
print(x)


# In[2]:


Str = "Hello, Iam studying B.E ,CSE."
x = Str.casefold()
print(x)


# In[3]:


Str = "python"
x = Str.center(20)
print(x)


# In[4]:


Str = "python"
x = Str.center(20, "0")
print(x)


# In[5]:


Str = "plant a tree, tree gives us many things!"
x = Str.count("tree")
print(x)


# In[6]:


Str = "plant a tree, tree gives us many things!"
x = Str.count("tree",10,24)
print(x)


# In[7]:


txt = "My name is Ståle"

x = txt.encode()

print(x)


# In[8]:


txt = "My name is Ståle"

print(txt.encode(encoding="ascii",errors="backslashreplace"))
print(txt.encode(encoding="ascii",errors="ignore"))
print(txt.encode(encoding="ascii",errors="namereplace"))
print(txt.encode(encoding="ascii",errors="replace"))
print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))


# In[9]:


Str = "hello, my name is dhanusha."
x = Str.endswith(".")
print(x)


# In[11]:


Str = "hello, my name is dhanusha."
x = Str.endswith("my world.")
print(x)


# In[12]:


txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)


# In[13]:


txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


# In[15]:


Str = "hello, my name is dhanusha."
x = Str.find("name")
print(x)


# In[20]:


txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)


# In[22]:


txt = "Hello, welcome to my world."

print(txt.find("q"))
print(txt.index("q"))


# In[23]:


txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


# In[30]:


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)


# In[29]:


Str = "hello, my name is dhanusha."
x = Str.index("name")
print(x)


# In[31]:


Str = "hello, my name is dhanusha."
x = Str.index("d")
print(x)


# In[33]:


Str = "organization14"
x = Str.isalnum()
print(x)


# In[34]:


Str = "organization 14"
x = Str.isalnum()
print(x)


# In[35]:


Str = "organizationZ"
x = Str.isalpha()
print(x)


# In[36]:


Str = "organization11"
x = Str.isalpha()
print(x)


# In[37]:


txt = "\u0033" #unicode for 3

x = txt.isdecimal()

print(x)


# In[38]:


a = "\u0030" #unicode for 0
b = "\u0047" #unicode for G

print(a.isdecimal())
print(b.isdecimal())

Str = "20202"
x = Str.isdigit()
print(x)
# In[39]:


a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for ²

print(a.isdigit())
print(b.isdigit())


# In[40]:


Str = "sample"
x = Str.isidentifier()
print(x)


# In[41]:


a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


# In[44]:


Str = "hello world!"
x = Str.islower()
print(x)


# In[46]:


Str = "2468"
x = txt.isnumeric()
print(x)


# In[47]:


a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())


# In[49]:


Str = "i like candy #8?"
x = Str.isprintable()
print(x)


# In[52]:


Str = "i like ,\ncandy #8?"
x = Str.isprintable()
print(x)


# In[53]:


Str = "  "
x = Str.isspace()
print(x)


# In[54]:


Str = " d  "
x = Str.isspace()
print(x)


# In[55]:


Str = "I like candy !"
x = Str.isprintable()
print(x)


# In[56]:


a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())


# In[57]:


txt = "THIS IS NOW!"

x = txt.isupper()

print(x)


# In[58]:


a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())


# In[59]:


myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)


# In[61]:


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)


# In[62]:


Str = "pen"

x = Str.ljust(20)

print(x, "it is a pen.")


# In[65]:


Str = "Good morning EVERYONE"
x = Str.lower()
print(x)


# In[66]:


txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")


# In[67]:


txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)


# In[68]:


txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))


# In[69]:


txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = txt.maketrans(x, y)
print(txt.translate(mytable))


# In[70]:


txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = txt.maketrans(x, y, z)
print(txt.translate(mytable))


# In[71]:


txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(txt.maketrans(x, y, z))


# In[72]:


txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)


# In[73]:


Str = "we play volleyball"
x = Str.replace("volleyball","cricket")
print(x)


# In[74]:


txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)


# In[75]:


txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)


# In[76]:


txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)


# In[77]:


txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")


# In[78]:


txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)


# In[79]:


txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)


# In[81]:


Str = "phy, math, chem"
x = Str.rsplit(", ")
print(x)


# In[83]:


Str = "phy, math, chem"
x = Str.rsplit(", ", 1)
print(x)


# In[84]:


Str = "enter the dragon"
x = Str.split()
print(x)


# In[85]:


txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)


# In[86]:


txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)


# In[91]:


Str = "Hello, this is a string."
x = Str.startswith("Hello")
print(x)


# In[92]:


Str = "Hello, this is a string."
x = Str.startswith("thi", 7, 10)
print(x)


# In[93]:


txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")


# In[94]:


txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)


# In[95]:


Str = "Hi My Name Is DHANUSHA"
x = Str.swapcase()
print(x)


# In[96]:


Str = "Enter the Dragon"
x = Str.title()
print(x)


# In[97]:


Str = "hi d8d8d9 and a3a3a3a3"
x = Str.title()
print(x)


# In[98]:


dict = {40: 48}
Str = "Hi bean!"
print(Str.translate(dict))


# In[99]:


Str = "hello bean!"
table = Str.maketrans("S", "P")
print(Str.translate(table))


# In[100]:


Str = "hello bean!"
x = "mSa"
y = "eJo"
table = Str.maketrans(x, y)
print(Str.translate(table))


# In[101]:


txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))


# In[103]:


Str = " Hello everyone"
x = Str.upper()
print(x)


# In[104]:


Str = "40"
x = Str.zfill(10)
print(x)


# In[105]:


a = "hello"
b = "welcome to the college"
c = "10.000"
print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))


# In[ ]:




