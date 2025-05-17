import requests
import json
import os

client_id = 'u-s4t2ud-450e395d8d86e115f4dc21269519cb43b74411becbd493fc8262d5df3861bdb9'
client_secret = os.environ['HACK_SECRECT']
token_url = 'https://api.intra.42.fr/oauth/token'
data = {
	'grant_type': 'client_credentials',
	'client_id': client_id,
	'client_secret': client_secret,
}
response = requests.post(token_url, data=data)
if response.status_code == 200:
	access_token = response.json()['access_token']
	headers = {
		'Authorization': f'Bearer {access_token}'
	}
	users = []
	pageN = 1
	while pageN < 29:
		response = requests.get('https://api.intra.42.fr/v2/campus/71/users', params={'page': pageN}, headers=headers)
		if response.status_code != 200:
			break
		data = response.json()
		if not data:
			break
		users.extend(data)
		pageN += 1
	with open("users", "w") as f:
		f.write(json.dumps(users, indent=2))
else:
	print("Error fetching token:", response.status_code, response.text)
