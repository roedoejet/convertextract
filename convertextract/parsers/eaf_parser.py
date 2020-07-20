from .utils import BaseParser

class Parser(BaseParser):
     """Extract text from ELAN file using pympi-ling.
    """

    def extract(self, filename, **kwargs):
        if 'mapping' in kwargs and kwargs['mapping']:
            transducer = self.create_transducer(kwargs['mapping'])
        else:
            transducer = self.get_transducer(kwargs.get('input_language', ''), 
                                             kwargs.get('output_language', ''))
        converted_filename = filename[:-4] + '_converted.eaf'
        # Here is where you should parse and convert the Elan file
        # To get output just do transducer(INPUT).output_string
        if "no_write" not in kwargs or not kwargs['no_write']:
            # This should save the file!!!
            pass
        # This should return the converted text
        return