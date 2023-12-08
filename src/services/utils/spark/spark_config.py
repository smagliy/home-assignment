from pyspark.sql import SparkSession


class SparkConfig:
    @staticmethod
    def get_basic_instance(app_name):
        return SparkSession.builder.appName(app_name).getOrCreate()