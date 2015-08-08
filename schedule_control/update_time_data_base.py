#!/usr/bin/env python

from pandas import DataFrame
import pandas as pd
from datetime import datetime
from numpy import nan
import os.path as path
import sys

# So first we need the extract the data of this moment

time_stamp = datetime.now()

# Now let's get all the data to add to the file
year = time_stamp.year
month = time_stamp.month
day = time_stamp.day
weekday = time_stamp.isoweekday()
hours = time_stamp.hour
minutes = time_stamp.minute
action = sys.argv[1]

# Actions

actions_dic_hours = {'wake': 'Woke Up Hours', 'work': 'Arrived Hours',
                     'leave': 'Left Work Hours'}

actions_dic_minutes = {'wake': 'Woke Up Minutes',
                       'work': 'Arrived Minutes',
                       'leave': 'Left Work Minutes'}


# Check that actions is wake, work or leave
possible_actions = actions_dic_hours
assert(action in possible_actions)

# Load the date frame
file_path = '/home/heberto/Dropbox/'
name = 'time_data_base.pickle'
filename = file_path + name
db = pd.read_pickle(filename)
# Check and get the date of the last index

if db.index.max() is nan:
    max_index = 0
else:
    max_index = db.index.max()
    date = db.loc[max_index]['Date']

today_date = datetime(year, month, day)

# Check if this should be new data
if (date == today_date):
    index_to_add = max_index
else:
    index_to_add = max_index + 1


# Add the data
if action == 'wake':
    hours = float(input('input the hour that you woke up (8, 9, 10, etc...) '))
    minutes = float(input('input the minutes (10, 17, 23, 44, ... etc) '))

action_hour = actions_dic_hours[action]
action_minutes = actions_dic_minutes[action]
db.loc[index_to_add, action_hour] = hours
db.loc[index_to_add, action_minutes] = minutes

# Show frame
print 'The last elements of the data base'
print db[-5:]

# Save the frame
db.to_pickle(filename)
