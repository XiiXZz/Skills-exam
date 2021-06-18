# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json
access_token = 'YWU1N2I1NWUtMDdhMC00NzI0LTgxYjQtZTFiODgwZDAzNWQyZWZkODM3MDItY2I2_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf'
url = 'https://webexapis.com/v1/people/me'
headers = {
 'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
