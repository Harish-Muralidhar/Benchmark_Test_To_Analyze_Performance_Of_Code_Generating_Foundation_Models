
In the third example,
You will need to paint 2 balloons. You can either first paint the first balloon, or the first two balloon. In both the cases, 2 flips are required.

# In[1]:


n = int(input())
for i in range (n):
    s = input()
    c = s.count("a")
    if c > (len(s)-c):
        print(len(s)-c)
    else:
        print(c)


# In[ ]: