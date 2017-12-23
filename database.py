import pymysql

def query(connection, sql, commit=True, results=True):
    """
    Queries the database given the sql command and connection
    
    http://pymysql.readthedocs.io/en/latest/user/examples.html
    
    :param connection: PyMySQL connection object 
    :param sql: string representing valid SQL command
    :param commit: boolean representing whether to commit (ie. if sproc or insert)
    :param results: boolean representing whether to show results
    :return: results if results true as a list of dictionaries given the appropriate sql command
    """
    try:
        with connection.cursor() as cursor:
            # Create a new record
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        if commit:
            connection.commit()

        if results:
            results = cursor.fetchall()
            return results
    finally:
        connection.close()

if __name__ == '__main__':
    connection = pymysql.connect(host='localhost',
                                 user='',
                                 password='',
                                 db='sys',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    # sql = "CALL sys.InsertPost('python test', 'confessions');"
    sql = "SELECT * from sys.FacebookPosts;"
    print(query(connection, sql))