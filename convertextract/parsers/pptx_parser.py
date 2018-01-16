# _*_ coding:utf-8 _*_
import pptx

from .utils import BaseParser
from ..cors import processCors

class Parser(BaseParser):
    """Extract text from pptx file using python-pptx
    """

    def extract(self, filename, **kwargs):

        if not isinstance(kwargs["language"], type(None)):
            cors = processCors(kwargs["language"]).cor_list
            cors.sort(key=lambda x: len(x["from"]), reverse=True)

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
                        a = run.text
                        if not isinstance(kwargs["language"], type(None)):
                            for kv in cors:
                                a = a.replace(kv["from"],kv["to"])
                        
                        # Replace old text
                        run.text = a
                        run.font.name = "Times New Roman"
                        
                        # Save new presentation
        presentation.save(converted_filename)
        return '\n\n'.join(text_runs)