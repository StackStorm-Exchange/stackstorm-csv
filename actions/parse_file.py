import os
import csv

from st2actions.runners.pythonrunner import Action

__all__ = [
    'ParseCSVFileAction'
]


class ParseCSVFileAction(Action):
    def run(self, file_path, delimiter=',', quote_char='"'):
        if not os.path.isfile(file_path):
            raise ValueError('File "%s" doesnt exist' % (file_path))

        result = []
        with open(file_path, 'r') as fh:
            reader = csv.reader(fh, delimiter=str(delimiter), quotechar=str(quote_char))

            for row in reader:
                result.append(row)

        return result
