import pandas as pd
df = pd.read_csv('top500.pages.05.18.csv')
print (df)
df.drop('Rank', axis = 1, inplace = True)
#print (df)
df.insert(loc=0, column = 'Scheme', value = 'http://')
print (df)
df.to_csv('top500.pages.05.18.csv', index = False)