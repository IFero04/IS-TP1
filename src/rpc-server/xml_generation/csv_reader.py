from csv import DictReader
from io import StringIO


class CSVReader:

    def __init__(self, file, delimiter=','):
        self._file = file
        self._delimiter = delimiter

    def loop(self):
        file_to_loop = StringIO(self._file)
        for row in DictReader(file_to_loop, delimiter=self._delimiter):
            yield row

    def read_entities(self, attrs: list, builder, after_create=None, is_valid=(lambda _: True)):
        entities = {}
        for row in self.loop():
            print(row)
            e = tuple(row[attr] for attr in attrs)
            if e not in entities:
                if not is_valid(row):
                    continue
                entities[e] = builder(row)
                after_create is not None and after_create(entities[e], row)

        return entities