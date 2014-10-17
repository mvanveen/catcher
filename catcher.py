from collections import defaultdict
import hashlib
import sys
import traceback

TRACE_STACK = []
TRACE_COUNTER = defaultdict(int)

class Trace(object):
    def __init__(self, exception_type, exception, traceback):
	#if not isinstance(exception, Exception):
	#    raise ValueError("Expected an Exception object as first argument")

	# TODO: try to grab exception if it's not passed in explicitly
        self._exception = exception
        self._traceback = traceback
	#self._stack = stack

    @property
    def exception(self):
        return self._exception

    @property
    def traceback(self):
        return self._traceback

    def hash(self):
        return hashlib.sha1(str(self)).hexdigest()

    def __str__(self):
	return ''.join(
	    traceback.format_exception(
                type(self.exception),
                self.exception,
                self.traceback
            )
         ).strip()

    def __repr__(self):
        return '<Trace (%s)>' % (
            str(type(self.exception)).replace('exceptions.', ''), 
        )

def catch(e):
    trace = Trace(*sys.exc_info())
    TRACE_STACK.append(trace)
    TRACE_COUNTER[trace.hash()] += 1

def dump(exception_type=None, lineno=None, module=None):
    return TRACE_STACK, TRACE_COUNTER

def clear():
    del TRACE_STACK
    del TRACE_COUNTER
    TRACE_STACK = []
    TRACE_COUNTER = default_dict(int)

if __name__ == '__main__':
    import random
    for i in range(20):
        try:
            random.randint(0,5) / 0
        except Exception, e:
            catch(e)

    print dump()
