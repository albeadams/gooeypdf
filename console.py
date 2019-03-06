from gooey import Gooey, GooeyParser
import sys
import oracle as orca

@Gooey(default_size=(610,530), program_name="MFG Report")
def createGooey():
	desc = "Download MFG PDF by entering one or two MFG names"
	g_parser = GooeyParser(description = desc)
	g_parser.add_argument("MFG", help="MFG to analyze. Entire name not required, but needs correct spelling.")
	args = g_parser.parse_args()

def oracle_connect():
	results = orca.query(sys.argv[2:])
	for code in results:
		print(code)

def findName(inputVal):
	#here going to take whatever input and lookup in a file for correct name
	return # need string

	#### need to pass in sys.argv[2:] to findName, make it upper, then pass result to oracle_connect,
	### which calls orca.query(val), which is already uppercase at this point, so
	### remove the logic in oracle.py that uses the array argv value
def main():
	createGooey()
	#result = findName()
	oracle_connect()

if __name__ == '__main__':
	main()