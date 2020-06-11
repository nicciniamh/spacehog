class list(list):
	'''
	class that extends list to initialize from an optional file. If no filename
	is specified a simple list is initialized. 
	'''
	def __init__(self,arg=False):
		self.initialize(arg)

	def initialize(self,arg=False):
		if not arg:
			filename = '/dev/null'
		else:
			filename = arg

		with open(filename) as f:
			self.extend(f.read().splitlines())


if __name__ == '__main__':
	import os
	from importlib.machinery import SourceFileLoader
	mod = SourceFileLoader("filelist", "filelist.py").load_module()
	foo = mod.list(os.path.expanduser('~/data'))
	print('foo is {}: {}'.format(type(foo), ', '.join(foo)))
