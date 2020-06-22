import pyspark
import findspark
import os
findspark.init()
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName('sparktest').setMaster('spark://spark-master.default.svc.cluster.local:7077')
conf.set("spark.driver.bindAddress", "0.0.0.0")
conf.set("spark.driver.host", "jupyter.juphub.svc.cluster.local")
conf.set("spark.driver.port", "39777") # Set in jupyter-svc.yaml file
# need to be set in order to use python in spark worker
os.environ["PYSPARK_PYTHON"] = 'python3'
sc = SparkContext(conf=conf)
sc
# app code goes below
sc.parallelize([1,2,3,4,5]).count()





