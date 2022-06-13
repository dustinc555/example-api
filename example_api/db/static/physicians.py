import json


class StaticDB():

    def __init__(self, path):
        self.path = path

    def get_all_physicians(self):
        return json.load(open('%s/physicians.json' % self.path))

    def get_physician_appointments(self, physician_id):
        physicians = json.load(open('%s/physicians.json' % self.path))
        physician = [x for x in physicians if str(x['_id']) == str(physician_id)]

        if len(physician) == 0:
            raise Exception("Could not find physician")

        return physician[0]['appointments']