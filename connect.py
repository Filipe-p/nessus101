# Importing dependencies 
import requests
import getpass
# import pdb

## Vars
# tn_user_name = input("Tenable user name: \n")
# tn_pass = input("Tenable passworkd: \n")
tn_user_name = "FilipeP"
tn_pass = getpass.getpass("Tenable password: \n")
tn_host = "0.0.0.0"
tn_url_base = f'https://{tn_host}:8834/'

## Loggin specific
data_block = {'username': tn_user_name, 'password': tn_pass}
tn_url_path = 'session'
tn_urL_request = tn_url_base + tn_url_path

request_1 = requests.post(tn_urL_request, data=data_block, verify=False)

print(request_1.status_code)

# breakpoint()
