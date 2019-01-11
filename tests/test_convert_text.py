import os
from . import test_cors
from unittest import TestCase
from convertextract import processText, process

class TextConvertTest(TestCase):
    def setUp(self):
        self.text_input = 'aaabbb'
        self.text_output = 'bbbbbb'
        self.cors = [{"from": "a", "to": "b", "before": "", "after": ""}]
        self.test_cors_dir = os.path.dirname(test_cors.__file__)

    def test_convert_from_list(self):
        cors_1 = [{"from": "a", "to": "b", "before": "", "after": ""}, {"from": "b", "to": "c", "before": "", "after": ""}]
        cors_2 = [{"from": "b", "to": "c", "before": "", "after": ""}, {"from": "a", "to": "b", "before": "", "after": ""}]
        self.assertEqual(processText(self.text_input, language=self.cors), self.text_output)
        self.assertEqual(processText(self.text_input, language=cors_1, order_as_is=True), 'cccccc')
        self.assertEqual(processText(self.text_input, language=cors_1, order_as_is=False), 'bbbccc')
        self.assertEqual(processText(self.text_input, language=cors_2, order_as_is=True), 'bbbccc')
        self.assertEqual(processText(self.text_input, language=cors_2, order_as_is=False), 'bbbccc')

    def test_convert_from_csv(self):
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'basic.csv')), self.text_output)
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.csv'), order_as_is=True), 'cccccc')
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.csv'), order_as_is=False), 'bbbccc')
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.csv'), order_as_is=True), 'bbbccc')
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.csv'), order_as_is=False), 'bbbccc')

    def test_convert_from_xlsx(self):
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'basic.xlsx')), self.text_output)
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.xlsx'), order_as_is=True), 'cccccc')
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.xlsx'), order_as_is=False), 'bbbccc')
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.xlsx'), order_as_is=True), 'bbbccc')
        self.assertEqual(processText(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.xlsx'), order_as_is=False), 'bbbccc')

    def test_context_sensitive(self):
        self.assertEqual(processText('test', language=[{'from': 't', 'to': 'p', 'before': '^', 'after': 'e'}]), 'pest')
        self.assertEqual(processText('test', language=[{'from': 't', 'to': 'p', 'before': '', 'after': ''}]), 'pesp')