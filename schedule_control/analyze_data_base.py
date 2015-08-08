import pandas as pd

# Load the data base
file_path = '/home/heberto/Dropbox/'
name = 'time_data_base.pickle'
filename = file_path + name
db = pd.read_pickle(filename)


print db[-5:]
