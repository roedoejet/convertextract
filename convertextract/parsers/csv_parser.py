import csv

from .utils import BaseParser

class Parser(BaseParser):
    """Extract text from comma separated values files (.csv).
    """

    delimiter = ','

    def extract(self, filename, **kwargs):
        transducer = self.get_transducer(kwargs.get('language', ''), kwargs.get('table', ''))
        # quick 'n dirty solution for the time being
        with open(filename) as stream:
            reader = csv.reader(stream, delimiter=self.delimiter)
            return transducer('\n'.join([self.delimiter.join(row) for row in reader]))
