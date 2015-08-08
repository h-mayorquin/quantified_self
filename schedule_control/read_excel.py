import pandas as pd

# Read the excel file
db = pd.read_excel('puntualidad.xlsx', header=3, parsed_dates=['Date'])
# Erase the index
del db['Id']
# This is because Panda's data frame alredy has an index

filename = './temporal.pickle'
db.to_pickle(filename)
