# _*_ coding:utf-8 _*_
import pptx

from .utils import BaseParser
from ..cors import processCors

class Parser(BaseParser):
    """Extract text from pptx file using python-pptx
    """

    def extract(self, filename, **kwargs):

        if not isinstance(kwargs["language"], type(None)):
            cors = processCors(kwargs["language"])

        converted_filename = filename[:-5] + '_converted.pptx'
        presentation = pptx.Presentation(filename)
        text_runs = []
        all_text = ""
        for slide in presentation.slides:
            for shape in slide.shapes:
                if not shape.has_text_frame:
                    continue
                for paragraph in shape.text_frame.paragraphs:
                    for run in paragraph.runs:
                    
                        # Convert text
                        if not isinstance(kwargs["language"], type(None)):
                            processed = cors.apply_rules(run.text)
                            
                        # Replace old text
                        run.text = processed
                        run.font.name = "Times New Roman"
                        
                        # Save new presentation
        presentation.save(converted_filename)
        return '\n\n'.join(text_runs)