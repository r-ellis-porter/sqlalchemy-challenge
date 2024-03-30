# SQLAlchemy Climate Analysis

## Overview/Purpose

Welcome to the SQLAlchemy Climate Analysis project! This project aims to conduct a comprehensive climate analysis of Honolulu, Hawaii, utilizing Python, SQLAlchemy, and Flask. The analysis includes exploring climate data, performing precipitation and station analysis, and designing a Flask API to present the findings.

### Important Findings

#### Precipitation Analysis

- The most recent date in the dataset is 2017-08-23.
- Precipitation data for the previous 12 months has been analyzed and visualized.
- Summary statistics for precipitation data:
  - Count: 2021
  - Mean: 0.177 inches
  - Standard Deviation: 0.461 inches
  - Min: 0.0 inches
  - 25th Percentile: 0.0 inches
  - Median: 0.02 inches
  - 75th Percentile: 0.13 inches
  - Max: 6.7 inches

#### Station Analysis

- Total number of stations in the dataset: 9
- Most active stations and their observation counts:
  - USC00519281: 2772
  - USC00519397: 2724
  - USC00513117: 2709
  - USC00519523: 2669
  - USC00516128: 2612
  - USC00514830: 2202
  - USC00511918: 1979
  - USC00517948: 1372
  - USC00518838: 511
- For the most active station (USC00519281):
  - Lowest Temperature: 54.0°F
  - Highest Temperature: 85.0°F
  - Average Temperature: 71.66°F
- Temperature observation data (TOBS) for the last 12 months has been analyzed and visualized as a histogram.

### Summary

This project provides valuable insights into the climate of Honolulu, Hawaii, by analyzing historical weather data. Through precipitation and station analysis, significant patterns and trends have been identified, aiding in understanding the climate characteristics of the region. Additionally, a Flask API has been designed to provide easy access to the analyzed data, allowing for further exploration and utilization in trip planning and research activities.

## Technical Details

- The project utilizes Python, SQLAlchemy, Pandas, and Matplotlib for data analysis and visualization.
- A SQLite database containing weather data is accessed and queried using SQLAlchemy.
- Flask is employed to create a web API, offering endpoints for accessing precipitation data, station information, temperature observations, and summary statistics based on dynamic date ranges.

For more detailed technical information, please refer to the provided Jupyter Notebook (`analysis.ipynb`) and Flask application script (`app.py`).

**Note:** Before running the code, make sure to follow the setup instructions provided in the assignment. Additionally, ensure that all necessary dependencies are installed and that the SQLite database (`hawaii.sqlite`) and resource files are available in the appropriate directory.
