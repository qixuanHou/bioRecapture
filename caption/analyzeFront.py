f = open("font.txt", "r")
line = f.readline()
dic = {}

while line != "":
	if dic.has_key(line):
		dic[line] = dic[line] + 1

	else:
		dic[line] = 1
		print "new"
	line = f.readline()
print dic


'size = 10 ALPIDL+Minion-Italic\n': 182, 
'size = 10 ALPGAC+MinionMM-SemiBoldItalicCondensed\n': 18, 
'size = 9 ALPIOH+MathematicalPi-One\n': 6, 
'size = 12 ALPEID+MinionMM-BoldCondensed\n': 336, 
'size = 13 ALPEID+MinionMM-BoldCondensed\n': 116, 
'size = 11 ALPEID+MinionMM-BoldCondensed\n': 42, 
'size = 24 ALPEDK+MinionMM-SemiBoldCondensed\n': 268, 
'size = 9 AMBBHG+MyriadMM-RegularCondensedIt\n': 38, 
'size = 9 ALPGLI+MyriadMM-BoldCondensed\n': 336, 
'size = 8 AMJEMN+MathematicalPi-Four\n': 2, 
'size = 8 ALPGLI+MyriadMM-BoldCondensed\n': 126, 
'size = 7 ALPEMP+MinionMM-RegularCondensed\n': 32, 
'size = 10 ALPGDF+Minion-Regular\n': 63580, 
'size = 8 ALPGDF+Minion-Regular\n': 31908, 
'size = 7 ALPGJN+MyriadMM-RegularCondensed\n': 2430, 
'size = 7 ALPGLI+MyriadMM-BoldCondensed\n': 14, 
'size = 8 ALPHMO+Universal-GreekwithMathPi\n': 190, 
'size = 9 ALPIDL+Minion-Italic\n': 594, 
'size = 9 AMHMOP+Universal-ChemicalPi\n': 4, 
'size = 5 ALPHMO+Universal-GreekwithMathPi\n': 4, 
'size = 9 ALPGJN+MyriadMM-RegularCondensed\n': 19440, 
'size = 6 ALPHMO+Universal-GreekwithMathPi\n': 10, 
'size = 9 ALPINJ+OurOwn-CJS\n': 2, 
'size = 31 ALPLDF+MathematicalPi-Three\n': 8, 
'size = 5 ALPGDF+Minion-Regular\n': 48, 
'size = 10 ALPJEP+Symbol\n': 26, 
'size = 9 ALPIJI+Minion-BoldItalic\n': 28, 
'size = 8 ALPGJN+MyriadMM-RegularCondensed\n': 2838, 
'size = 11 ALPEDK+MinionMM-SemiBoldCondensed\n': 4576, 
'size = 5 ALPEMP+MinionMM-RegularCondensed\n': 6, 
'size = 8 ALPIOH+MathematicalPi-One\n': 58, 
'size = 6 ALPGDF+Minion-Regular\n': 28, 
'size = 9 ALPGDF+Minion-Regular\n': 30272, 
'size = 7 ALPHMO+Universal-GreekwithMathPi\n': 4, 
'size = 10 ALPLNI+Minion-Bold\n': 1094, 
'size = 9 AMBAPK+MyriadMM-BoldCondensedItalic\n': 166, 
'size = 10 ALPHMO+Universal-GreekwithMathPi\n': 78, 
'size = 7 AMBBHG+MyriadMM-RegularCondensedIt\n': 4, 
'size = 9 ALPEMP+MinionMM-RegularCondensed\n': 346, 
'size = 12 ALPEDK+MinionMM-SemiBoldCondensed\n': 42

