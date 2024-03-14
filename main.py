import os, dotenv
from dotenv import load_dotenv

load_dotenv('keys.env')

public_key = os.getenv('PUBLIC_KEY')
application_id = os.getenv('APPLICATION_ID')

print(public_key)
print(application_id)
