import os

os.environ["hf_mysql_host"]="127.0.0.1"
os.environ["hf_mysql_user"] = "root"
os.environ["hf_mysql_password"]="password"  
os.environ["hf_db_name"] = "gmail_api_demo"

batch_size = 10
list_iteration = 10