from openpyxl import load_workbook
import six

from .utils import BaseParser


class Parser(BaseParser):
    """Extract text from Excel files (.xls/xlsx).
    """

    def extract(self, filename, **kwargs):
        converted_filename = filename[:-5] + '_converted.xlsx'
        transducer = self.get_transducer(kwargs.get('language', ''), kwargs.get('table', ''))
        workbook = load_workbook(filename)
        sheet_names = workbook.worksheets
        output = "\n"
        for name in sheet_names:
            worksheet = sheet_names[workbook.index(name)]
            for row in worksheet:
                new_output = []
                for col in row:
                    value = col.value
                    if value:
                        if isinstance(value, (int, float)):
                            value = six.text_type(value)
                        if "language" in kwargs and kwargs['language']:
                            value = transducer(value)
                            col.value = value
                        new_output.append(value)
                if new_output:
                    output += u' '.join(new_output) + u'\n'
        if "no_write" in kwargs and kwargs['no_write']:
            pass
        else:
            workbook.save(converted_filename)
        return output
