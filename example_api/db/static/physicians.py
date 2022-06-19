import json

from example_api.exceptions import NotFoundError

from example_api.util import to_json, from_json

from example_api import logging
logger = logging.getLogger()

def find_physician_by_id(physicians, physician_id):
        return next((index for index, physician in enumerate(physicians) if str(physician['_id']) == str(physician_id)), -1)

def compute_next_id(list_of_items = []):
    """computes next logical _id for list of items with _id"""
    return max([-1] + [int(x['_id']) for x in  list_of_items]) + 1

class StaticDB():
    """Primary interface for the static physicians database"""

    def __init__(self, path):
        self.path = '%s/physicians.json' % path

    def get_all_physicians(self):
        return json.load(open(self.path))

    def write_physicians(self, physicians):
        with open(self.path, 'w') as f:
            f.write(to_json(physicians, pretty_print=True))

    def get_physician_appointments(self, physician_id):
        physicians = self.get_all_physicians()

        index = find_physician_by_id(physicians, physician_id)

        if index == -1:
            raise NotFoundError('Could not find physician with id %s' % physician_id)

        return physicians[index]['appointments']

    def add_physician_appointments(self, physician_id, new_appointments):

        logger.debug('adding new appointments for physician %s' % physician_id)
        logger.debug(str(new_appointments))

        physicians = self.get_all_physicians()

        index = find_physician_by_id(physicians, physician_id)

        if index == -1:
            raise NotFoundError('Could not find physician with id %s' % physician_id)

        # server side compute each new id for appointments
        for appointment in new_appointments:
            appointment["_id"] = compute_next_id(physicians[index]['appointments'])
            physicians[index]['appointments'].append(appointment)

        self.write_physicians(physicians)