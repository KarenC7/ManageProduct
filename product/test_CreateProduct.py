from django.test import TestCase
import os
import json
import requests

# API URL
url = 'http://localhost:8000/products/'

def test_create_new_product():
    file = open('C:\\Users\\kcastillo\\Desktop\\CreateNewProduct.json','r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response =requests.post(url,request_json)
    assert response.status_code == 201
    print(response.headers.get('Content-Length'))
    response.json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json,'id')
    print(id[0])