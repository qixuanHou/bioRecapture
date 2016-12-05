def read():
	import os

	allpapers = "training"
	f = open("result.txt", "w")

	pdfpaths = os.listdir(os.path.join(os.getcwd(), allpapers))
	for path in pdfpaths:

		if (path == ".DS_Store"):
			pass
		else:
			newpath = ''.join(e for e in path if e.isalnum())
			newpath = newpath[0:-3] + ".txt"
			path = os.path.join(allpapers, path)
			newpath = os.path.join(allpapers, newpath)
			r = open(newpath, "r")
			ls = r.readlines()
			i = 0
			x = 0
			f.write("============================================================\n")
			f.write(newpath+"\n")
			while (x == 0):
				if (ls[i][0:3] == "fig" or ls[i][0:3] == "Fig" or ls[i][0:3] == "FIG"):
					f.write(ls[i])
					i=i+1;
					try:
						while(ls[i] != "\n"):
							f.write(ls[i])
							i=i+1;
						f.write("\n")
					except:
						pass
				else:
					i = i + 1
				try:
					print ls[i]
				except:
					x = 1
					print "done"

def count(filename, dic):
	import re
	f = open(filename, "r")
	d = open(dic, "r")
	dls = d.readlines()
	dictionary = []
	for x in dls:
		dictionary.append(x[0:-1])
	ls = f.readlines()
	dic = {}
	for l in ls:
		l = l.lower()
		nestr = re.sub(r'[^a-z ]',r'',l)
		x = nestr.split(" ")

		for item in x:
			if (item != "" and item in dictionary):
				if (item not in dic):
					dic[item] = 1
				else:
					dic[item] = dic[item] + 1
	print dic


count("result.txt", "search.txt")






