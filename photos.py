import json
import requests

f = open('users.json')
data = json.load(f)
for x in data:
	link = x['image']['link']
	name = x['login']
	if link != None:
		response = requests.get(link)
	if response.status_code == 200:
		with open(name + '.jpg', 'wb') as file:
			file.write(response.content)
			file.close()
	print(link)
f.close()