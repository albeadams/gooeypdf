import cx_Oracle as ora
import re
import dataconfig as dc
# import pyodbc
# import pandas.io.sql as psql

def query(mfg):

	#user should supply username, password once on initial use, store in text and pass in here
	connection = ora.connect(dc.data['username'], dc.data['password'], dc.data['client'])

	cursor = connection.cursor()

	cursor.execute(dc.query3,
	 		mfg_name = mfg)

	return cursor