from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable


def to_date_df(df, fmt, fld):
    return df.withColumn(fld, to_date(col(fld), fmt))


if __name__ != "__main__":
    pass
else:
    spark = SparkSession \
        .builder \
        .master("local") \
        .appName("RowDemo").getOrCreate()

    mySchema = StructType([
        StructField("ID", StringType(), True),
        StructField("EventDate", StringType(), True)
    ])

    my_rows = [Row("123", "04/05/2020"), Row("124", "4/5/2020"), Row("125", "04/5/2020"), Row("126", "4/05/2020")]
    my_rdd = spark.sparkContext.parallelize(my_rows, 2)

    my_df = spark.createDataFrame(my_rdd, mySchema)

    my_df.printSchema()
    my_df.show()
    new_df = to_date_df(my_df, "M/d/y", "EventDate")
    new_df.printSchema()
    new_df.show()
