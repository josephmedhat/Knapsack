# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 00:28:09 2019

@author: josep
"""

class Pair:
    def __init__(self,weight=0,benefit=0):
        self.weight=weight
        self.benefit=benefit
        
    def getData(self):
        print("({0},{1})".format(self.weight,self.benefit))
    
   
    