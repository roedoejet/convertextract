import docx

from .utils import BaseParser

class Parser(BaseParser):
    """Extract text from docx file using python-docx.
    """

    def extract(self, filename, **kwargs):
        transducer = self.get_transducer(kwargs.get('language', ''), kwargs.get('table', ''))
        converted_filename = filename[:-5] + '_converted.docx'
        document = docx.Document(filename)
        text_runs = []
        for paragraph in document.paragraphs:
            for run in paragraph.runs:
                if "language" in kwargs and kwargs['language']:
                    # this line prevents images from being erased
                    if run.text != "" and run.text != " ":
                        run.text = transducer(run.text)
                        text_runs.append(run.text)
        if "no_write" in kwargs and kwargs['no_write']:
            pass
        else:
            document.save(converted_filename)
        return '\n\n'.join(text_runs)
