import numpy as np
import re
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy.sql import exists  

from flask import Flask, jsonify

#Setup DB
engine = create_engine("sqlite:///Resources/")

#Postgres DB
connection_url = 'postgresql+psycopg2://user:password@localhost:5432/california_housing'
engine = create_engine(connection_url)

#use Base to reflect DB and reflect tables
Base = automap_base()
Base.prepare(engine, reflect=True)

#set up flask
print(__name__)
app = Flask(__name__)

#List available APIs
@app.route("/")
def home():
    """List all available api routes."""
    return (
        f""
    )

@app.route("/api/v1.0/sql")
def sql():
    session = Session(engine)
    results = session.query().all()
    session.close
    #convert list of tuples into normal list
    #CODE HERE

    return jsonify()




#Creat a dictionary from the raw data and appemd to a list of sql database
##CODE HERE!






if __name__ == '__main__':
    app.run(debug=True)
