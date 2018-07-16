"""mapFunc.py"""

import sys
import pandas as pd

df = pd.read_csv(sys.stdin)

doc = []

for i in range(len(df)):
        
	print ('%s\t%s\t%s' % (df.iloc[i][3],df.iloc[i][2],df.iloc[i][0]))

