import os
from test_cors import __file__ as test_dir
from unittest import main, TestCase
from convertextract import process_text, process

class TextConvertTest(TestCase):
    def setUp(self):
        self.text_input = 'aaabbb'
        self.text_output = 'bbbbbb'
        self.cors = [{"in": "a", "out": "b", "context_before": "", "context_after": ""}]
        self.test_cors_dir = os.path.dirname(test_dir)

    def test_convert_from_list(self):
        cors_1 = [{"in": "a", "out": "b", "context_before": "", "context_after": ""}, {"in": "b", "out": "c", "context_before": "", "context_after": ""}]
        cors_2 = [{"in": "b", "out": "c", "context_before": "", "context_after": ""}, {"in": "a", "out": "b", "context_before": "", "context_after": ""}]
        self.assertEqual(process_text(self.text_input, language=self.cors), self.text_output)
        self.assertEqual(process_text(self.text_input, language=cors_1, as_is=True), 'cccccc')
        self.assertEqual(process_text(self.text_input, language=cors_1, as_is=False), 'cccccc')
        self.assertEqual(process_text(self.text_input, language=cors_2, as_is=True), 'bbbccc')
        self.assertEqual(process_text(self.text_input, language=cors_2, as_is=False), 'bbbccc')

    def test_convert_from_csv(self):
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'basic.csv')), self.text_output)
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.csv'), as_is=True), 'cccccc')
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.csv'), as_is=False), 'cccccc')
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.csv'), as_is=True), 'bbbccc')
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.csv'), as_is=False), 'bbbccc')

    def test_convert_from_xlsx(self):
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'basic.xlsx')), self.text_output)
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.xlsx'), as_is=True), 'cccccc')
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_1.xlsx'), as_is=False), 'cccccc')
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.xlsx'), as_is=True), 'bbbccc')
        self.assertEqual(process_text(self.text_input, language=os.path.join(self.test_cors_dir, 'order_2.xlsx'), as_is=False), 'bbbccc')

    def test_context_sensitive(self):
        self.assertEqual(process_text('test', language=[{"in": 't', "out": 'p', 'context_before': '^', 'context_after': 'e'}]), 'pest')
        self.assertEqual(process_text('test', language=[{"in": 't', "out": 'p', 'context_before': '', 'context_after': ''}]), 'pesp')


if __name__ == '__main__':
    main()