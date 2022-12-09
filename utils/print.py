import json

def print_json(obj):
    print(json.dumps(obj, sort_keys = True, indent = 4))