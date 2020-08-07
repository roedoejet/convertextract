import csv

from convertextract.parsers.utils import BaseParser

class Parser(BaseParser):
    """Extract text from comma separated values files (.csv).
    """

    delimiter = ','

    def extract(self, filename, **kwargs):
        if 'mapping' in kwargs and kwargs['mapping']:
            transducer = self.create_transducer(kwargs['mapping'])
        else:
            transducer = self.get_transducer(kwargs.get('input_language', ''), kwargs.get('output_language', ''))
        # quick 'n dirty solution for the time being
        with open(filename) as stream:
            reader = csv.reader(stream, delimiter=self.delimiter)
            data = [row for row in reader]
        return '\n'.join([self.delimiter.join([transducer(col).output_string for col in row]) for row in data])
