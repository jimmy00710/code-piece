import os
from pdfminer.high_level import extract_text

"""
Input - filepath
Output - Text/String
"""


def text_converter(file_pth):
    text = extract_text(open(file_pth, "rb"))
    return text
