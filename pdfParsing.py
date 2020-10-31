import pytesseract as pts
import os
from pdf2image import convert_from_path, convert_from_bytes
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError)


PATH = ('D:/images/example2.pdf')
poppler_path = ('./poppler/Library/bin')

pages = convert_from_path(PATH, 501, poppler_path=poppler_path)

for page in pages:
    test_str = pts.image_to_data(page, lang='eng', config='--psm 6')
    current_linenum = 0
    current_line = ''

    for _line in test_str.split('\n')[1:]:
        line = _line.split('\t')

        if line[4] == current_linenum:
            current_line += line[-1] + ' '
        else:
            print(current_line)
            current_linenum = line[4]
            current_line = line[-1]

print(current_lune)
