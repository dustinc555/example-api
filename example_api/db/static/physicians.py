import json

def get_all_physicians(path):
    return json.load(open('%s/physicians.json' % path))

def get_physician_appointments(path, physician_id):
    physicians = json.load(open('%s/physicians.json' % path))
    physician = [x for x in physicians if str(x['_id']) == str(physician_id)]

    if len(physician) == 0:
        raise Exception("Could not find physician")

    return physician[0]['appointments']