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


# Create the frame
filename = './data_frame_test.pickle'
cols = ['year', 'month', 'day', 'weekday',
        'hour', 'minutes', 'action']

if path.exists(filename):
    print 'Data frame exists'
    frame = pd.read_pickle(filename)
else:
    print 'Creating data frame'
    frame = DataFrame(columns=cols)

if frame.index.max() is nan:
    index_to_add = 0
else:
    index_to_add = frame.index.max() + 1

frame.loc[index_to_add] = [year, month, day, weekday, hours, minutes, action]

# Show frame
print frame

# Save the frame
frame.to_pickle(filename)
