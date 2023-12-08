from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window


class SortGitHubData(object):
    CLOSED_STATE = "closed"
    OPEN_STATE = "open"

    def __init__(self, df: DataFrame, partition_value: str, column_ts: str):
        self.window_spec = Window.partitionBy(partition_value).orderBy(F.desc(column_ts))
        self.df = df

    def sort_to_state_prs(self) -> DataFrame:
        df_ranked = self.df.withColumn("row_num", F.row_number().over(self.window_spec))
        return df_ranked.filter(
            (df_ranked["state"] == self.CLOSED_STATE) |
            ((df_ranked["state"] == self.OPEN_STATE) &
             (df_ranked["row_num"] == 1))).drop("row_num")
