from .utils import BaseParser

class Parser(BaseParser):
    """Parse ``.txt`` files"""

    def extract(self, filename, **kwargs):
        
        with open(filename, 'r', encoding='utf8') as stream:
            text = stream.read()

        transducer = self.get_transducer(kwargs.get('language', ''), kwargs.get('table', ''))
        converted_filename = filename[:-4] + '_converted.txt'
        text = transducer(text)

        if "no_write" in kwargs and kwargs['no_write']:
            pass
        else:
            textfile = open(converted_filename, 'w', encoding='utf-8')
            textfile.write(text)
            textfile.close()
                        
        return text
