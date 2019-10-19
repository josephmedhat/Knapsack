# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:20:15 2019

@author: josep
"""
from Gene import Gene as gene
import random

class Knapsack:
    def __init__(self,size,itemsCount,items):
        self.itemsCount=itemsCount
        self.size=size
        self.items=items
        self.populationSize=1000
        self.population=self.initialPopulation()
    
    def initialPopulation(self):
        populationList=[]
        for i in range (self.populationSize):
            newGene=gene(self.size,self.itemsCount,self.items)
            populationList.append(newGene)
            
    def totalFitness(self):
        total=0
        for i in self.population:
            total+=self.population[i].fitness
        return total
    
    def RouletteWheelSelection(self):
        maxSum=self.totalFitness()
        randomNumber=random.uniform(0,maxSum)
        currentSum=0
        for i,geneObject in self.initialPopulation:
            currentSum+=geneObject.fitness
            if currentSum > randomNumber:
                return geneObject
            
    
# =============================================================================
#     def singlePointCrossover(self,parent1,parent2):
#         point=self.singlePointPlace()      
#         newGene=gene(self.size,self.itemsCount,self.items)
# 
#     def singlePointPlace(self):
#         if self.itemsCount % 2 ==0:
#             return self.itemsCount/2
#         else:
#             return int(self.itemsCount/2) +1
# =============================================================================
