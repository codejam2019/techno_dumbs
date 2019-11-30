import pytest
from pyspark.sql import functions as F
from pyspark.sql.session import SparkSession


from  functions import report_aggregator
import json

@pytest.fixture(scope="session")
def spark_test_session():
    return (
        SparkSession
        .builder
        .master('local[*]')
        .appName('unit-testing')
        .getOrCreate()
    )

def run_aggregate():
    reportAgg = report_aggregator.data_agrregators("C:\\CodeJam\\sourceData\\", "C:\\CodeJam\\Destination\\")
    reportAgg.run_aggregate()
    df_out=spark_test_session.read.paquet("C:\\CodeJam\\Destination\\")
    assert 1==df_out.count


def read_source(spark_test_session):
    reportAgg=report_aggregator.data_agrregators("C:\\CodeJam\\sourceData\\","C:\\CodeJam\\Destination\\")
    print("hh")
    testdata='{"Wind_Speed": "4.4", "Solar_Radiation": "6", "Total_Rain": "15.2", "Timestamp": "02-02-2017 21:00", "Wind Direction": "293", "Rain_Intensity": "0", "Humidity": "56", "Measurement_ID": "63rdStreetWeatherStation201702022100", "Sensor_Location": "63rd Street Weather Station", "Barometric_Pressure": "1004.9", "Temperature": "-6.2"}'
    jsonData=json.loads(testdata)
    jsonStrings = ['{"Wind_Speed": "4.4", "Solar_Radiation": "6", "Total_Rain": "15.2", "Timestamp": "02-02-2017 21:00", "Wind Direction": "293", "Rain_Intensity": "0", "Humidity": "56", "Measurement_ID": "63rdStreetWeatherStation201702022100", "Sensor_Location": "63rd Street Weather Station", "Barometric_Pressure": "1004.9", "Temperature": "-6.2"}']
    otherPeopleRDD = spark_test_session.sparkContext.parallelize(jsonStrings)
    otherPeople = spark_test_session.read.json(otherPeopleRDD)
    expected=1
    output=otherPeople.count


    assert output == expected

def write_destination():
    reportAgg = report_aggregator.data_agrregators("C:\\CodeJam\\sourceData\\", "C:\\CodeJam\\Destination\\")
    testdata = '{"Wind_Speed": "4.4", "Solar_Radiation": "6", "Total_Rain": "15.2", "Timestamp": "02-02-2017 21:00", "Wind Direction": "293", "Rain_Intensity": "0", "Humidity": "56", "Measurement_ID": "63rdStreetWeatherStation201702022100", "Sensor_Location": "63rd Street Weather Station", "Barometric_Pressure": "1004.9", "Temperature": "-6.2"}'
    jsonData = json.loads(testdata)
    jsonStrings = [
        '{"Wind_Speed": "4.4", "Solar_Radiation": "6", "Total_Rain": "15.2", "Timestamp": "02-02-2017 21:00", "Wind Direction": "293", "Rain_Intensity": "0", "Humidity": "56", "Measurement_ID": "63rdStreetWeatherStation201702022100", "Sensor_Location": "63rd Street Weather Station", "Barometric_Pressure": "1004.9", "Temperature": "-6.2"}']
    otherPeopleRDD = spark_test_session.sparkContext.parallelize(jsonStrings)
    otherPeople = spark_test_session.read.json(otherPeopleRDD)
    reportAgg.write_destination(otherPeople)
    expected=1
    assert expected==1


