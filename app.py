from flask import Flask, jsonify, make_response

# initialize the app. creating an instance of Flask class
app = Flask(__name__)

# create a root route
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/data')
def get_data():
    return jsonify([{
      'name': 'abhijit',
      'id': 1
    }])

app.run(port=5000,   # run the webserver or app on port 5000
        debug=True) # set debug = True when you are in development environment