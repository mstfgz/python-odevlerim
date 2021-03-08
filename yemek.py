# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 21:29:17 2021

@author: sandıklıtso
"""

yemek = int(input("Lütfen yemek ücretini giriniz?"))

vergi1 = (yemek*0.08)

yemekHam = (yemek-vergi1)

bahşiş1 = (yemekHam*0.10)

vergi = round(vergi1,2)
yemek2 = round(yemekHam,2)
bahşiş = round(bahşiş1,2)
toplam = vergi + yemek2 + bahşiş
print ("yemek bedeli :" + str(yemek2) + " TÜRK LİRASI")
print("vergi :" + str(vergi) + " TÜRK LİRASI")
print("bahşiş :" + str(bahşiş) + " TÜRK LİRASI")
print("toplam :" + str(toplam) + " TÜRK LİRASI'dır.")