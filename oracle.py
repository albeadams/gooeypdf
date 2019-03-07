import cx_Oracle as ora
import dataconfig as dc

def query(mfg, name):

	#user should supply username, password once on initial use, store in text and pass in here
	connection = ora.connect(dc.data['username'], dc.data['password'], dc.data['client'])

	cursor = connection.cursor()

	cursor.execute(dc.query[name],
	 		mfg_name = mfg)

	return cursor