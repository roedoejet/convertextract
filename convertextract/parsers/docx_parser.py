import docx

from convertextract.parsers.utils import BaseParser

class Parser(BaseParser):
    """Extract text from docx file using python-docx.
    """

    def extract(self, filename, **kwargs):
        if 'mapping' in kwargs and kwargs['mapping']:
            transducer = self.create_transducer(kwargs['mapping'])
        else:
            transducer = self.get_transducer(kwargs.get('input_language', ''), kwargs.get('output_language', ''))
        converted_filename = filename[:-5] + '_converted.docx'
        document = docx.Document(filename)
        text_runs = []
        for paragraph in document.paragraphs:
            for run in paragraph.runs:
                # this line prevents images from being erased
                if run.text != "" and run.text != " ":
                    run.text = transducer(run.text).output_string
                    text_runs.append(run.text)
        if "no_write" in kwargs and kwargs['no_write']:
            pass
        else:
            document.save(converted_filename)
        return '\n\n'.join(text_runs)
