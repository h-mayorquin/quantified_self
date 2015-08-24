actions_dic_hours = {'wake': 'Woke Up Hours', 'work': 'Arrived Hours',
                     'leave': 'Left Work Hours'}

actions_dic_minutes = {'wake': 'Woke Up Minutes',
                       'work': 'Arrived Minutes',
                       'leave': 'Left Work Minutes'}

actions_dic_time = {'wake': 'Woke Up Time',
                    'work': 'Arrived Time',
                    'leave': 'Left Work Time'}


def get_complete_time(db, action, actions_dic_hours, actions_dic_minutes):

    aux1 = actions_dic_hours[action]
    aux2 = actions_dic_minutes[action]

    time = db[aux1] + db[aux2] * 1.0 / 60.0

    return time
