import json

def get_all_books(path):
    return json.load(open('%s/books.json' % path))