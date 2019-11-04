# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:20:15 2019

@author: josep
"""
from Gene import Gene as gene
import random
from operator import attrgetter


class Knapsack:
    def __init__(self,size,itemsCount,items):
        self.itemsCount=itemsCount
        self.size=size
        self.items=items
        self.populationSize=32
        self.population=self.initialPopulation()
    
    def initialPopulation(self):
        populationList=[]
        for i in range (self.populationSize):
            newGene=gene(self.size,self.itemsCount,self.items)
            populationList.append(newGene)
        return populationList
            
    def totalFitness(self):
        total=0
        for i in self.population:
            total+=i.fitness
        return total
    
    def rouletteWheelSelection(self):
        maxSum=self.totalFitness()
        randomNumber=random.uniform(0,maxSum)
        currentSum=0
        for geneObject in self.population:
            currentSum+=geneObject.fitness
            if currentSum > randomNumber:
                return geneObject
 
    def algorithm(self):
        generationCount=400
        for i in range (generationCount):
            parent1=self.rouletteWheelSelection()
            parent2=self.rouletteWheelSelection()
            #Crossover
            child1,child2=self.singlePointCrossover(parent1,parent2)
            #Mutation
            child1.mutate()
            child2.mutate()
            
            self.population.extend([child1,child2])
            
            #remove worst 2 genes in population
            self.removeWorst()
            self.removeWorst()
        
        return max(self.population, key=attrgetter('fitness'))
  
    def singlePointCrossover(self,parent1,parent2):
         point=self.singlePointPlace() 
         child1=gene(self.size,self.itemsCount,self.items)
         child2=gene(self.size,self.itemsCount,self.items)
        
         child1.code=parent1.code[0:point]+parent2.code[-(self.itemsCount-point):]
         child2.code=parent2.code[0:point]+parent1.code[-(self.itemsCount-point):]
        
         return child1,child2
     
    def removeWorst(self):
         worstIndex=0
         for i in range(len(self.population)):
             if self.population[i].fitness < self.population[worstIndex].fitness:
                 worstIndex=i
         self.population.pop(worstIndex)
             
    def singlePointPlace(self):
        return random.randint(0,self.itemsCount-1)
# =============================================================================
#          if self.itemsCount % 2 ==0:
#              return int(self.itemsCount/2)
#          else:
#              return int(self.itemsCount/2) +1
# =============================================================================
 
