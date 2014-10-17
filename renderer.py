"""HTML renderer for catcher
"""
from pygments import highlight
from pygments.lexers import PythonTracebackLexer
from pygments.formatters import HtmlFormatter

import catcher


def render():
    items = catcher.dump()
    for item in items:
        yield highlight(str(item), PythonTracebackLexer(), HtmlFormatter())

if __name__ == '__main__':
    import random
    for i in range(20):
        try:
            random.randint(0,5) / 0
        except Exception, e:
            catcher.catch(e)

    print '<style>'
    print HtmlFormatter().get_style_defs('.highlight')
    print '</style>'

    for item in render():
        print item
