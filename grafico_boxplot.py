import matplotlib.pyplot as plt

import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

years=[1992,1993,1994,1995]
xvals = range(len(df))
x=df.mean(axis=1)
y=(df.std(axis=1) / (df.count(axis=1) **0.5)) * 1.96

plt.bar(xvals,x, width = 1,  color='grey' ,edgecolor='w', yerr=y, capsize=8 ) 
plt.xticks(xvals, years)

plt.show()

def verifica_valor(z):
    colors=[]
    for i in range(4):
        if( (y.iloc[i] + x.iloc[i] -z)/ (2*y.iloc[i])>1):
            colors.append('r')
        elif(  (y.iloc[i] + x.iloc[i] -z)/ (2*y.iloc[i])< 0):
            colors.append('b')
        else:
            colors.append('grey')

    plt.bar(xvals,x, width = 1,  color=colors ,edgecolor='w', yerr=y, capsize=8 ) 
    plt.axhline(z, color="y")
    plt.ylabel('Valores criados')
    plt.xticks(xvals, years)
    return plt.show()

verifica_valor(44000)
