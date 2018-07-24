import unittest
import shutil
import os

from . import base


class TxtTestCase(base.BaseParserTestCase, unittest.TestCase):
    extension = 'txt'

    def test_converted_text_python(self):
        """Make sure converted text matches from python"""
        for cor in self.languages_filenames:
            fn, ext = os.path.splitext(cor)
            head, tail = os.path.split(cor)
            language = os.path.splitext(tail)[0]
            fn = fn + "_converted"
            new_file = fn + ext
            self.compare_converted_python_output(cor, expected_filename=new_file, language=language)

    def compare_converted_python_output(self, filename, expected_filename=None, **kwargs):
        # import pdb; pdb.set_trace()
        if expected_filename is None:
            expected_filename = self.get_expected_filename(filename, **kwargs)
        # print(kwargs['language'])
        import convertextract
        result = convertextract.process(filename, **kwargs)
        if isinstance(result, bytes):
            result = result.decode("utf8")
        # print(type(result))
        # self.maxDiff = None
        with open(expected_filename, 'r', encoding="utf8") as stream:
            result = self.clean_str(result)
            expected = self.clean_str(stream.read())
            self.assertEqual(result, expected)

    # def test_extensionless_filenames(self):
    #     """make sure that text from extensionless files is treated as txt"""
    #     temp_filename = self.get_temp_filename()
    #     shutil.copyfile(self.raw_text_filename, temp_filename)
    #     self.compare_python_output(temp_filename, self.raw_text_filename)
    #     os.remove(temp_filename)
