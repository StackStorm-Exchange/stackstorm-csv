import os
import csv
from StringIO import StringIO

from st2actions.runners.pythonrunner import Action

__all__ = [
    'ParseCSVFileAction'
]


class ParseCSVFileAction(Action):
    def run(self, file_path, delimiter=',', quote_char='"'):
        if not os.path.isfile(file_path):
            raise ValueError('File "%s" doesnt exist' % (file_path))

        with open(file_path, 'r') as fp:
            content = fp.read()

        fh = StringIO(content)

        reader = csv.reader(fh, delimiter=str(delimiter), quotechar=str(quote_char))

        result = []
        for row in reader:
            result.append(row)
        return result
