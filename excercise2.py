#!/usr/bin/env python
# coding: utf-8

# In[32]:


import random
n = int(input())
l = [i for i in range(1, n**2 +1)]
random.shuffle(l)

table = [0 for i in range(n)]
j = 0
for i in range(n):
    table[i] = l[i +j:i +j + n]
    j += n-1
def print_table(table):
    for string in table:
        for element in string:
            print(element, end = ' ')
           
        print()
        

def sort(table):
    summ =[]    
    t = table
   
    for i in range(n):
        sum_raw = 0
        for j in range(n):
            sum_raw += table[i][j]
        summ.append(sum_raw) 
    t.append(summ)
    
    for k in range(n):
        min_i = k  
        for i in range(k, n):
            if t[n][i] <= t[n][min_i]:
                min_i = i
        a = t[n][k]
        t[n][k] = t[n][min_i]
        t[n][min_i] = a
        c = t[k]
        t[k] = t[min_i]
        t[min_i] = c
    return t[0:n]       
def row_to_col(table):
    t = [[i for i in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            t[j][i] = table[i][j]
    return t        
            
    
    
    
    
    
    
    
    
print_table(table)
print()
res = sort(row_to_col(table))

print_table(sort(row_to_col(res)))                


# In[ ]:




