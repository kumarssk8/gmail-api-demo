import os
import base64

from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
from datetime import datetime
from gmail_service import GmailService
from db.gmail_msg import GmailMsg



class FetchEmail:

    # iterates only specified no of times to fetch results using pagination,
    # as most of the account will have large no of emails
    def execute(self):
        next_page_token=""
        for i in range(5): 
            try:
                results = GmailService.list_msgs(max_results=10, page_token=next_page_token)
                print(len(results["messages"]))
                insert_mail_details = []
                for msg in results["messages"]:
                    msg = GmailService.retrieve_msg(msg["id"])
                    internal_date = str(datetime.fromtimestamp(int(msg["internalDate"])/1000).strftime('%Y-%m-%d %H:%M:%S'))
                    mail_details = {"msg_id": msg["id"], "thread_id": msg["threadId"], "internal_date": internal_date}
                    try:
                        self._get_header(msg["payload"]["headers"], mail_details)
                        for part in msg["payload"]["parts"]:
                            if 'body' in part and 'data' in part["body"]:
                                body_data = part["body"]["data"]
                                body = base64.urlsafe_b64decode(body_data).decode('utf-8')
                                mail_details["body"] = BeautifulSoup(body, 'html.parser').get_text()
                            else:
                                print("Body not found in payload.parts")
                                mail_details["body"]=""
                    except Exception as ex:
                        mail_details["body"] = ""
                        print("processing error for msg id " + msg["id"])
                        print(msg)


                    insert_mail_details.append(mail_details)
                GmailMsg().insert(insert_mail_details)
                next_page_token = results.get("nextPageToken", None)
                print("next page token " + next_page_token)
                if(next_page_token is None):
                    break
            except HttpError as error:
                print(f"An error occurred: {error}")
        
    
    def _get_header(self, headers, mail_details):
        for item in headers:
            if item["name"] == "From":
                mail_details["from_address"] = item["value"]
            elif item["name"] == "Subject":
                mail_details["subject"]= item["value"]
            elif item["name"] == "Date":
                try:
                    mail_details["date_received"] = datetime.strptime(item["value"].split(" (")[0], "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d %H:%M:%S")
                except Exception as ex:
                    print(ex)
                    mail_details["date_received"]=""

