Title: How to read HAWQ Parquet tables from Spark
Date: 2015-12-06 21:05
Category: Spark
Tags: HAWQ, Spark
Slug: hawq-parquet-spark

Spark SQL still lags behind many SQL on Hadoop engines in performance,
reliability and functionality. As a data scientist, I really value
being able to write PySpark code in Jupyter Notebooks for exploratory
analysis, running unit tests using unittest/py.test and nosetests and
using the growing ecosystem of machine learning libraries on top of
Spark. Yet typical SQL tasks like joining datasets can be tedious and
slow in Spark SQL. Spark SQL also lacks functionality such as window
functions.

How can we get the best of both worlds? SQL on Hadoop engines such as
HAWQ can read and write Parquet files, which Spark is also able to
read and write. Using these, we can get the two systems to exchange
data with HDFS acting as a storage layer.

In HAWQ, you can create a table using Parquet as a storage format and
gzip as compression like so:

    :::sql
    CREATE TABLE :target_schema.my_tabe
    WITH (
    appendonly = TRUE,
    orientation = parquet,
    compresstype = gzip,
    compresslevel = 4) AS ..

Spark can read those Parquet tables from HDFS with a simple `sqlContext.read.parquet(filename)`:

    :::python
    from pyspark.sql import SQLContext
    sqlContext = SQLContext(sc)
    filenames = ['/hawq_data/gpseg' + str(i) + '/16385/26349/61298' for i in range(24)]
    file = sqlContext.read.parquet(*filenames)

One downside is that HAWQ stores tables across segments with a
randomly generated file path. To find the HDFS file path
programatically, you can actually query the database. The first part of
the file name (16385 in our case) always remains the same (determined by the database).

The middle part (26349) can be found using `SELECT oid,datname FROM my_table` and the final part (61298) with `SELECT 'my_table'::regclass::oid`.

Another downside is that you need to provide the number of HAWQ
segments (24) in this case. If you scale up your number of segments
you also have to adjust this in your Spark code, else you will
silently lose some of your data in Spark.

I am sure in the near future we will see more elegant ways to interact with Spark.
