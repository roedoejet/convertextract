from convertextract.parsers.utils import BaseParser

class Parser(BaseParser):
    """Parse ``.txt`` files"""

    def extract(self, filename, **kwargs):
        with open(filename, 'r', encoding='utf8') as stream:
            text = stream.read()
        if 'mapping' in kwargs and kwargs['mapping']:
            transducer = self.create_transducer(kwargs['mapping'])
        else:
            transducer = self.get_transducer(kwargs.get('input_language', ''), kwargs.get('output_language', ''))
        converted_filename = filename[:-4] + '_converted.txt'
        text = transducer(text).output_string

        if "no_write" in kwargs and kwargs['no_write']:
            pass
        else:
            with open(converted_filename, 'w', encoding='utf8') as textfile:
                textfile.write(text)         
        return text
