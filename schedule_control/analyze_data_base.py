import pandas as pd
import matplotlib.pyplot as plt
from aux_functions import get_complete_time
from aux_functions import actions_dic_hours, actions_dic_time
from aux_functions import actions_dic_minutes


# Load the data base
file_path = '/home/heberto/Dropbox/'
name = 'time_data_base.pickle'
filename = file_path + name
db = pd.read_pickle(filename)

# Print the total mean for the three quantities
print 'Total mean over time'
print 'Wake Up ', db['Woke Up Time'].mean()
print 'Work ', db['Arrived Time'].mean()
print 'Leave', db['Left Work Time'].mean()

# Print the 30 days mean for the three quantities
print '-----------------------'
print 'Statistics for the last 30 days'
n = 30
print 'Wake Up ', db['Woke Up Time'][-n:].mean()
print 'Work ', db['Arrived Time'][-n:].mean()
print 'Leave', db['Left Work Time'][-n:].mean()

# Print the 7 days mean for the three quantities
print '-----------------------'
print 'Statistics for the last seven days'
n = 7
print 'Wake Up ', db['Woke Up Time'][-n:].mean()
print 'Work ', db['Arrived Time'][-n:].mean()
print 'Leave', db['Left Work Time'][-n:].mean()
