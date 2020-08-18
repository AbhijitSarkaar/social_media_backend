from flask import Flask, jsonify, make_response, request
from flask_mysqldb import MySQL
import db_config
from utils import user_util

# initialize the app. creating an instance of Flask class
app = Flask(__name__)

#configure mysql
app.config['MYSQL_HOST'] = db_config.MYSQL_HOST
app.config['MYSQL_USER'] = db_config.MYSQL_USER
app.config['MYSQL_PASSWORD'] = db_config.MYSQL_PASSWORD
app.config['MYSQL_DB'] = db_config.MYSQL_DB

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
    rows = []
    for row in userDetails:
      rows.append(user_util(row))
    return jsonify(rows)

@app.route('/create_user', methods=['POST'])
def create_user():
  if request.method == 'POST':
    _first = request.form['first_name']
    _last = request.form['last_name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (first_name, last_name) VALUES (%s, %s)", (_first, _last))
    mysql.connection.commit()
    cur.close()
    return {'status': 200, 'message': 'Inserted Successfully'}

@app.route('/update_user', methods=['PATCH'])
def update_user():
  if request.method == 'PATCH':
    _id = request.form['id']
    _first = request.form['first_name']
    _last = request.form['last_name']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET first_name=%s, last_name = %s WHERE id = %s", (_first, _last, _id))
    mysql.connection.commit()
    cur.close()
    return {'status': 200, 'message': 'Updated Successfully'}

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