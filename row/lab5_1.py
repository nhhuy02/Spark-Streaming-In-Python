from pyspark import Row
from pyspark.sql import SparkSession

import os
import sys

from pyspark.sql.functions import *
from pyspark.sql.types import *

os.environ['PYSPARK_PYTHON'] = sys.executable

spark = SparkSession.builder.appName('local').getOrCreate()


def to_date_df(df, dateformat, field):
    return df.withColumn(field, to_date(col(field), dateformat))


if __name__ == '__main__':
    my_rows = [Row("123", "04/05/2020"), Row("124", "4/5/2020"), Row("125", "04/5/2020"), Row("126", "4/05/2020")]
    my_schema = StructType([
        StructField("ID", StringType(), True),
        StructField("EventDate", StringType(), True)
    ])
    my_rdd = spark.sparkContext.parallelize(my_rows, 2)
    my_df = spark.createDataFrame(my_rdd, my_schema)
    my_df.printSchema()
    my_df.show()

    new_df = to_date_df(my_df, 'M/d/y', 'EventDate')
    new_df.printSchema()
    new_df.show()
