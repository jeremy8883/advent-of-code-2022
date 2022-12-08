import json

def print_dict(obj):
    print(json.dumps(obj, sort_keys = True, indent = 4))