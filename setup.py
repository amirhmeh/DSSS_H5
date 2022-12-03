#!/usr/bin/env python
# coding: utf-8

# In[2]:


from distutils.core import setup
from setuptools import find_packages

setup(

    name = "snowflake",
    version = "0.1",
    author = "Amirhossein Mehrizi",
    packages = find_packages(),
    install_requires = ["numpy","turtles","random"],
)


# In[ ]:




