# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 13:22:28 2019

@author: josep
"""
import random
class Gene :
    def __init__(self,size,length,items):
         self.length=length
         self.size=size
         self.items=items
         self.code=self.generateGene(length)
         self.pairs=self.getPairs()
         self.fitness=self.fitnessFunction()
         
    def getData(self):
        print("{0} :: pairs --> {1} ".format(self.code,self.pairs))
    
    def generateGene(self,length):
        code=""
        for x in range (length):
            code+=str(random.randint(0,1))
        return code
    
    def getPairs(self):
        codePairs=[]
        for i,c in enumerate(self.code):
            if c == "1":
                codePairs.append(self.items[i])
        return codePairs;
    
    def fitnessFunction(self):
        geneFitness=0;
        if self.isFeasible():
            return geneFitness
        for i in self.pairs:
            geneFitness+=self.pairs[i].benefit
        return geneFitness
    
    def isFeasible(self):
        totalIncludedWeight=0;
        for i in self.pairs:
            totalIncludedWeight+=self.pairs[i].weight
        return bool(totalIncludedWeight > self.size)