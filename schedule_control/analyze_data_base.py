import pandas as pd
import matplotlib.pyplot as plt

# Load the data base
file_path = '/home/heberto/Dropbox/'
name = 'time_data_base.pickle'
filename = file_path + name
db = pd.read_pickle(filename)

# Dictionary of actions
actions_dic_hours = {'wake': 'Woke Up Hours', 'work': 'Arrived Hours',
                     'leave': 'Left Work Hours'}

actions_dic_minutes = {'wake': 'Woke Up Minutes',
                       'work': 'Arrived Minutes',
                       'leave': 'Left Work Minutes'}


# Actions
action = 'wake'


def get_complete_time(db, action, actions_dic_hours, actions_dic_minutes):

    aux1 = actions_dic_hours[action]
    aux2 = actions_dic_minutes[action]

    time = db[aux1] + db[aux2] * 1.0 / 60.0

    return time


time = get_complete_time(db, action, actions_dic_hours, actions_dic_minutes)
mean = time.mean()
minutes = (mean - int(mean)) * 60.0

print int(mean), minutes
