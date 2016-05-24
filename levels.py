class Level():
	def __init__(self):
		self.levels = []
	
	def is_root (self):
		return self.levels[0] == 1
	
	def sort_level(self):
		 self.levels.sort(key=lambda x: x.p, reverse=True)

		
				
	