"""
This is the runs module and supports all the ReST actions for the
runs collection
"""
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

# Data to serve with our API
runs = [
    {
        "instanceid": "1a",
        "status": "Active",
        "files": ['f1', 'f2', 'f3'],
        "log": '/somewhere/log.txt',
        "start-time": "asdsad",
        "end-time": "asdasd"
    },
    {
        "instanceid": "2b",
        "status": "Active",
        "files": ['f1', 'f2', 'f3'],
        "log": '/somewhere/log.txt',
        "start-time": "asdsad",
        "end-time": "asdasd"
    },
    {
        "instanceid": "3c",
        "status": "Failed",
        "files": ['f1', 'f2', 'f3'],
        "log": '/somewhere/log.txt',
        "start-time": "asdsad",
        "end-time": "asdasd"
    },
]

# Create a handler for our read (GET) doggo
def get_active():
    """
    This function responds to a request for /doggo-info/random

    # Create the list of doggo from our data
    """
    active_runs = list(filter(lambda r: r["status"] == 'Active', runs))
    return active_runs

def create(run):
    runs.append(run)
    return runs

def get_run(instanceid):
    return list(filter(lambda r: r["instanceid"] == instanceid, runs))[0]

def update(instanceid, run):
    for i, run in enumerate(runs):
        if run["instanceid"] == instanceid:
            runs[i] = run
    return runs

def delete(instanceid):
    for run in runs:
        if run["instanceid"] == instanceid:
            runs.remove(run)
    return runs