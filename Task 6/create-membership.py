# Fill in this file with the code to create a room membership from the Webex Teams exercise
import requests
access_token = 'YWU1N2I1NWUtMDdhMC00NzI0LTgxYjQtZTFiODgwZDAzNWQyZWZkODM3MDItY2I2_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNWY2ZDBhNzAtZDAxZS0xMWViLTg0NjgtNTUzNmNkMTU0ZjYx'
person_email = 'Yvan.Rooseleer@biasc.be'
url = 'https://webexapis.com/v1/memberships'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'personEmail': person_email}
res = requests.post(url, headers=headers, json=params)
print(res.json())