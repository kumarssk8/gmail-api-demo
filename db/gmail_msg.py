import mysql.connector;

from db.connection import Connection


class GmailMsg:

    def __init__(self):
        self._table_name = "gmail_msgs" # table name in db
    
    def insert(self, data):
        print(data)
        try:
            insert_query = f"insert ignore into {self._table_name} (msg_id, thread_id, date_received, internal_date, subject, from_address, body) values (%(msg_id)s, %(thread_id)s, %(date_received)s, %(internal_date)s, %(subject)s, %(from_address)s, %(body)s)"
            
            mysql_connection = Connection.get()
            mysql_connection.cursor().executemany(insert_query, data)
            mysql_connection.get().commit()
        except Exception as ex:
            print(ex)
    
    def select_msg_ids(self, condition):
        query_string = f"select msg_id from {self._table_name} where {condition}"

        mysql_connection = Connection.get()
        cursor = mysql_connection.cursor()

        cursor.execute(query_string)
        result_set = cursor.fetchall()
        msg_ids = [row[0] for row in result_set]
        return msg_ids
    
    
