from flask import Flask, request, jsonify, url_for
from threading import Thread
from time import sleep
from functions import *

app = Flask(__name__)

threads = []

data = []

# Generates a public version of data to be sent to the client
def make_public_data(data):
    new_data = {}
    for name in data:
        if name == 'name':
            new_data['URL'] = url_for('getOne', name = data['name'], _external = True)
        else:
            new_data[name] = data[name]
    return new_data 

@app.route('/', methods=['GET'])
def welcomeMessage():
    return jsonify({'Networking Programming' : 'Laboratory Work Nr.3'})

@app.route('/getData', methods=['GET'])
def returnAll():
    return jsonify({'Data' : data})

@app.route('/getData/<string:name>', methods=['GET'])
def getOne(name):
    theOne = list(filter(lambda l: l['name'] == name, data)) 
    return jsonify({'Specific Data:' : make_public_data(theOne[0])})

@app.route('/postData', methods=['POST'])
def addOne():
    new_item = request.get_json()
    data.append(new_item)
    return jsonify({'Data' : data})

@app.route('/putData/<string:name>', methods=['PUT'])
def editOne(name):
    new_item = request.get_json()
    for i, q in enumerate(data):
      if q['name'] == name:
        data[i] = new_item    
    return jsonify({'Data' : data})

@app.route('/deleteData/<string:name>', methods=['DELETE'])
def deleteOne(name):
    for i, q in enumerate(data):
      if q['name'] == name:
        del data[i]  
    return jsonify({'Data' : data})

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
    for thread in threads:
        thread.start()
        sleep(4)
    for thread in threads:
        thread.join()
        
if __name__ == "__main__":
    run_requests()