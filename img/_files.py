import os
from os import walk

f = []
for (dirpath, dirnames, filenames) in walk("./dac"):
    f.extend(filenames)
    break

def banana():
	out = ""
	for i in range(0, len(f)):
		if "_files.py" in f[i]:
			f[i] = ''
		out += '"%s", ' % (f[i]).replace(".png", "")
	return out



print(banana())