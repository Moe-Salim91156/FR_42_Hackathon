import requests
import json
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
client_id = 'u-s4t2ud-450e395d8d86e115f4dc21269519cb43b74411becbd493fc8262d5df3861bdb9'
client_secret = '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'
redirect_uri = 'http://localhost:3000'
auth_url = (
	f'https://api.intra.42.fr/oauth/authorize?'
	f'client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
)
webbrowser.open(auth_url)
class Handler(BaseHTTPRequestHandler):
	def do_GET(self):
		parsed = urlparse(self.path)
		params = parse_qs(parsed.query)
		if 'code' in params:
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b"Authorization successful. You can close this window.")
			code = params['code'][0]
			print("Authorization code:", code)
			token_url = 'https://api.intra.42.fr/oauth/token'
			data = {
				'grant_type': 'authorization_code',
				'client_id': client_id,
				'client_secret': client_secret,
				'code': code,
				'redirect_uri': redirect_uri
			}
			response = requests.post(token_url, data=data)
			if response.status_code == 200:
				access_token = response.json()['access_token']
				headers = {
					'Authorization': f'Bearer {access_token}'
				}
				users = []
				pageN = 1
				while True:
					response = requests.get('https://api.intra.42.fr/v2/campus/35/users', params={'page': pageN}, headers=headers)
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
			def stop_server(server):
				server.shutdown()
			import threading
			threading.Thread(target=stop_server, args=(httpd,)).start()
		else:
			self.send_response(400)
			self.end_headers()
			self.wfile.write(b"Authorization code not found.")# Run the server
httpd = HTTPServer(('localhost', 3000), Handler)
print("Waiting for OAuth redirect...")
httpd.serve_forever()