# coding: utf-8

# In[1]:


def count_pairs_soln(L):
    assert type(L)==list

    from itertools import combinations
    L2=sorted(L)
    count=0
    for a,b in combinations(L,2):
        if a-b==1 or b-a==1:
            count+=1
    return count

