from flask import Flask, request
app = Flask(__name__)

seed = 0

@app.route('/', methods = ['POST', 'GET'])
def server():
    # To change the value of a global variable inside a function, 
    # refer to the variable by using the global keyword
    global seed
    if request.method == 'POST':
        seed = int(request.json['num'])
        return str(seed)
    if request.method == 'GET':
        return str(seed)
    return 'Hello World'

if __name__ == '__main__':
    # app.run(hostname to listen to, port, bool to provide debug information, options)
    app.run(host='0.0.0.0', port=5000, debug=True)


# The application handles the following two HTTP REST requests:

# HTTP POST "/" with JSON body {"num": 100} where 100 can be any integer.

# Your program should update the seed value with the given number.

# HTTP GET "/"

# Your program should return the integer seed value in string format. 
# The response body for the above case will be: "100"


# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World'

# if __name__ == '__main__':
#     app.run()