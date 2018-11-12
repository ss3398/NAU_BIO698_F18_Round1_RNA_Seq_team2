#!/usr/bin/env python

from sqlalchemy import create_engine
import pandas as pd

df = pd.read_csv('s_table.csv')
dwh_engine = create_engine('mysql://bio698:bio698@localhost/bio698',echo=False)
print 'loading S_TABLE'
df.to_sql('S_TABLE',dwh_engine,index=False)

print 'Completed loading S_TABLE'
