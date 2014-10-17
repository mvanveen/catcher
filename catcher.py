import traceback


trace_stack = []

class Trace(object):
    def __init__(self, exception, stack):
	if not isinstance(exception, Exception):
		raise ValueError("Expected an Exception object as first argument")

	# TODO: try to grab exception if it's not passed in explicitly
        self._exception = exception
	self._stack = stack

    @property
    def exception(self):
        return self._exception

    @property
    def stack(self):
        return self._stack

    def __repr__(self):
        return ''.join(
            traceback.format_list(self.stack) +
	    traceback.format_exception_only(
              type(self.exception),
              self.exception
            )
	).strip()

def catch(e):
    trace_stack.append(Trace(e, traceback.extract_stack()))

def dump(exception_type=None, lineno=None, module=None):
    return trace_stack

if __name__ == '__main__':
    try:
        2 / 0
    except Exception, e:
        catch(e)

    print dump()[0]
