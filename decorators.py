import functools
import time

def decorators(func):
	@functools.wraps(func)
	def wrappers_decorators(*args, **kwargs):
		# Do something before
		value = func(*args, **kwargs)
		# Do something after
		return value
	return wrappers_decorators

def timer(func):
	""" Print the runtine of the decorated function"""
	@functools.wraps(func)
	def wrappers_timer(*args, **kwargs):
		start_time = time.perf_counter() # 1
		value = func(*args, **kwargs)
		end_time = time.perf_counter()
		run_time = end_time - start_time
		print (f'Finished {func.__name__!r} in {run_time:.4f} secs')
		return value
	return wrappers_timer



def debug(func):
	""" Print the function signature and return a value """
	@functools.wraps(func)
	def wrappers_debug(*args, **kwargs):
		# Do something before
		args_repr = [repr(a) for a in args]
		kwargs_repr = [f"{k} = {v!r}" for k, v in kwargs.items()]
		signature = ", ".join(args_repr + kwargs_repr)
		print (f"Calling {func.__name__}({signature})")
		value = func(*args, **kwargs)
		# Do something after
		print(f"{func.__name__!r} returned {value!r}")
		return value
	return wrappers_debug