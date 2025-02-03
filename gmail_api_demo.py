import os, json

from fetch_email import FetchEmail
from db.gmail_msg  import GmailMsg

from rules.rule_parser import *

os.environ["hf_mysql_host"]="127.0.0.1"
os.environ["hf_mysql_user"] = "root"
os.environ["hf_mysql_password"]="password"
os.environ["hf_db_name"] = "gmail_api_demo"


class GmailApiDemo:
    
    def fetch_emails(self):
        fetch_email = FetchEmail()
        fetch_email.execute()
    
    def execute_rule(self, file_name):
        with open(file_name, 'r') as file:
            json_data = json.load(file)
        
        print(json_data)
        rules = RuleParser().create_rules(json_data)
        for r in rules:
            r.execute()
        

if __name__ == "__main__":

    gmail_api_demo = GmailApiDemo()
    gmail_api_demo.fetch_emails()
    gmail_api_demo.execute_rule("rules_0.json")

