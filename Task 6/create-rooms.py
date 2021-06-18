# Fill in this file with the code to create a new room from the Webex Teams exercise
import requests
access_token = 'YWU1N2I1NWUtMDdhMC00NzI0LTgxYjQtZTFiODgwZDAzNWQyZWZkODM3MDItY2I2_PF84_4e1d5c08-564b-48e5-9d8f-c4e20787cdbf'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params={'title': 'netacad_devasc_skills_{{pgo}}'}
res = requests.post(url, headers=headers, json=params)
print(res.json())
