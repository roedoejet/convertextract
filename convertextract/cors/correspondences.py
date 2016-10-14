"""
Parse spreadsheets for correspondence lists.
"""

import os
import importlib
from openpyxl import load_workbook 
from openpyxl.styles import Font, Fill, Color
from openpyxl.cell import Cell
from .. import exceptions
import re


# _*_ coding:utf-8 _*_
class Correspondence():
    
    def __init__(self, language):
        # Load workbook, either from correspondence spreadsheets, or user loaded
        this_dir = os.path.dirname(os.path.abspath(__file__))
        if not isinstance(language, type(None)):
            if re.search(r'\.xlsx', language):
                wb = load_workbook(language)
                ws = wb.active
            else:
                file_name = this_dir + "\\" + "correspondence_spreadsheets" + "\\" + language + ".xlsx"
                wb = load_workbook(file_name)
                ws = wb.active

            # Create wordlist
            cor_list = []

            # Loop through rows in worksheet, create if statements for different columns and append Cors to cor_list.
            for entry in ws:
                newCor = {}
                for col in entry:
                    if col.column == 'A':
                        value = col.value
                        if type(value) == long or float or int:
                            value = unicode(value)
                        newCor["to"] = value
                    if col.column == 'B':
                        value = col.value
                        if type(value) == long or float or int:
                            value = unicode(value)
                        newCor["from"] = value
                    cor_list.append(newCor)

            self.cor_list = cor_list

