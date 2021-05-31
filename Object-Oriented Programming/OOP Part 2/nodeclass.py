class Node(object):
	def __init__(self, content):
		if content is None:
			raise ValueError('Node must have content')
		self.c = content
		self.n = None

	@property
	def content(self):
		return self.c

	@content.setter
	def content(self, val):
		self.c = val

	@property
	def next(self):
		return self.n

	@next.setter
	def next(self, val):
		self.n = val