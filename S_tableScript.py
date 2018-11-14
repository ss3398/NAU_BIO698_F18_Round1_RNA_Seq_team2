#!/bin/env python

InFile = open('s_table.csv')

#Goal = setup a dictionary for each file where keys are identical

Counter = 0
Stab_Dictionary = {}
for Line in InFile:
    Counter = Counter+1
    S = Line.split(',')
    if Counter > 1: 
        val=[]
        val.append(S[2])
        val.append(S[3])
        val.append(S[10])
        Stab_Dictionary[S[1]]= val
#print(len(Stab_Dictionary['NODE_1155_length_1050_cov_93.5739_g991_i0']))