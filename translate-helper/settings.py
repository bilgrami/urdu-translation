import json
from collections import namedtuple


def _json_object_hook(d): 
  return namedtuple('X', d.keys())(*d.values())

def _Json2Obj(data): 
  return json.loads(data, object_hook=_json_object_hook)

def _ReadJson(file_name):
  with open(file_name, encoding='utf-8') as fh:
    data = json.load(fh)
    return json.dumps(data)

def LoadSettings(file_name):
  json_data =  _ReadJson(file_name)
  settings = _Json2Obj(json_data)
  return settings
