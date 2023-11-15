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
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# welcome page and routes
@app.route("/")
def welcome():
    return (
        f"Available Static Routes:<br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"Summary Statistics Dynamic Date Range Routes:<br/><br/>"
        f"~~~ start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/ <br/>"
        f"~~~ start/end  (enter as YYYY-MM-DD/YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end"
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

# dynamic dates route start to end of data
@app.route("/api/v1.0/<start>")

def summary_stats_start(start):
    
    # acknowledge server request
    print("Server received request for 'summary stats' page...")
    
    # define variables
    selection = [func.min(Measurement.tobs),
                        func.round(func.avg(Measurement.tobs), 2),
                        func.max(Measurement.tobs)]
    
    # start your session engines!
    session = Session(engine)   
        
    # save session query
    results = session.query(*selection).\
        filter(Measurement.date >= start).all()
    session.close()
        
    # save list from list of tuples
    summary_stats = list(np.ravel(results))
    # insert labels
    summary_stats.insert(0, 'Minimum Temperature')
    summary_stats.insert(2, 'Average Temperature')
    summary_stats.insert(4, 'Maximum Temperature')
        
    return jsonify(summary_stats)

# dynamic dates route start to end
@app.route("/api/v1.0/<start>/<end>")

def summary_stats_start_end(start, end):
    
    # acknowledge server request
    print("Server received request for 'summary stats' page...")
    
    # define variables
    selection = [func.min(Measurement.tobs),
                        func.round(func.avg(Measurement.tobs), 2),
                        func.max(Measurement.tobs)]
    
    # start your session engines!
    session = Session(engine)   
        
    # save session query
    results = session.query(*selection).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    session.close()
        
    # save list from list of tuples
    summary_stats = list(np.ravel(results))
    # insert labels
    summary_stats.insert(0, 'Minimum Temperature')
    summary_stats.insert(2, 'Average Temperature')
    summary_stats.insert(4, 'Maximum Temperature')
        
    return jsonify(summary_stats) 
    

if __name__ == '__main__':
    app.run(debug=True)


