from src.config.config import Config
from src.services.request.api_requestor import ApiRequestor
from src.services.extract.github.utils.parse_event_to_dict import EventsToDict


class GitHubEventsExtractor:
    def __init__(self):
        self.url = Config.GITHUB_API_ORG_URL + Config.COMPANY_NAME + f"/{Config.ENDPOINT}"
        self.response = ApiRequestor(self.url).get_json()
        self.data_pr = []

    def get_events_links(self):
        if len(self.response) > 0:
            return [[repo["events_url"], repo["full_name"]] for repo in self.response]
        else:
            return []

    def get_pull_request_events(self):
        for link, full_name in self.get_events_links():
            response = ApiRequestor(link).get_json()
            for event in response:
                if event["type"] == "PullRequestEvent":
                    self.data_pr.append(EventsToDict.parse_event_to_dict(event, full_name))
        return self.data_pr

