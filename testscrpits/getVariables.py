import re

def main():
	dutFilePath = "temp/TopLevel.sv"
	dutFile = open(dutFilePath, "r")
	for line in dutFile:

		# this should be done with re as this will allow for a comment within a line
		line = removeComments(line)
		##line = line.split("//",1)[0]
		##line = line.split("/*",1)[0]
		##try:
		##	line = line.split("*/",1)[1]
		##except:
		##	pass

		print(line.strip("\n"))

def removeComments(string):
    string = re.sub(re.compile("/\*(.|\n)*?\*/",re.DOTALL ) ,"" ,string) # remove all occurance streamed comments (/*COMMENT */) from string
    string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile("/\*.*?\n" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    string = re.sub(re.compile(".*?\*/" ) ,"" ,string) # remove all occurance singleline comments (//COMMENT\n ) from string
    return string

main()