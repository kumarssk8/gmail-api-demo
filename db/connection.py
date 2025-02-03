import os
import mysql.connector;

class Connection():

    _instance = None

    @classmethod
    def get(cls):
        if cls._instance is not None:
            return cls._instance
        try:
            cls._instance =  mysql.connector.connect(
                host = os.environ.get("hf_mysql_host"),
                user = os.environ.get("hf_mysql_user"),
                password = os.environ.get("hf_mysql_password"),
                database = os.environ.get("hf_db_name")
            )
            return cls._instance
        except Exception as ex:
            print(ex)