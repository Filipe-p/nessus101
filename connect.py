# Importing dependencies 
import requests
import getpass
# import pdb

## Vars
# tn_user_name = input("Tenable user name: \n")
# tn_pass = input("Tenable passworkd: \n")
tn_user_name = "FilipeP" # not for prod
tn_pass = getpass.getpass("Tenable password: \n") # Not for prod
# tn_host = "0.0.0.0"
# tn_url_base = f'https://{tn_host}:8834/'

# ## Loggin specific
# data_block = {'username': tn_user_name, 'password': tn_pass}
# tn_url_path = 'session'
# tn_urL_request = tn_url_base + tn_url_path

# tn_connection = requests.post(tn_urL_request, data=data_block, verify=False)

# print(tn_connection.status_code)

class Tn_connection:

    #initialize connection
    def __init__(self, tn_user_name, tn_pass, tn_host='0.0.0.0'):
        self.tn_user = tn_user_name
        self.__tn_pass = tn_pass
        self.tn_host = tn_host
        self.tn_url_base = f'https://{self.tn_host}:8834/'
        self.tn_url_path = 'session'
        self.tn_urL_request = self.tn_url_base + self.tn_url_path

        self.tn_connection = requests.post(self.tn_urL_request, {'username': self.tn_user, 'password': self.__tn_pass}, verify=False)
        self.status =  self.tn_connection.status_code
        self.json = self.tn_connection.json()
        self.md5sum_wizard_templates = self.tn_connection.json()['md5sum_wizard_templates']
        self.token = self.tn_connection.json()['token']
        self.md5sum_tenable_links = self.tn_connection.json()['md5sum_tenable_links']



connection2 = Tn_connection(tn_user_name, tn_pass)

print(connection2.tn_connection)
print(connection2.status)