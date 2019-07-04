"""
This is the runs module and supports all the ReST actions for the
runs collection
"""
from datetime import datetime

# 3rd party modules
from flask import make_response, abort
from pymongo import MongoClient
from bson.json_util import dumps
from flask import jsonify
import json

client = MongoClient('mongodb://root:example@db:27017')
runs = client.pvtdb.runs

def get_active():
    active_runs = list(runs.find({'status': 'Active'}))
    return json.loads(dumps(active_runs))

def create(run):
    run['start-time'] = _get_timestamp()
    run['update-time'] = ''
    run['end-time'] = ''
    result = runs.insert_one(run)
    if result.inserted_id:
        return {'ok': True, 'message': 'Create Successful!'}, 201
    else:
        return {'ok': False, 'message': 'Create Failed!'}, 404

def get_run(instanceid):
    result = runs.find_one({'instanceid': instanceid})
    if result:
        return json.loads(dumps(result))
    else:
        return {'ok': False, 'message': f'Instance id {instanceid} not found!'}, 404


def update(instanceid, run):
    run['update-time'] = _get_timestamp()
    result = runs.find_one_and_update({'instanceid': instanceid}, {'$set': run})
    if result:
        return {'ok': True, 'message': 'Update Successful!'}
    else:
        return {'ok': False, 'message': f'Instance id {instanceid} not found!'}, 404

def delete(instanceid):
    result = runs.delete_one({'instanceid': instanceid})
    if result.deleted_count:
        return {'ok': True, 'message': 'Delete Successful!'}
    else:
        return {'ok': False, 'message': f'Instance id {instanceid} not found!'}, 404

def _get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))    