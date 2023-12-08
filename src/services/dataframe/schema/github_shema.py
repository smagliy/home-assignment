from pyspark.sql.types import StructType, StructField, StringType, IntegerType


class Schemas:
    github_event_schema = StructType([
        StructField("event_id", StringType(), True),
        StructField("actor", StringType(), True),
        StructField("repo", StringType(), True),
        StructField("repo_id", IntegerType(), True),
        StructField("action", StringType(), True),
        StructField("id_pull_request", IntegerType(), True),
        StructField("action_number", IntegerType(), True),
        StructField("state", StringType(), True),
        StructField("closed_at", StringType(), True),
        StructField("merged_at", StringType(), True),
        StructField("owner", StringType(), True)
    ])
