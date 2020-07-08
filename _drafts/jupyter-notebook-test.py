# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,1000)
plt.plot(x,np.sin(x))
plt.show()


# %%
msg = "Hello World"
print(msg)
print("add a new line")


# %%
import sys
print sys.version

# %% [markdown]
# ~~markdown~~
# 
# > test1  
# > test2  
# 
# > test3 
# 
# * line item 1
# * line item 2
# 
# **italy**
# 
# ***cold***
# 
# - [ ] test 
# - [x] add
# 
# 
