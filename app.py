# Import the dependencies.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
import numpy as np
import pandas as pd


from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

app = Flask(__name__)

database_path = "/Users/martinthompson/Desktop/UCF_Bootcamp/SurfsUp/Resources/hawaii.sqlite"
engine = create_engine(f'sqlite:///{database_path}')                     

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measure = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
# completed above in database setup

#################################################
# Flask Routes
#################################################
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

@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measure.date, Measure.prcp).filter(Measure.date >= prev_year).all()
    precipitation_data = pd.DataFrame(precipitation, columns=['date', 'prcp'])
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)

@app.route('/api/v1.0/stations')
def stations():
    stations = session.query(Station.station).all()
    return jsonify(stations)

@app.route('/api/v1.0/tobs')
def get_tobs():
    tobs = session.query(Measure.tobs).all()
    tobs_list = [tobs[0].tobs for tobs in tobs]
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def tobs_start_orm(start):
    data = sql.query_tobs_start(start)
    return jsonify(data)

@app.route("/api/v1.0/<start>/<end>")
def tobs_start_end(start, end):
    data = sql.query_tobs_start_end(start, end)
    return jsonify(data)

# Run the App
if __name__ == '__main__':
    app.run(debug=True)







    






















