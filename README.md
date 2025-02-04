### Steps to run the application:
* Clone the app in local
* Install the requirements.txt
* Ensure mysql is running in local
* Enable google gmail api via oauth on your gmail account. Follow this [link](https://developers.google.com/gmail/api/quickstart/python)
* Copy the oauth json downloaded from google and place it on root dir in the name `credentials.json`
* Update the mysql connection details in `db_config.py`
* Optional : Run the command `python db/create_table.py` to create database and table.
* Run main program from root dir `python gmail_api_demo.py`
