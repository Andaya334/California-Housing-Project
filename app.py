import sqlite3
from flask import Flask, render_template, jsonify

# create a Flask app
app = Flask(__name__)

# connect to the SQLite database
conn = sqlite3.connect('Housing_Table.sqlite')
cur = conn.cursor()

# check that we can fetch data from the Housing table
res = cur.execute('SELECT * FROM Housing')
print(res.fetchone())

# define some API endpoints
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/housing')
def get_housing():
    cur.execute('SELECT * FROM Housing')
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/distance_to_la/<float:distance>')
def get_housing_by_distance_to_la(distance):
    cur.execute('SELECT * FROM Housing WHERE Distance_to_LA <= ?', (distance,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/distance_to_sf/<float:distance>')
def get_housing_by_distance_to_sf(distance):
    cur.execute('SELECT * FROM Housing WHERE Distance_to_SanFrancisco <= ?', (distance,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/distance_to_sd/<float:distance>')
def get_housing_by_distance_to_sd(distance):
    cur.execute('SELECT * FROM Housing WHERE Distance_to_SanDiego <= ?', (distance,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/distance_to_sj/<float:distance>')
def get_housing_by_distance_to_sj(distance):
    cur.execute('SELECT * FROM Housing WHERE Distance_to_SanJose <= ?', (distance,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/distance_to_coast/<float:distance>')
def get_housing_by_distance_to_coast(distance):
    cur.execute('SELECT * FROM Housing WHERE Distance_to_coast <= ?', (distance,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/median_house_value/<int:value>')
def get_housing_by_median_house_value(value):
    cur.execute('SELECT * FROM Housing WHERE Median_House_Value = ?', (value,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/median_income/<int:value>')
def get_housing_by_median_income(value):
    cur.execute('SELECT * FROM Housing WHERE Median_Income = ?', (value,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/median_age/<int:value>')
def get_housing_by_median_age(value):
    cur.execute('SELECT * FROM Housing WHERE Median_Age = ?', (value,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/tot_rooms/<int:value>')
def get_housing_by_tot_rooms(value):
    cur.execute('SELECT * FROM Housing WHERE Tot_Rooms = ?', (value,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/tot_bedrooms/<int:value>')
def get_housing_by_tot_bedrooms(value):
    cur.execute('SELECT * FROM Housing WHERE Tot_Bedrooms = ?', (value,))
    data = cur.fetchall()
    return jsonify(data)

@app.route('/api/housing/population/<int:value>')
def get_housing_by_population(value):
    cur.execute('SELECT * FROM Housing WHERE Population = ?', (value,))
    data = cur.fetchall()
    return jsonify(data)



if __name__ == '__main__':
    app.run(debug=True)
