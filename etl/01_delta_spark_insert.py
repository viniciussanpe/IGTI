from pyspark.sql import SparkSession
from pyspark.sql import functions as f
from pyspark.sql.functions import col, min, max


# Cria objeto da Spark Session
spark = (SparkSession.builder.appName("DeltaExercise")
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

# Importa o modulo das tabelas delta
from delta.tables import *

# Leitura de dados
enem = (
    spark.read.format("csv")
    .option("inferSchema", True)
    .option("header", True)
    .option("delimiter", ";")
<<<<<<< HEAD
    .option( "encoding", "latin1")
    .load("s3://datalake-vini-igti-edc-tf/csv/rais")
=======
    .load("s3://datalake-ney-igti-edc/raw-data/enem")
>>>>>>> parent of 8e0743c (fix spark configs)
)

# Escreve a tabela em staging em formato delta
print("Writing delta table...")
(
    enem
    .write
    .mode("overwrite")
    .format("delta")
    .partitionBy("year")
<<<<<<< HEAD
    .save("s3://datalake-vini-igti-edc-tf/raw-data/rais")
=======
    .save("s3://datalake-ney-igti-edc-tf/staging-zone/enem")
>>>>>>> parent of 8e0743c (fix spark configs)
)


