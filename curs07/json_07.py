import json
x = '{"name": "ion", "age": 30, "city": "iasi"}'
y = json.loads(x)
print(y, type(y))
z = json.dumps(y)
print(z, json.dumps(z), type(z))
a = ["mere", "pere"]
print(a, json.dumps(a), type(a))
a = "hello"
print(a, json.dumps(a), type(a))
a = 42
print(a, json.dumps(a), type(a))
a = 31.75
print(a, json.dumps(a), type(a))
a = True
print(a, json.dumps(a), type(a))
a = None
print(a, json.dumps(a), type(a))





