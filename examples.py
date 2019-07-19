from decorators import *

@timer
def waste_some_time(num_times):
	for _ in range(num_times):
		sum([i**2 for i in range(10000)])


@debug
def make_greeting(name, age=None):
	if age is None:
		return f"Howdy {name}"
	else:
		return f"Whoa {name}! {age} already, you are growing up!"


