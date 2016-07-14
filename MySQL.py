#!/usr/bin/python
import pymysql

# select (table, parameter)
# insert (table, data)
# update (table, id, data)
# delete (table, id)

class MySQL:
    def __init__(self):
        self.sort_by = ""
        self.order = ""
        self.wher = ""
        # initiate database connection.
        self.connection = pymysql.connect(host='localhost',
                             user='root',
                             password='zicom@123',
                             db='sherlock',
                             charset='utf8mb4')
        
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
     # this fuction is for filter mysql records. (the "where" factor)
    def where(self, *args):
        args = list(args)
        operator=["=", ">=", "<=", "!="]
        for op in operator:
            if op in args[0]:
                self.wher = "where %s \"%s\"" % (args[0], args[1])
            else:
                self.wher = "where %s = \"%s\"" % (args[0], args[1])        

    # this function is for selecting any feild on any table.(feilds veriable is optinal)     
    def select(self, table, feilds="*", *args, **kwargs):
     
        sql = "SELECT %s FROM `%s`" % (feilds, table)
        
        try:
            if self.wher and self.sort_by:
                sql = sql+" "+str(self.wher)+" order by "+str(self.sort_by)+" "+str(self.order)
            elif self.wher:
                sql = sql+" "+str(self.wher)
        except:
            sql = sql+"order by"+str(self.sort_by)+" "+str(self.order)
        print sql
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result    

    
    # This function is for data sorting for Mysql; but optinal.
    # example : SELECT * FROM `users`  order by id asc
    def order_by(self, sort_by="", order="", *args, **kwargs):
        self.sort_by = sort_by
        self.order = order
    
    # this function is for closing Mysql connection
    def close(self):
        self.connection.close()

########### END OF MySQL CLASS #############


