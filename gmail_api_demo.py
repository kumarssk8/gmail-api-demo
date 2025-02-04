import os, json

from db_config import *
from fetch_email import FetchEmail
from rules.rule_parser import RuleParser


class GmailApiDemo:
    
    def fetch_emails(self):
        fetch_email = FetchEmail()
        fetch_email.execute()
    
    def execute_rule(self, file_name):
        with open(file_name, 'r') as file:
            json_data = json.load(file)
        
        rules = RuleParser().create_rules(json_data)
        for r in rules:
            r.execute()
        

if __name__ == "__main__":

    gmail_api_demo = GmailApiDemo()
    gmail_api_demo.fetch_emails()
    gmail_api_demo.execute_rule("rules_0.json")

