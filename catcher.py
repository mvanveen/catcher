import traceback


trace_stack = []

class Trace(object):
    def __init__(self, exception, stack=None):
	if not isinstance(exception, Exception):
	    raise ValueError("Expected an Exception object as first argument")

	if not stack:
	    stack = traceback.extract_stack()
            # pop off current frame and initial catch frame
	    stack.pop()
            stack.pop() 

	# TODO: try to grab exception if it's not passed in explicitly
        self._exception = exception
	self._stack = stack

    @property
    def exception(self):
        return self._exception

    @property
    def stack(self):
        return self._stack

    def __str__(self):
        return ''.join(
            traceback.format_list(self.stack) +
	    traceback.format_exception_only(
              type(self.exception),
              self.exception
            )
	).strip()

    def __repr__(self):
        return '<Trace (%s)>' % (
            type(self.exception).replace('exceptions.', ''), 
        )


def catch(e):
    trace_stack.append(Trace(e))

def dump(exception_type=None, lineno=None, module=None):
    return trace_stack

if __name__ == '__main__':
    import random
    for i in range(20):
        try:
            random.randint(0,5) / 0
        except Exception, e:
            catch(e)

    print str(dump()[0])
