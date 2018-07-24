import pptx

from .utils import BaseParser
from ..cors import processCors


class Parser(BaseParser):
    """Extract text from pptx file using python-pptx
    """

    def extract(self, filename, **kwargs):
        if "language" in kwargs and kwargs['language']:
            converted_filename = filename[:-5] + '_converted.pptx'
            cors = processCors(kwargs["language"])

        presentation = pptx.Presentation(filename)
        text_runs = []
        for slide in presentation.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                        if "language" in kwargs and kwargs['language']:
                            run.text = cors.apply_rules(run.text)
                        text_runs.append(run.text)
        if "language" in kwargs and kwargs["language"] and "no_write" in kwargs and not kwargs['no_write']:
            presentation.save(converted_filename)
        return '\n\n'.join(text_runs)