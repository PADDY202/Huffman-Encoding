import huff
input={'1':eval('1/21'),'2':eval('2/21'),'3':eval('3/21'),'4':eval('4/21'),'5':eval('5/21'),'6':eval('6/21')}
symbols = list(input.keys())
huff.Huff(2, **input)
huff.Huff(3, **input)
huff.Huff(4, **input)
