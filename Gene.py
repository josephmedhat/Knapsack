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
         self.code=self.generateGene()
         self.pairs=self.getPairs()
         self.fitness=self.fitnessFunction()
         
    def getData(self):
        print("{0} :: pairs --> {1} ".format(self.code,self.pairs))
    
    def generateGene(self):
        code=""
        for x in range (self.length):
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
        for pair in self.pairs:
            geneFitness+=pair.benefit
        return geneFitness
    
    def mutate(self):
        mutationProbablity= 0.33
        if random.random() < mutationProbablity:
            charIndex=random.randint(0,self.length-1)
            codeList=list(self.code)
            codeList[charIndex]= '0' if codeList[charIndex] == '1' else '1'
            self.code="".join(codeList)
        
    def isFeasible(self):
        totalIncludedWeight=0;
        for pair in self.pairs:
            totalIncludedWeight+=pair.weight
        return bool(totalIncludedWeight > self.size)