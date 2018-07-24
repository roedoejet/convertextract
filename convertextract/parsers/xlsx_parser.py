from openpyxl import load_workbook
import six

from six.moves import xrange

from .utils import BaseParser
from ..cors import processCors


class Parser(BaseParser):
    """Extract text from Excel files (.xls/xlsx).
    """

    def extract(self, filename, **kwargs):
        if "language" in kwargs and kwargs['language']:
            converted_filename = filename[:-5] + '_converted.xlsx'
            cors = processCors(kwargs["language"])
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
                            value = cors.apply_rules(value)
                            col.value = value
                        new_output.append(value)
                if new_output:
                    output += u' '.join(new_output) + u'\n'
        if "language" in kwargs and kwargs["language"] and "no_write" in kwargs and not kwargs['no_write']:
            workbook.save(converted_filename)
        return output
