from flask import Flask, jsonify, make_response, request
from flask_mysqldb import MySQL

# initialize the app. creating an instance of Flask class
app = Flask(__name__)

#configure mysql
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'BACKEND@2020'
app.config['MYSQL_DB'] = 'sql_store'

mysql = MySQL(app)

# create a root route
@app.route('/')
def index():
    return "Hello World!"

@app.route('/users')
def users():
  cur = mysql.connection.cursor()
  resultValue = cur.execute("SELECT * FROM users")
  if resultValue > 0:
    userDetails = cur.fetchall()
    print(userDetails)
    return jsonify(userDetails)

@app.route('/data')
def get_data():
    return jsonify(
      [{
        'name': 'Abhijit',
        'id': 1
      }, 
      {
        'name': 'Padmini',
        'id': 2
      }
      ])

app.run(port=5000,   # run the webserver or app on port 5000
        debug=True) # set debug = True when you are in development environment, to see updated changes without restarting server