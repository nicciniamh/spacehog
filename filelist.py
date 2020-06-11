class list(list):
	'''
	class that extends list to initialize from an optional file. If no filename
	is specified a simple list is initialized. 
	'''
	def __init__(self,filename=False):
		if filename:
			self.filename = filename
			with open(filename) as f:
				self.extend(f.read().splitlines())

if __name__ == '__main__':
	foo = filelist('data')
	print('foo is {}: {}'.format(type(foo), ', '.join(foo)))