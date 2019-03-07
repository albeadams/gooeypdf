from gooey import Gooey, GooeyParser
import sys
import pandas as pd
import oracle
import graph


@Gooey(default_size=(610,530), program_name="MFG Report")
def createGooey():
	desc = "Download MFG PDF by entering one or two MFG names"
	g_parser = GooeyParser(description = desc)
	g_parser.add_argument("MFG", help="MFG to analyze. Entire name not required, but needs correct spelling.")
	args = g_parser.parse_args()

def oracle_query(name, query):
	try:
		cursor = oracle.query(name, query)
		cols = [ x[0] for x in cursor.description ]
		rows = cursor.fetchall()
		return pd.DataFrame(rows, columns=cols)
	except:
		print("Failed to grab data")
	finally:
		if cursor is not None:
			cursor.close()


def findName(inputVal):
	input = inputVal[0].upper()
	count = 0
	with open("mfg_names.txt", "r") as fp:
		for line in iter(fp.readline, ''):
			if input in line.rstrip():
				submit = line.rstrip()
				count += 1
			if input == line.rstrip():
				#exact match, i.e. MONSANTO
				return submit

	if count > 1:
		print('More than one MFG found, please be more specific')
		return ""
	else:
		return submit

def main():
	createGooey()
	name = findName(sys.argv[2:])
	if name != "":
		df = oracle_query(name, "mfg_sales")
		graph.make_pdf(df, name)

if __name__ == '__main__':
	main()