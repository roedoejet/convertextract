import pptx

from .utils import BaseParser

class Parser(BaseParser):
    """Extract text from pptx file using python-pptx
    """

    def extract(self, filename, **kwargs):
        converted_filename = filename[:-5] + '_converted.pptx'
        transducer = self.get_transducer(kwargs.get('language', ''), kwargs.get('table', ''))
        presentation = pptx.Presentation(filename)
        text_runs = []
        for slide in presentation.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        if "language" in kwargs and kwargs['language']:
                            run.text = transducer(run.text)
                        text_runs.append(run.text)
        if "no_write" in kwargs and kwargs['no_write']:
            pass
        else:
            presentation.save(converted_filename)
        return '\n\n'.join(text_runs)