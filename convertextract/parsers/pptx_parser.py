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
                        
                        # Add font attributes
                        font = run.font
                        bold_attr = font.bold
                        try:
                            color_attr = font.color.rgb if font.color.type != None else None
                        except:
                            pass
                        italic_attr = font.italic
                        name_attr = font.name
                        size_attr = font.size
                        
                        # Replace text
                        a = run.text
                        if not isinstance(kwargs["language"], type(None)):
                            for kv in cors:
                                a = a.replace(kv["from"],kv["to"])
                        
                        # Remove old text
                        run.text = ""
                        
                        # Add new run
                        new_run = paragraph.add_run()
                        
                        # Add new text to run
                        new_run.text = a
                        
                        # Add attributes
                        new_run.font.bold = bold_attr
                        
                        try:
                            new_run.font.color.rgb = color_attr
                        except:
                            pass

                        new_run.font.italic = italic_attr
                        new_run.font.name = name_attr
                        new_run.font.size = size_attr
                        
                        # Append text to run
                        text_runs.append(a)
                        
                        # Save new presentation
        presentation.save(converted_filename)
        return '\n\n'.join(text_runs)