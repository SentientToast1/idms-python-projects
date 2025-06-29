from datetime import datetime, date
import time
import json
import src.paths as paths
import ctypes

with open(paths.SCHEDULE, "r") as file:
    schedule = json.load(file)

def toast(i):
    ctypes.windll.user32.MessageBoxW(0, schedule[i]["Description"], schedule[i]["Name"], 0x0)

# Preprocess task times
for task in schedule:
    dt = datetime.strptime(task["Time"], "%H:%M")
    task["timestamp"] = datetime.combine(date.today(), dt.time()).timestamp()

# Track triggered tasks
triggered = set()

# Last task timestamp
lastTimestamp = schedule[-1]["timestamp"]

while True:
    now = datetime.now().timestamp()

    for i, task in enumerate(schedule):
        if i in triggered:
            continue
        if now >= task["timestamp"]:
            toast(i)
            triggered.add(i)

    if now >= lastTimestamp and len(triggered) == len(schedule):
        break
    time.sleep(30)

