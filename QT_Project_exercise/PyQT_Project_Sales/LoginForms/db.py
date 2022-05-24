import mysql.connector
# from mysql.connector import connection
#pip install configparser
from configparser import ConfigParser


class DB:
	def __init__(self):
		db_config = DB.read_db_config(filename='./config.ini', section='MYSQL')

		try:
			self.cnx = mysql.connector.connect(
				user=db_config['user'],
				password=db_config['password'],
				db=db_config['db'],
				host=db_config['host'],
				port=db_config['port']
			)
		except mysql.connector.Error as e:
			print(e)
			exit()

	def read_db_config(filename='./config.ini', section='MYSQL'):
		""" Read database configuration file and return a dictionary object
				:param filename: name of the configuration file
				:param section: section of database configuration
				:return: a dictionary of database parameters
		"""
		# create parser and read the configuration file
		parser = ConfigParser()
		parser.read(filename)


		db_config = {}
		if parser.has_section(section):
				items = parser.items(section)
				for item in items:
						db_config[item[0]] = item[1]
		else:
				raise Exception(f'{section} not found in the {filename} file')

		return db_config

	def authenticate(self, user_name, password):
		# create a cursor for the connection
		c= self.cnx.cursor()

		# prepare SQL query:
		q = f"""
			SELECT * FROM salesperson
				WHERE Email=%s AND PasswordID=%s
		"""
		# execute the query
		c.execute(q,(user_name,password))

		# we are only interested if 1 or 0 rows are returned
		res = c.fetchone()

		# do something with the result
		return True if res else False
	#return sales
	def view_sales(self):
		c = self.cnx.cursor()
		q = f"""
					SELECT * FROM salesorder

				"""
		c.execute(q)
		result = c.fetchone()
		print(result)
		return result

if __name__ == '__main__':
	db = DB()

	# let's use some hard-coded values for test:
	user_name_test = 'snezhana@gmail.com'
	password_test = 'Snezhana123'

	if db.authenticate( user_name=user_name_test, password=password_test):
		print('User is valid')
	else:
		print('Invalid user name or password')
