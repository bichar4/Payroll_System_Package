import pymysql
DB_CONFIG = {
    'host': 'localhost',
    'user': 'newuser2',
    'pass': 'randomPass',
    'db': 'payroll_management_system',
    'char': 'utf8',
    'file': './sqlFiles/create_tables.sql'
}

class Database:
    def __init__(self,DB_CONFIG):
        """
            Creates a mysql database connector 
        """
        try:
            self.conn = pymysql.connect(
                    host=DB_CONFIG['host'],
                    user=DB_CONFIG['user'], 
                    password = DB_CONFIG['pass'],
                    cursorclass=pymysql.cursors.DictCursor,
            )
            self.cur = self.conn.cursor()
        except ValueError:
            print("Please contact your database administrtor")

    def switch_db(self,database):
        self.conn.select_db(database)

    def __del__(self):
        try:
            self.conn.close()
        except ValueError:
            print("Please contact your database administrator")

    def get_sql_from_file(self,filename):
        """
        Get the SQL instruction from a file

        :return: a list of each SQL query whithout the trailing ";"
        """
        from os import path

        # File did not exists
        if path.isfile(filename) is False:
            print("sql file NOt found")
            print("File load error : {}".format(filename))
            return False

        else:
            with open(filename, "r") as sql_file:
                # Split file in list
                ret = sql_file.read().split(';')
                # drop last empty entry
                ret.pop()
                return ret

    def executeSqlFile(self,filename):
        """
            executes the list of the instructions
        """
        request_list = self.get_sql_from_file(filename)
        if request_list is not False:
            for idx, sql_request in enumerate(request_list):
                print(idx,sql_request)
                self.cur.execute(sql_request + ';')
        self.conn.commit()
        return self.cur.fetchall()
    
    def executeSQLCommand(self,command,values=None):
        """
            executes custom command fetched by the user 
        """
        if values is None:
            self.cur.execute(command)
        else:
            self.cur.execute(command,values)
        self.conn.commit()
        return self.cur.fetchall()
            

if __name__ == '__main__':
    myDatabase = Database(DB_CONFIG)
    # myDatabase.executeSqlFile(DB_CONFIG['file'])
    myDatabase.executeSqlFile("./sqlFiles/create_tables.sql")
    myDatabase.switch_db('payroll_management_system')
    myDatabase.executeSqlFile("./sqlFiles/dummy_data.sql")
    # print(myDatabase.executeSqlFile('./showData-loff.sql'))
    # print(myDatabase.executeSQLCommand("SELECT * FROM product WHERE id = %s",(1)))
    print(myDatabase.executeSQLCommand("show tables"))