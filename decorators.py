import functools

def decorators(func):
	@functools.wraps(func)
	def wrappers_decorators(*args, **kwargs):
		# Do something before
		value = func(*args, **kwargs)
		# Do something after
		return value
	return wrappers_decorators

