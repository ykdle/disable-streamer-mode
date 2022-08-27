import requests


class Content():
    def __init__(self, Requests, log):
        self.Requests = Requests
        self.log = log

    def get_content(self):
        content = self.Requests.fetch("custom", f"https://shared.{self.Requests.region}.a.pvp.net/content-service/v3/content", "get")
        return content

    def get_latest_season_id(self, content):
        for season in content["Seasons"]:
            if season["IsActive"]:
                self.log(f"retrieved season id: {season['ID']}")
                return season["ID"]

    def get_all_agents(self):
        rAgents = requests.get("https://valorant-api.com/v1/agents?isPlayableCharacter=true").json()
        agent_dict = {}
        agent_dict.update({None: None})
        for agent in rAgents["data"]:
            agent_dict.update({agent['uuid'].lower(): agent['displayName']})
        self.log(f"retrieved agent dict: {agent_dict}")
        return agent_dict
