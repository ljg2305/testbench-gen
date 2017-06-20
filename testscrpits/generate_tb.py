import sys

def main():
	dutFilePath = sys.argv[1]
	
	dutFile = importFile(dutFilePath)
	if(dutFile):
		print("file opened sucessfully")
	else:
		print("no file opened :(")
		return

	dutTbFile = generateOuptutFile(dutFilePath)
	if(dutTbFile):
		print("file created sucessfully")
	else:
		print("no file created :(")
		return

	closeAllFiles(dutFile,dutTbFile)

def closeAllFiles(dutFile,dutTbFile):
	dutFile.close()
	dutTbFile.close()

def importFile(dutFilePath):
	try:
		print("Opening",dutFilePath, ":")
		dutFile = open(dutFilePath, "r")
	except:
		print("File entered does not have the correct permissions or does not exist, plase check the file name.")
		return
	
	if not(dutFilePath.endswith('.sv') or dutFilePath.endswith('.v')):
		print("File must be of type .sv or .v")
		return

	for line in dutFile:
		print(line.strip('\n'))
	print()

	return dutFile

def generateOuptutFile(dutFilePath):
	extentions = [".sv",".v"]

	for extention in extentions:
		if dutFilePath.endswith(extention):
			dutFilePath = dutFilePath[:-len(extention)]
			dutTbFilePath = dutFilePath+"TB"+extention


	try:
		open(dutTbFilePath, "r")
		overwrite =  input("The requested testbench already exists, do you want to overwrite the file? y/n: ")
		validInput = False
		while  (not validInput):
			if(overwrite.lower() == "n"):
				validInput = True; #I know this one is in vein  
				return #might be a return if want one scrpit to rule them all
			elif(overwrite.lower() == "y"):
				print("Overwriting file")
				validInput = True;
			else:
				overwrite = input("Input invalid: please enter y/n: ")
	except:
		print("Creating output file",dutTbFilePath)


	dutTbFile = open(dutTbFilePath, "w+")
	#need to remeber to remove this
	dutTbFile.close();
	return dutTbFile

main()