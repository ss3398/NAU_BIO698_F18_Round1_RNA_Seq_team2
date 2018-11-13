#!/usr/bin/env python
import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('readcounts.txt')
df.boxplot(column='est_counts',by='sample')
plt.show()
print 'plot done'
