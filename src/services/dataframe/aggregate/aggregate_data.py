from pyspark.sql import DataFrame
from pyspark.sql import functions as F


class DataAggregator:
    @staticmethod
    def group_by_columns(df: DataFrame):
        grouped_df = (
            df.groupBy("organization_name", "repo_id", "repo", "owner")
              .agg(
                  F.count("id_pull_request").alias("num_prs"),
                  F.sum(F.when(df["merged_at"].isNotNull(), 1).otherwise(0)).alias("num_prs_merged"),
                  F.max("merged_at").alias("merged_at")
              )
        )
        return grouped_df
