import huff
import random
input={'1':eval('1/21'),'2':eval('2/21'),'3':eval('3/21'),'4':eval('4/21'),'5':eval('5/21'),'6':eval('6/21')}
symbols = list(input.keys())
sentence =[]
trees = []
reverse_dict ={}
detree = []
#make code
for i in range(0,10):	#sub 10 for any length
	sentence.append(random.choice(symbols))
def encode(sentence, dictionary):
	code_sentence=[]
	for i, val in enumerate(sentence):
		code_sentence.append(dictionary[val] )
	return (code_sentence)

trees.append(huff.Huff(3, **input).sym_codes)
trees.append(huff.Huff(4, **input).sym_codes)

for i, val in enumerate(trees):
	print("sentence" + str(sentence))
	code = encode(sentence,val)
	print("code" + str(code))
	reverse_dict=(dict([v, k] for k, v in val.items()))
	print("decode" +str(encode(code,reverse_dict)))

