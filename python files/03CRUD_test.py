import requests, json, io
URL = 'http://127.0.0.1:8000/studentapi/'

def get_data(id= None):
    data = {}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    res = requests.get(url=URL, data= json_data )
    data = res.json()
    print(data)
# get_data()

def post_data():
    data = {
        'name' : 'rohit',
        'roll' : 101,
        'city' : 'jaunpur'
    }
    json_data = json.dumps(data)
    res = requests.post(url=URL, data= json_data )
    data = res.json()
    print(data)
# post_data()


# update -- 
def update_data():
    data = {
        'id' : 5,
        'name' : 'Mangesh',
        'roll' : 102,
        # 'city' : 'azamgarh'
    }
    json_data = json.dumps(data)
    res = requests.put(url=URL, data= json_data )
    data = res.json()
    print(data)
# update_data()


# delete --
def delete_data():
    data = {
        'id' : 4,
        
    }
    json_data = json.dumps(data)
    res = requests.delete(url=URL, data= json_data )
    data = res.json()
    print(data)
delete_data()