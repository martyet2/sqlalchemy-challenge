# Import the dependencies.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import numpy as np

from flask import Flask, jsonify



#################################################
# Database Setup
#################################################
# engine = create_engine('sqlite:///Resources/hawaii.sqlite')
# engine = create_engine('sqlite:///Users/martinthompson/Desktop/UCF_Bootcamp/SurfsUp/Resources/hawaii.sqlite')
database_path = "/Users/martinthompson/Desktop/UCF_Bootcamp/SurfsUp/Resources/hawaii.sqlite"
engine = create_engine(f'sqlite:///{database_path}')                     

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
# Base.prepare(engine, reflect=True)
Base.prepare(autoload_with=engine)
# Save references to each table
Measure = Base.classes.measurement
Station = Base.classes.station
session = Session(engine)

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route('/api/v1.0/stations')
def stations():
    # Add your code for the stations route here
    pass

@app.route('/api/v1.0/temp/<start>')
def start_temp(start):
    pass
    

@app.route('/api/v1.0/precipitation/<start>/<end>')
def start_end_precipitation(start, end):
    pass



# /api/v1.0/tobs
# /api/v1.0/precipitation
# /api/v1.0/stations
# /api/v1.0/temp/<start>
# /api/v1.0/precipitation/<start>/<end>
@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"<p>'start' and 'end' date should be in the format MMDDYYYY.</p>"

    )