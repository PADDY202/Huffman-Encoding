#Huffman Coding
#Padraig Mitchell
#Takes in a alphabet and each elements probability & max number for encoding
#Uses the max number of encoding to create huffman tree of the same number of childern
#returns a dict of each alphabet element and its code & the average length of the codes


import node
import levels
import codes
class Huff():
		def __init__(self,d,**pmf):
			self.d =d
			self.pmf = pmf
			self.p = list(self.pmf.values())
			self.s = list(self.pmf.keys())
			self.tree = []
			self.maketree()
			self.makecode()
			self.expectedlength()
			
		# take in a list of n parents
		def make_parent(self, n):
				#find the combined probability
				newp=0
				for i, val in enumerate(n):
					newp = newp + val.p				
				parent = node.Node(newp)
				parent.childern = n
				for i, val in enumerate(n):
					val.parents = parent
					val.value = i
					val.parent_level = len(self.tree)
				return parent
				
		#tree list of levels
		#levels list of nodes
		def maketree(self):
			base = levels.Level()
			for i, val in enumerate(self.p):
				n = node.Node(val)
				n.symbol = self.s[i]
				base.levels.append(n)
			base.sort_level()	
			self.tree.append(base)	
			while (len(self.tree[-1].levels) != 1):
				babies = self.tree[-1].levels[-self.d:]
				parent = self.make_parent(babies)
				level = levels.Level()
				level.levels.append(parent)
				for val in self.tree[-1].levels[:-self.d]:
					level.levels.append(val)
				level.sort_level()
				self.tree.append(level)	

		#traverse tree and make codes
		#store codes in a symbol -> code dict
		def makecode(self):
			self.sym_codes = {}	
			for i, val in enumerate(self.tree[0].levels):
				code = codes.Codes()
				symbol = self.tree[0].levels[i].symbol
				code.codes.append(self.tree[0].levels[i].value)
				
				parent =self.tree[0].levels[i].parents
				while(parent.p < 0.99):
					code.codes.append(parent.value)
					parent = parent.parents					
				code.order()
				self.sym_codes[symbol]=code.codes


		#expected length	
		def expectedlength(self):
			c = list(self.sym_codes.values())
			csum = 0
			for i, val in enumerate(c):
				csum = csum + len(val)
			expected_len = csum / len(c) 
			print('\n'+str(self.d)+'-ary Code')
			print('Huffman Codes:\n ' + str(self.sym_codes))
			print('Expected code length:\n ' +str(expected_len))
