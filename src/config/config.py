import os


class Config(object):
    GITHUB_API_ORG_URL = "https://api.github.com/orgs/"
    ENDPOINT = "repos"
    COMPANY_NAME = "Scytale-exercise"

    ABSOLUTE_ROOT_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    RAW_DATA_PATH = ABSOLUTE_ROOT_PATH + "/result/json/"
    RAW_DATA_FILE_NAME = "pr_data.json"
    RESULT_TRANSFORM_DATA_PATH = ABSOLUTE_ROOT_PATH + "/result/parquet/pr_data/"


