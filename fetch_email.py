import os
import base64

from googleapiclient.errors import HttpError
from bs4 import BeautifulSoup
from datetime import datetime
from gmail_service import GmailService
from db.gmail_msg import GmailMsg



class FetchEmail:

    # time constraint as input to this method??
    def execute(self):
        try:
            results = GmailService.get().users().messages().list(userId="me").execute()
            insert_mail_details = []
            for msg in results["messages"][:10]:
                msg = GmailService.get().users().messages().get(userId="me", id=msg["id"]).execute()
                internal_date = str(datetime.fromtimestamp(int(msg["internalDate"])/1000).strftime('%Y-%m-%d %H:%M:%S'))
                mail_details = {"msg_id": msg["id"], "thread_id": msg["threadId"], "internal_date": internal_date}
                self._get_header(msg["payload"]["headers"], mail_details)
                try:
                    for part in msg["payload"]["parts"]:
                        if 'body' in part and 'data' in part["body"]:
                            body_data = part["body"]["data"]
                            body = base64.urlsafe_b64decode(body_data).decode('utf-8')
                            mail_details["body"] = BeautifulSoup(body, 'html.parser').get_text()
                except Exception as ex:
                    mail_details["body"] = ""
                    print("Unable to get body for msg id " + msg["id"])

                # print(mail_details)
                insert_mail_details.append(mail_details)
                # print("-------")

            print(results["nextPageToken"])
            print(results["resultSizeEstimate"])
            GmailMsg().insert(insert_mail_details)

        except HttpError as error:
            print(f"An error occurred: {error}")
    
    def _get_header(self, headers, mail_details):
        for item in headers:
            if item["name"] == "From":
                mail_details["from_address"] = item["value"]
            elif item["name"] == "Subject":
                mail_details["subject"]= item["value"]
            elif item["name"] == "Date":
                print(item["value"])
                mail_details["date_received"] = datetime.strptime(item["value"].split(" (")[0], "%a, %d %b %Y %H:%M:%S %z").strftime("%Y-%m-%d %H:%M:%S")

