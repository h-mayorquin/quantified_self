from datetime import datetime

# So first we need the extract the datea of this moment

time_stamp = datetime.now()

# Now let's get all the data
minutes = time_stamp.minute
hours = time_stamp.hour
weekday = time_stamp.isoweekday()
day = time_stamp.day
month = time_stamp.month
year = time_stamp.year
