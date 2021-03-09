# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 21:02:30 2021

@author: sandıklıtso
"""



list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]

list3 = list1 + list2
print("birleştirilmiş liste :",list3)


list4 = [i*2 for i in list3]

list4.sort()
print("her bir liste elemanının ikiyle çarpılarak sıralanmış listesi" ,list4)

i=0

while (i < len(list4)):

  print(i, "th item: ","[",list4[i],"]", " type:", type(list4[i]))
  i+=1


