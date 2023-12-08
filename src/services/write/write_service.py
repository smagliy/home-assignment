import json

from pyspark.sql import DataFrame

from src.services.write import WriteService


class WriteJsonService(WriteService):
    def __init__(self, file_path: str, data):
        self.file_path = file_path
        self.data = data

    def write(self):
        with open(self.file_path, "w") as json_file:
            json.dump(self.data, json_file, indent=2)


class WriteParquetService(WriteService):
    def __init__(self, file_path: str, data):
        self.file_path = file_path
        self.data: DataFrame = data

    def write(self):
        self.data.write.parquet(self.file_path)