#!/bin/env python

import numpy as np

KT = open('k_table.csv')

Counter = 0
K_Dictionary = {}
for Line in KT:
    Counter = Counter+1
    E = Line.split(',')
    if Counter > 1:
        if E[1] not in K_Dictionary.keys():
            K_Dictionary[E[1]] = {}
            K_Dictionary[E[1]][E[2]] = E[3]

        else:

            K_Dictionary[E[1]][E[2]] = E[3]
    #if Counter ==26:
        #break
KT.close()

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

InFile.close()
outfilename = "output.txt"
outfile = open(outfilename, 'w')

for sample, value in K_Dictionary.items():

  area1 = []
  area2 = []
  area3 = []
  area4 = []
  for sample2, value2 in value.items():
    if sample2.endswith("S1"):
      area1.append(value2)
    if sample2.endswith("S2"):
      area1.append(value2)
    if sample2.endswith("S3"):
      area1.append(value2)
    if sample2.endswith("S7"):
      area2.append(value2)
    if sample2.endswith("S8"):
      area2.append(value2)
    if sample2.endswith("S10"):
      area2.append(value2)
    if sample2.endswith("S9"):
      area3.append(value2)
    if sample2.endswith("S11"):
      area3.append(value2)
    if sample2.endswith("S12"):
      area3.append(value2)
    else:
      area4.append(value2)
    if sample in Stab_Dictionary.keys():

        stabval = Stab_Dictionary[sample]
        pval = stabval[0]
        qval = stabval[1]
        sigma = stabval[2]
    else:
        pval = 'NaN'
        qval = 'NaN'
        sigma = 'NaN'

outfile.write(sample + "\t" + str(np.mean(area1)) + "\t" + str(np.mean(area2)) + "\t" + str(np.mean(area3)) + "\t" + str(np.mean(area4)) + "\t" + str(np.sd(area1)) + "\t" + str(np.sd(area2)) + "\t" + str(np.sd(area3)) + "\t" + str(np.sd(area4)) + "\t" + pval + "\t" + qval + "\t" + sigma + "\n")
