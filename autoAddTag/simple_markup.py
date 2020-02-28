import re

from autoAddTag.util import *


def markup(file):
    print('<html><head><title>...</title></head><body>')
    title = True
    for block in blocks(file):
        block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
        if title:
            print('<h1>')
            print(block)
            print('</h1>')
            title = False
        else:
            print('<p>')
            print(block)
            print('</p>')
