"""HTML renderer for catcher
"""
from pygments import highlight
from pygments.lexers import PythonTracebackLexer
from pygments.formatters import HtmlFormatter

import catcher

def render_to_file():
    print '<style>'
    print HtmlFormatter().get_style_defs('.highlight')
    print '</style>'

    for item in render():
        print item

def render():
    items, count = catcher.dump()
    visited = {}
    for item in items:
        _hash = item.hash()
        if not visited.get(_hash):
           yield '<div><p>count: %s</p></div>' % (count[_hash], ) + highlight(
             str(item),
             PythonTracebackLexer(),
             HtmlFormatter()
           )
           visited[_hash] = True

if __name__ == '__main__':
    import random
    for i in range(20):
        try:
            if random.randint(2, 5) > 3:
		sadfasdf(saf)
            else:
		2 / 0
        except Exception, e:
            catcher.catch(e)
    catcher.dump()
    render_to_file()
