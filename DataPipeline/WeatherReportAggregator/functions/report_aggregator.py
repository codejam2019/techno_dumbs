from pyspark.sql import SparkSession
from  pyspark.sql.functions import *
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext


class data_agrregators:
    def __init__(self, spark, source, destination):
        self.source = "C:\\CodeJam\\sourceData\\"
        self.destination = "C:\\CodeJam\\Destination\\"
        self.sparkSession = spark

    def read_source(self):
        df_input = self.sparkSession.read.option("header","true").json(self.source)

        return df_input

    def write_destination(self,df_aggregate):
        df_aggregate.write.option("hreader","true").mode("overwrite").csv(self.destination)
    def run_aggregate(self):
        df_input=self.read_source()
        df_input.registerTempTable("weatherData")

        df_aggregate=self.sparkSession.sql("select max(Temperature) as MAX_TEMP,min(Temperature) as MIN_TEMP,max(Total_Rain) as MAX_RAIN ,min(Total_Rain) as MIN_RAIN from weatherData group By City,SendorId,Date")
        self.write_destination(df_aggregate)


def main():
    spark = SparkSession.builder.appName("weather-report").getOrCreate()
    source = "C:\\CodeJam\\sourceData\\"
    destination = "C:\\CodeJam\\Destination\\"
    dataAgg=data_agrregators(spark, source, destination)
    dataAgg.run_aggregate()


if __name__ == "__main__":
    main()


