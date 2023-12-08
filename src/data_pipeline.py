from src.services.extract.github.data_extractor import GitHubEventsExtractor
from src.services.write.write_service import WriteJsonService, WriteParquetService
from src.services.data_processor.github_processor import GitHubDataProcessor
from src.services.dataframe.dataframe_service import SparkDataFrameUtils
from src.services.utils.spark.spark_config import SparkConfig
from src.services.dataframe.schema.github_shema import Schemas
from src.services.utils.file_manager import FileManager
from src.config.config import Config


class DataPipeline:
    def __init__(self):
        self.raw_data_path = Config.RAW_DATA_PATH + Config.RAW_DATA_FILE_NAME
        self.spark_session = SparkConfig.get_basic_instance("GitHub data processing")
        self.trans_data_path = Config.RESULT_TRANSFORM_DATA_PATH

    def extract_data(self):
        data = GitHubEventsExtractor().get_pull_request_events()
        FileManager(Config.RAW_DATA_PATH).check_and_create_directory()
        WriteJsonService(self.raw_data_path, data).write()

    def transform_data(self):
        df_prs = SparkDataFrameUtils.convert_json_to_df(self.spark_session,
                                                        self.raw_data_path,
                                                        Schemas.github_event_schema)
        return GitHubDataProcessor(df_prs).process_github_pr()

    def load_data(self):
        WriteParquetService(self.trans_data_path, self.transform_data()).write()


if __name__ == '__main__':
    data_pipeline = DataPipeline()
    data_pipeline.extract_data()
    data_pipeline.load_data()

