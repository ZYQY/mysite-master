import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mysql.netsoc.co',
                             user='stephenteam5',
                             password='eFDhNR4lUP',
                             db='stephenteam5_Project5',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # Create a new record
    #     sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
    #     cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
    #
    # # connection is not autocommit by default. So you must commit to save
    # # your changes.
    # connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT * FROM `Researchers `"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()