#!/usr/bin/env python
# coding: utf-8

# In[3]:


### Loop through the list ###

for names in["Jame","John","David","Rocky"]:
    print("Welcome to python",names)


# In[12]:


#check in list#
first_name =["James","John","David","Rocky"]
print("James" in first_name)
print("John" in first_name)
print("David" in first_name)
print("Mary" in first_name)
print("Rocky" in first_name)


# In[20]:


first_name =["James","John","David","Rocky"]

first_name=nick_name.copy()
first_name[1]="Bruce"
print(nick_name)


# In[23]:


first_name =["James","John","David","Rocky"]
last_name = ["Bob","ong","Max","Buld","linux"]
print(first_name + [22,4,58,3,4])
print(["Mango","Gauva","Grapes"]*5)


# In[26]:


# inserting elemrts by insert()

first_name=["James","John","David","Rocky"]
first_name.insert(0,"Bob")

first_name[1:3]=["Peka","Bean","Panther"]
print(first_name)


# In[ ]:




