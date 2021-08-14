# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 20:56:40 2021

@author: Admin
"""
input1=21


key_words=["<5lakh","5lakh-15lakh","15lakh-20lakh","20lakh>"]
numbers = []
for i in key_words:
    numbers.append(i.replace('lakh',''))
    
digit=[]
operator=[]
for i in numbers:
    for k in i:
        if k.isdigit():
            digit.append(k)
        else:
            operator.append(k)
for i in range(len(operator)):
   numbers[i]= numbers[i].replace(operator[i],'t')
num=[]
for i in range(len(numbers)):
    num.append(tuple(numbers[i].split('t')))
count=0
for i in num:
    if(i[0]==""):
        if(input1<int(i[1])):
            index=0
    elif(i[1]==""):
        if(input1>int(i[0])):
            index=-1
    else:
        if(int(i[0])<input1)&(int(i[1])>input1):
            index=count
    count+=1
print(key_words[index])