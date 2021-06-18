# Fill in this file with the messages code from the Webex Teams exercise
import requests
access_token = 'YWU1N2I1NWUtMDdhMC00NzI0LTgxYjQtZTFiODgwZDAzNWQyZWZkODM3MDItY2I2_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf'
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNWY2ZDBhNzAtZDAxZS0xMWViLTg0NjgtNTUzNmNkMTU0ZjYx'
message = 'Here are my screenshots of netacad-devasc skills-based exam'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
