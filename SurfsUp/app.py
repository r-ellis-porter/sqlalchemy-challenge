# Import the dependencies.
import numpy as np
import datetime as dt
import pandas as pd

import flask 
print(flask.__version__)
import sqlalchemy
print(sqlalchemy.__version__)
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# welcome page and routes
@app.route("/")
def welcome():
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#################################################
# Flask Routes
#################################################

# precipitation route
@app.route("/api/v1.0/precipitation")

def precipitation():

    # acknowledge server request
    print("Server received request for 'precipitation' page...")
    
    # define variables
    year_before = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    
    # save session query
    session = Session(engine)
    selection = [Measurement.date, Measurement.prcp]
    results = session.query(*selection).\
        filter(Measurement.date >= year_before).all()
    session.close()

    # dictionary comprehension
    precipitation = {date: prcp for date, prcp in results}
    
    return jsonify(precipitation)

# stations route
@app.route("/api/v1.0/stations")

def stations():
    
    # acknowledge server request
    print("Server received request for 'stations' page...")
    
    # save session query
    session = Session(engine)
    results = session.query(Station.station).all()
    session.close()
    
    # save list from list of tuples
    stations = list(np.ravel(results))
    
    return jsonify(stations)

# tobs route
@app.route("/api/v1.0/tobs")

def tobs():
    
    # acknowledge server request
    print("Server received request for 'tobs' page...")
    
    # define variables
    year_before = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    selection = [Measurement.date, Measurement.tobs]
    
    # save most active station
    session = Session(engine)    
    most_active = session.query(Measurement.station).\
        group_by(Measurement.station).\
        order_by(func.count(Measurement.station).desc()).first()
    
    # save session query
    results = session.query(*selection).\
        filter(Measurement.station == most_active[0]).\
        filter(Measurement.date >= year_before).all()
    session.close()
    
    # list comprehension
    temperatures = [(date, tobs) for date, tobs in results]
    
    return jsonify(temperatures)

    
    




