from gooey import Gooey, GooeyParser
import sys
import oracle as orca
import pandas as pd

@Gooey(default_size=(610,530), program_name="MFG Report")
def createGooey():
	desc = "Download MFG PDF by entering one or two MFG names"
	g_parser = GooeyParser(description = desc)
	g_parser.add_argument("MFG", help="MFG to analyze. Entire name not required, but needs correct spelling.")
	args = g_parser.parse_args()

def oracle_connect(submit):
	results = orca.query(submit)
	for code in results:
		print(code)

def findName(inputVal):
	input = inputVal[0].upper()
	count = 0
	with open("mfg_names.txt", "r") as fp:
		for line in iter(fp.readline, ''):
			if input in line.rstrip():
				submit = line.rstrip()
				count += 1

	if count > 1:
		print('More than one MFG found, please be more specific')
		return ""
	else:
		return submit

def main():
	createGooey()
	result = findName(sys.argv[2:])
	if result != "":
		oracle_connect(result)

if __name__ == '__main__':
	main()