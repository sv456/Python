class other(object):
	def implicit(self):
		print "other implicit"
		
class child(object):
	def __init__(self):
		self.other=other()
		
	def implicit(self):
		self.other.implicit()
		
		
son=child()
son.implicit()