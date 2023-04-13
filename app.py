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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#use Base to reflect DB and reflect tables
Base = automap_base()
Base.prepare(engine, reflect=True)