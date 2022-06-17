import json

from example_api.exceptions import NotFoundError

from example_api.util import to_json, from_json

from example_api import logging
logger = logging.getLogger()

def find_physician_by_id(physicians, physician_id):
        return next((index for index, physician in enumerate(physicians) if str(physician['_id']) == str(physician_id)), -1)

class StaticDB():

    def __init__(self, path):
        self.path = '%s/physicians.json' % path

    def get_all_physicians(self):
        return json.load(open(self.path))

    def write_physicians(self, physicians):
        with open(self.path, 'w') as f:
            f.write(to_json(physicians, pretty_print=True))

    def get_physician_appointments(self, physician_id):
        physicians = json.load(open(self.path))

        index = find_physician_by_id(physicians, physician_id)

        if index == -1:
            raise NotFoundError('Could not find physician with id %s' % physician_id)

        return physicians[index]['appointments']

    def add_physician_appointments(self, physician_id, new_appointments):
        physicians = json.load(open(self.path))

        index = find_physician_by_id(physicians, physician_id)

        if index == -1:
            raise NotFoundError('Could not find physician with id %s' % physician_id)

        physicians[index]['appointments'] += new_appointments

        self.write_physicians(physicians)