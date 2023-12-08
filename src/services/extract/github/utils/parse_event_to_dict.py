
class EventsToDict:
    @staticmethod
    def parse_event_to_dict(event: dict, full_name: str):
        return {"event_id": event["id"],"actor": event["actor"]["login"],
                "repo": full_name, "repo_id": event["repo"]["id"],
                "action": event["payload"]["action"],
                "id_pull_request": event["payload"]["pull_request"]["id"],
                "action_number": event["payload"]["number"],
                "state": event["payload"]["pull_request"]["state"],
                "closed_at": event["payload"]["pull_request"]["closed_at"],
                "merged_at": event["payload"]["pull_request"]["merged_at"],
                "owner": event["payload"]["pull_request"]["head"]["repo"]["owner"]["login"]
        }