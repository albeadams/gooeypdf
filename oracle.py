import cx_Oracle as ora
import re
import dataconfig as df

def query(mfg):

	#user should supply username, password once on initial use, store in text and pass in here
	connection = ora.connect(df.data['username'], df.data['password'], df.data['client'])

	cursor = connection.cursor()

	cursor.execute(df.query1,
	 		mfg_name = mfg)

	return cursor