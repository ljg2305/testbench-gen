"""
readfile will read a .sv or a .v file and verify its existance and extention 
"""
import sys

def main(): ##need to make this a proper funtion with passable args
	"""

	readfile will read a .sv or a .v file and verify its existance and extention 
 	"""

	try:
		filename = str(sys.argv[1])
		print("Opening",filename, ":")
		file = open(filename, "r")
	except:
		print("File entered does not have the correct permissions or does not exist, plase check the file name.")
		return
	
	if not(filename.endswith('.sv') or filename.endswith('.v')):
		print("File must be of type .sv or .v")
		return

	for line in file:
		print(line)
	


main()