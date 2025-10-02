import pymysql

def mysqlconnect():
	# To connect MySQL database
	conn = pymysql.connect(
		host='localhost',
		user='root',
		password = " ",
		db='manually_fill_attendance',
		)
	
	cur = conn.cursor()
	
	# Select query
	cur.execute("select * Se_2023-05-23_10-38-46")
	output = cur.fetchall()
	
	for i in output:
		print(i)
	
	# To close the connection
	conn.close()

# Driver Code
if __name__ == "__main__" :
	mysqlconnect()

