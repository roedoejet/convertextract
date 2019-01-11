import docx

from .utils import BaseParser
from ..cors import Correspondence

class Parser(BaseParser):
    """Extract text from docx file using python-docx.
    """

    def extract(self, filename, **kwargs):
        if "language" in kwargs and kwargs["language"]:
            converted_filename = filename[:-5] + '_converted.docx'
            cors = Correspondence(kwargs["language"], kwargs)

        document = docx.Document(filename)
        text_runs = []
        for paragraph in document.paragraphs:
            for run in paragraph.runs:
                if "language" in kwargs and kwargs['language']:
                    # this line prevents images from being erased
                    if run.text != "" and run.text != " ":
                        run.text = cors.apply_rules(run.text)
                        text_runs.append(run.text)
        if "language" in kwargs and kwargs["language"]:
            if "no_write" in kwargs and kwargs['no_write']:
                pass
            else:
                document.save(converted_filename)
        return '\n\n'.join(text_runs)
