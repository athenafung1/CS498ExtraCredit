from flask import Flask, request
import socket
from subprocess import Popen

app = Flask(__name__)

seed = 0

@app.route('/', methods = ['POST', 'GET'])
def server():
    # To change the value of a global variable inside a function, 
    # refer to the variable by using the global keyword
    global seed
    if request.method == 'POST':
        subprocess.Popen('python3 stress_cpu.py')
        # seed = int(request.json['num'])
        # return str(seed)
    if request.method == 'GET':
        # return str(seed)
        return socket.gethostname()
    return 'Hello World'

if __name__ == '__main__':
    # app.run(hostname to listen to, port, bool to provide debug information, options)
    app.run(host='0.0.0.0', port=5000, debug=True)