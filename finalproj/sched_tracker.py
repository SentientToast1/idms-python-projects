from datetime import datetime
import csv
import argparse
import json
import os



parser = argparse.ArgumentParser()
parser.add_argument("-start",type=str,default= None, nargs='?',help="enter start time")
parser.add_argument("-end",type=str,help="enter end time")
parser.add_argument("-name",type=str,help="name of the task")
parser.add_argument("-list", action="store_true",help="list the tasks")
parser.add_argument("-stoptask",action="store_true",help="stop the ongoing task")
parser.add_argument("-ct",action='store_true',help="clears all tasks")
args = parser.parse_args()
currentTime  = datetime.now()

def addTask():
    data = []
    with open("data/tasklist.json",'r') as file:
        data = json.load(file)

    data.append({"date" : currentTime.strftime("%d-%m-%Y"),"data" : {"name":args.name , "start":args.start, "end":args.end}})

    with open("data/tasklist.json",'w') as file:
        json.dump(data,file,indent=2)
    print(f"{args.name} added to tasks")

def startTask():
    startedTime = int(currentTime.timestamp())
    task = f"{args.name},{startedTime}"
    with open("data/current.txt",'w') as f:
        f.write(task)
    print("Started timer!")

def endTask():
    endedTime = int(currentTime.timestamp())
    with open("data/current.txt",'r') as f:
        name,startTime = f.read().strip().split(',')
    duration = endedTime-int(startTime)
    hours = duration // 3600
    minutes = (duration%3600) // 60
    seconds = duration % 60
    print(f"{name} took {hours}h {minutes}m {seconds}s")
    with open("data/tasklist.json",'r') as file:
        data = json.load(file)

    data.append({"date" : currentTime.strftime("%d-%m-%Y"),"data" : {"name":name , 
                                                                     "start":datetime.fromtimestamp(int(startTime)).strftime("%H:%M"), 
                                                                     "end":datetime.fromtimestamp(endedTime).strftime("%H:%M")}})

    with open("data/tasklist.json",'w') as file:
        json.dump(data,file,indent=2) 
    os.remove('data/current.txt')

def listTasks():
    data = []
    with open("data/tasklist.json", 'r') as f:
        data = json.load(f)
    entries = len(data)
    print("Date".ljust(20) + "Name".ljust(20) + "Start Time" + "\t\t" + "End Time")
    for i in range(entries):
        print(f'{data[i]["date"].ljust(12)}\t{data[i]["data"]["name"].ljust(20)}\t{data[i]["data"]["start"]}\t\t\t{data[i]["data"]["end"]}')

def makeReport():
    pass

def clearFile():
    with open("data/tasklist.json",'w') as f:
        json.dump([],f)


def main():
    if args.start and args.end and args.name:
        addTask()
    elif args.start is None and args.name:
        startTask()
    elif args.stoptask:
        endTask()
    elif args.list:
        listTasks()
    elif args.ct:
        clearFile()
    else:
        print("no arguments provided!")



main()