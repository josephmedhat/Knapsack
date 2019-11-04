# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 21:16:34 2019

@author: josep
"""
from Pair import Pair
from knapsack import Knapsack as Knapsack


pair1=Pair(4,1)
pair2=Pair(7,7)
pair3=Pair(1,22)
pair4=Pair(2,23)
pair5=Pair(3,6)

items=[]
items.extend([pair1,pair2,pair3,pair4,pair5])
knapsackObject=Knapsack(14,5,items)

#print(knapsackObject.algorithm().fitness)


filePath = "input_example.txt"
f = open("result.txt", "a")

with open(filePath, "r") as file:
    text = file.read()

testCases = text.split("\n\n")

start=1
while start <= int(testCases[0]):
    case = testCases[start].strip().split("\n")

    items = []
    for item in case[2:]:
        weight, value = item.split(" ")
        items.append(Pair(int(weight), int(value)))
    
    size =int(case[1]) 
    knapsackObject=Knapsack(size,int(case[0]),items)
    
    f.write("Case {0}: {1} \n".format(start,knapsackObject.algorithm().fitness))
    print("Case {0}: {1}".format(start,knapsackObject.algorithm().fitness))
    start+=1
f.write("---------------------------- New Iteration -----------------------------\n")
f.close()