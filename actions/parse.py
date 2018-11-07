import csv

from six.moves import StringIO

from st2common.runners.base_action import Action

__all__ = [
    'ParseCSVAction'
]


class ParseCSVAction(Action):
    def run(self, data, delimiter=',', quote_char='"'):
        fh = StringIO(data)

        reader = csv.reader(fh, delimiter=str(delimiter), quotechar=str(quote_char))

        result = []
        for row in reader:
            result.append(row)
        return result
