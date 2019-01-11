from .utils import BaseParser
from ..cors import Correspondence

class Parser(BaseParser):
    """Parse ``.txt`` files"""

    def extract(self, filename, **kwargs):
        converted_filename = filename[:-4] + '_converted.txt'
        with open(filename, 'r', encoding='utf8') as stream:
            text = stream.read()
        if "language" in kwargs and kwargs['language']:
            self.cors = Correspondence(kwargs["language"], kwargs)
            text = self.cors.apply_rules(text)

            if "language" in kwargs and kwargs["language"]:
                if "no_write" in kwargs and kwargs['no_write']:
                    pass
                else:
                    textfile = open(converted_filename, 'w', encoding='utf-8')
                    textfile.write(text)
                    textfile.close()
                        
        return text
