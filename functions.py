import requests
import json
from time import sleep

def print_welcome_message():
    welcomeURL = 'http://localhost:5000/'
    request1 = requests.get(welcomeURL)
    data1 = request1.json()
    data1_formatted = json.dumps(data1, indent = 2)
    print("Welcome Message:")
    print(data1_formatted)
    sleep(3)
    
def print_all_data():
    print("Empty Data:")
    allDataURL = 'http://localhost:5000/getData'
    request2 = requests.get(allDataURL)
    data2 = request2.json()
    data2_formatted = json.dumps(data2, indent = 2)
    print(data2_formatted)
    sleep(3)
    
def post_all_data():
    print("Add Data:")
    postAllDataURL = 'http://localhost:5000/postData'
    data = []
    data0 = {'name': 'name1', 'age': '21'}
    data.append(data0)
    data1 = {'name': 'name2', 'age': '45'}
    data.append(data1)
    data2 = {'name': 'name3', 'age': '37'}
    data.append(data2)
    data3 = {'name': 'name4', 'age': '15'}
    data.append(data3)
    data4 = {'name': 'name5', 'charge': '78'}
    data.append(data4)
    for i in data:
        request4 = requests.post(postAllDataURL, json = i)
    requested_data = request4.json()
    requested_data_formatted = json.dumps(requested_data, indent = 2)
    print(requested_data_formatted)
    sleep(3)
    
def print_data():
    URL1 = 'http://localhost:5000/getData/name1'
    request1 = requests.get(URL1)
    data1 = request1.json()
    data1_formatted = json.dumps(data1, indent = 2)
    print(data1_formatted)
    URL2 = 'http://localhost:5000/getData/name2'
    request2 = requests.get(URL2)
    data2 = request2.json()
    data2_formatted = json.dumps(data2, indent = 2)
    print(data2_formatted)
    URL3 = 'http://localhost:5000/getData/name3'
    request3 = requests.get(URL3)
    data3 = request3.json()
    data3_formatted = json.dumps(data3, indent = 2)
    print(data3_formatted)
    URL4 = 'http://localhost:5000/getData/name4'
    request4 = requests.get(URL4)
    data4 = request4.json()
    data4_formatted = json.dumps(data4, indent = 2)
    print(data4_formatted)
    URL5 = 'http://localhost:5000/getData/name5'
    request5 = requests.get(URL5)
    data5 = request5.json()
    data5_formatted = json.dumps(data5, indent = 2)
    print(data5_formatted)
    sleep(3)