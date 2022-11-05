from flask import Flask, request, jsonify
from threading import Thread
from time import sleep
from functions import *

app = Flask(__name__)

threads = []

data = []

@app.route('/', methods=['GET'])
def welcomeMessage():
    return jsonify({'Networking Programming' : 'Laboratory Work Nr.3'})

@app.route('/getData', methods=['GET'])
def returnAll():
    return jsonify({'Data' : data})

@app.route('/getData/<string:name>', methods=['GET'])
def getOne(name):
    theOne = list(filter(lambda l: l['name'] == name, data)) 
    return jsonify({'Specific Data' : theOne[0]})

@app.route('/postData', methods=['POST'])
def addOne():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify({'Data' : data})

@app.route('/putData/<string:name>', methods=['PUT'])
def editOne(name):
    theOne = list(filter(lambda l: l['name'] == name, data))
    theOne[0]['name'] = request.json.get('name', theOne[0]['name'])
    theOne[0]['age'] = request.json.get('age', theOne[0]['age'])
    return jsonify({'Edited Data' : theOne[0]})

@app.route('/deleteData/<string:name>', methods=['DELETE'])
def deleteOne(name):
    theOne = list(filter(lambda l: l['name'] == name, data))
    data.remove(theOne[0])  
    return jsonify({'Data Delete' : data})

def run_requests():
    main_thread = Thread(target = lambda: app.run(host = '0.0.0.0', port = 5000, debug = False, use_reloader = False), daemon = True)
    threads.append(main_thread)
    thread1 = Thread(target = print_welcome_message, name = "Thread1")
    threads.append(thread1)
    thread2 = Thread(target = print_all_data, name = "Thread2")
    threads.append(thread2)
    thread3 = Thread(target = post_all_data, name = "Thread3")
    threads.append(thread3)
    thread4 = Thread(target = print_data, name = "Thread4")
    threads.append(thread4)
    thread5 = Thread(target = put_data, name = "Thread5")
    threads.append(thread5)
    thread6 = Thread(target = print_all_data, name = "Thread6")
    threads.append(thread6)
    thread7 = Thread(target = delete_data, name = "Thread7")
    threads.append(thread7)
    for thread in threads:
        thread.start()
        sleep(4)
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    run_requests()