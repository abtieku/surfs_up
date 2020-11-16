#9.5.1
#import our usual dependencies
import datetime as dt
import numpy as np
import pandas as pd

#import SQLAlchemy dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#add dependencies needed for Flask
from flask import Flask, jsonify

#set up database engine
engine = create_engine("sqlite:///hawaii.sqlite")

#reflect the database into our classes
Base = automap_base()
Base.prepare(engine, reflect=True)

#create variables for the classes so we can reference them later
Measurement = Base.classes.measurement
Station = Base.classes.station

#create session link from Python to our database
session = Session(engine)

#define Flask app - will create a Flask app called app
app = Flask(__name__)

#9.5.2
#welcome route
@app.route("/")

#define function called welcome
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')
#9.5.3
#Route for precipitation analysis
@app.route("/api/v1.0/precipitation")

#define precipitation function
def precipitation():
   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
   precipitation = session.query(Measurement.date, Measurement.prcp).\
    filter(Measurement.date >= prev_year).all()
   precip = {date: prcp for date, prcp in precipitation}
   return jsonify(precip)

#9.5.4
#add the stations route
@app.route("/api/v1.0/stations")

#new function called stations
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)

#9.5.5
#add the temperature route
@app.route("/api/v1.0/tobs")

#create function for temps
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

#9.5.6
#create route for statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

#function called stats
def stats(start=None, end=None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
