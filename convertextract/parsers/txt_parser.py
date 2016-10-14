import os
import codecs
from .utils import BaseParser
from ..cors import processCors

class Parser(BaseParser):
    """Parse ``.txt`` files"""

    def extract(self, filename, **kwargs):
        if not isinstance(kwargs["language"], type(None)):
            cors = processCors(kwargs["language"]).cor_list
            cors.sort(key=lambda x: len(x["from"]), reverse=True)
            with open(filename) as stream:
                all_text = ""
                lines = stream.readlines()
                new_lines = []
                for line in lines:
                    line = unicode(line.decode('utf-8'))
                    for kv in cors:
                        line = line.replace(kv["from"],kv["to"])
                    new_lines.append(line)
                    all_text += line
                    
            # write to new file
                converted_filename = filename[:-4] + '_converted.txt'
                textfile = codecs.open(converted_filename,'w', 'utf-8')
                textfile.writelines(new_lines)
                textfile.close()
        else:    
            with open(filename) as stream:
                all_text = stream.read()
            
        return all_text

        
