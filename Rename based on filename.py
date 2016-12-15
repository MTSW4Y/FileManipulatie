import os
import re

for filename in os.listdir("."):
	NewName = re.sub("-99=1_1" , "_1", filename)
	print filename, NewName
	if filename !=  NewName:
		os.rename(filename, NewName)