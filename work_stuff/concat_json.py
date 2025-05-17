import json

result = []
f1 = open('cleanAmman.json', 'r')
result.extend(json.load(f1))
f1.close()
f2 = open('cleanBeruit.json', 'r')
result.extend(json.load(f2))
f2.close()
f3 = open('cleanResult.json', 'w')
json.dump(result, f3)