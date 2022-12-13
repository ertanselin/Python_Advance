# -*- coding: utf-8 -*-
""" Bu fonksiyon ile °C den °F'e veya
°F den °C ye birim dnüştürebilirsiniz.

Mesela:
donusm.Santigrat(100) 
bize 100°C değerinin °F değerinin döndürür.

Created on Sun Oct 23 12:14:31 2022
@author: Öğrenci
"""

def Santigrat_F(C):
    return (C*1.8)+32

def Fahrenheit_C(F):
    return (F-32)/1.8