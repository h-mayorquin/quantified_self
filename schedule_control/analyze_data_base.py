import pandas as pd

filename = './time_data_base.pickle'
db = pd.read_pickle(filename)
print db[-5:]
