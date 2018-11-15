#!/bin/env python

import numpy as np

outfilename = "output.txt"
outfile = open(outfilename, 'w')

for sample, value in k_dictionary:

  area1 = []
  area2 = []
  area3 = []
  area4 = []
  for sample2, value2 in value:
    if sample2.endwith("S1"):
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
        pval = "NaN"
        qval = "NaN"
        sigma = "NaN"

outfile.write(sample + "\t" + np.mean(area1) + "\t" + np.mean(area2) + "\t" + np.mean(area3) + "\t" + np.mean(area4) + "\t" + np.sd(area1) + "\t" + np.sd(area2) + "\t" + np.sd(area3) + "\t" + np.sd(area4) + "\t" + pval + "\t" + qval + "\t" + sigma + "\n")
