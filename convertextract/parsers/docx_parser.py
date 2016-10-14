# _*_ coding:utf-8 _*_
import docx

from .utils import BaseParser
from ..cors import processCors

class Parser(BaseParser):
    """Extract text from docx file using python-docx.
    """

    def extract(self, filename, **kwargs):
        converted_filename = filename[:-5] + '_converted.docx'
        if not isinstance(kwargs["language"], type(None)):
            cors = processCors(kwargs["language"]).cor_list
            cors.sort(key=lambda x: len(x["from"]), reverse=True)
            
        text = ""
        document = docx.Document(filename)
        all_text = ""
        for paragraph in document.paragraphs:
            paragraph_format = paragraph.paragraph_format
            for run in paragraph.runs:
                a = run.text
                font_prop = run.font.bold
                if not isinstance(kwargs["language"], type(None)):
                    for kv in cors:
                        a = a.replace(kv["from"],kv["to"])
                run.text = ""
                new_run = paragraph.add_run()
                new_run.text = a
                new_run.font.bold = font_prop
                all_text += '\n\n' + a
            document.save(converted_filename)
            
#       **NEEDS WORK**
#        # Extract text from root paragraphs.
#        text += '\n\n'.join([
#            paragraph.text for paragraph in document.paragraphs
#        ])
#
#        # Recursively extract text from root tables.
#        for table in document.tables:
#            text += '\n\n' + self._parse_table(table)

        return all_text

    def _parse_table(self, table):
        text = ''
        for row in table.rows:
            for cell in row.cells:
                # For every cell in every row of the table, extract text from
                # child paragraphs.
                for paragraph in cell.paragraphs:
                    text += '\n\n' + paragraph.text

                # Then recursively extract text from child tables.
                for table in cell.tables:
                    text += self._parse_table(table)

        return text
