import numpy as np
import pandas as pd
columns=['2002','2004','2005','1009']
index=['z','y','d','a']
df=pd.DataFrame(columns=columns,index=index)
df['2002']['z']=12
df['2004']['y']=2
df['2005']['d']=1
df['1009']['a']=10

print df
df.to_csv('out.csv',sep=',')