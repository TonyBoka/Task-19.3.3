import requests

import json

# пример запроса GET

status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status=available", headers={'accept': 'application/json'})
print(res.status_code, 'запрос Get')
print(res.json())

# пример запроса POST

new_pet = {
  "id": 9223372036854774423,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_p = requests.post(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
data = json.dumps(new_pet))
print(res_p.status_code, 'запрос Post')
print(res_p.json())

# пример запроса DELETE

res_d = requests.delete(f'https://petstore.swagger.io/v2/pet/9223372036854774423', headers = {'accept': 'application/json'})
print(res_d.status_code, 'запрос DELETE')
print(res_d.json())

# пример запроса PUT

data = {
  "id": 9223372036854774423,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
res_put = requests.put(f'https://petstore.swagger.io/v2/pet', headers = {'accept': 'application/json', 'Content-Type': 'application/json'},
data = json.dumps(data))
print(res_put.status_code, 'запрос PUT')
print(res_put.json())