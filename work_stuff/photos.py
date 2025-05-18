import json

f = open('users_beruit.json')
data = json.load(f)
cleanData = []
for x in data:
	link = x['image']['link']
	kind = x['kind']
	# is_student = True
	# if kind != 'student':
	# 	is_student = False
	is_student = False
	name = x['login']
	if link != None:
			entry = {}
			entry['image_path'] = '/kaggle/input/0x2ahack-data/images/' + name + '.jpg'
			entry['is_student'] = is_student
			cleanData.append(entry)
			entry2 = {}
			entry2['image_path'] = '/kaggle/input/0x2ahack-data/images/' + name + '_mirrored' + '.jpg'
			entry2['is_student'] = is_student
			cleanData.append(entry2)
f.close()
f = open('cleanBeruit.json', 'w')
f.write(json.dumps(cleanData))

# import requests
# import json

# f = open("users_beruit.json")
# data = json.load(f)
# for x in data:
# 	if x['image']['link'] != None:
# 		resp = requests.get(x['image']['link'])
# 		file = open('./beiruit_images/' + x['login'] + '.jpg', 'wb')
# 		file.write(resp.content)
# 		file.close()