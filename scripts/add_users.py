import yaml
import requests
import urllib3
from pathlib import Path

with open("users.yml", 'r') as users_file:
    data = yaml.safe_load(users_file)

with open(str(Path().resolve().parent) + '/defaults/main.yml', 'r') as vars_file:
    role_vars = yaml.safe_load(vars_file)

authentication = ('admin', role_vars['harbor_admin_password'])
url = "https://" + role_vars["harbor_hostname"] + "/api/v2.0/users"
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
for user_info in data['users']:
    response = requests.post(url, headers=headers, json=user_info, auth=authentication, verify=False)
    print('POST user:', user_info['username'], response)
