from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql import functions as F
from pyspark.sql import DataFrame


class SparkDataFrameUtils(object):
    @staticmethod
    def convert_json_to_df(spark_session: SparkSession, path_to_file: str, schema: StructType) -> DataFrame:
        return spark_session.read.schema(schema).option('multiline', True).json(path_to_file)

    @staticmethod
    def convert_rows_to_timestamp(column_names: list, df: DataFrame) -> DataFrame:
        for column_name in column_names:
            df = df.withColumn(column_name, F.to_timestamp(F.col(column_name)))
        return df




# if __name__ == '__main__':
#     from pyspark.sql import SparkSession
#     from src.services.data_processor.github_processor import GitHubDataProcessor
#     from src.services.utils.spark.spark_config import SparkConfig
#     from src.services.dataframe.schema.github_shema import Schema
#     path = "/Users/kate/PycharmProjects/home-assignment/result/json/pr_data.json"
#
#     df = DataFrameService().json_transform_to_dataframe(SparkConfig.get_basic_instance("test"),
#         path, Schema.github_event_schema)
#
#     GitHubDataProcessor(df).process_github_pr()
#
#
#     # df\
#     #     .withColumn("merged_at(timestamp)", to_timestamp(col("merged_at")))\
#     #     .withColumn("closed_at(timestamp)", to_timestamp(col("closed_at")))\

