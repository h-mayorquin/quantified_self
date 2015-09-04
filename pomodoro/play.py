"""
This file serves to explore the type of dictionary that my 
pomodoro application utilizes.
"""

import json

# First we load the file 
filename = './PomodoroChallengeBackup_2015-08-03_15-31-43.json'
json_data = open(filename).read()

data = json.loads(json_data)

achievements = data['achievements']
h_rank = data['highestRank']
creation_time = data['creationTime']
rank = data['rank']
version = data['version']
workUnits = data['workUnits']
projects = data['projects']
pomodoros = data['pomodoros']
