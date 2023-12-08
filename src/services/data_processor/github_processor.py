from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from src.services.dataframe.dataframe_service import SparkDataFrameUtils
from src.services.dataframe.sort.sort_data import SortGitHubData
from src.services.dataframe.aggregate.aggregate_data import DataAggregator


class GitHubDataProcessor:
    def __init__(self, raw_df: DataFrame):
        self.raw_df = raw_df

    @staticmethod
    def calculate_is_compliant_col(grouped_df: DataFrame):
        return grouped_df.withColumn(
            "is_compliant", (grouped_df["num_prs"] == grouped_df["num_prs_merged"]) &
                            (F.col("owner").contains("Scytale")))

    def process_github_pr(self):
        df_timestamps = SparkDataFrameUtils.convert_rows_to_timestamp(
            ["closed_at", "merged_at"], self.raw_df)
        sorted_df = SortGitHubData(
            df_timestamps.withColumn("organization_name",
                                     F.split(df_timestamps["repo"], "/")[0]),
            "id_pull_request", "closed_at").sort_to_state_prs()
        return self.calculate_is_compliant_col(DataAggregator.group_by_columns(sorted_df))








