import requests, json

URL = 'http://127.0.0.1:8000/stud_create/'
data = {
    'name': 'Mangesh',
    'roll' : 101,
    'city' : "thekma"
}
json_data = json.dumps(data )
res = requests.post(url=URL, data=json_data)
print(res.json())