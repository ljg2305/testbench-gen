"""
"""
import sys
import re

def main(): ##need to make this a proper funtion with passable args
	testFile = sys.argv[1]
	extentions = [".sv",".v"]

	for extention in extentions:
		if testFile.endswith(extention):
			testFile = testFile[:-len(extention)]
			testbench_name = testFile+"TB"+extention

	print("Creating output file",testbench_name)

	testbench = open(testbench_name, "w+")
	testbench.close();
main()