#!/usr/bin/env python
# coding: utf-8

# In[36]:


base1 = int(input())
number1 = input()
number2 = input()
base2 = int(input())
n1 = []
n2 = []
for element in number1:
    n1.append(element)
for element in number2:
    n2.append(element)
alphabet = []

for i in range(48, 58):
    alphabet.append(chr(i))
for i in range(65, 91):
    alphabet.append(chr(i))    


dicti = {}
for i in range (0, len(alphabet)):
    dicti[alphabet[i]] = i
   

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
def to_decimal(num, base):
    num10 = 0
    for i in range(0, len(num)):
        num10 += dicti[num[i]]*(base**(len(num)-i-1))
    return num10
def to_base(num, base):
    answer = num
    rest = []
    if num / base < 1:
        result = get_key(dicti, num)
    else:
        while answer >= base:
            rest.append(get_key(dicti, answer % base))
            answer = answer // base
        rest.append(get_key(dicti, answer))
        rest.reverse()
        result = rest
    return result
    
    
final = to_base(to_decimal(n1, base1) + to_decimal(n2, base1), base2)    
for element in final:
    print(element, end = '')


# In[ ]:





# In[ ]:




