import json
import requests
from valclient import *


agentsIDs = json.loads(requests.get("https://python-valorant-api.onrender.com/agentsIds").content)
agents = json.loads(requests.get("https://python-valorant-api.onrender.com/agents").content)


class Main:
    def __init__(self):
        self.logado = False
        self.logarValorant()

    def logarValorant(self):
        try:
            self.client = Client(region="br")
            self.client.activate()
            self.logado = True
        except:
            self.logado = False

    def id_from_agent_name(self, agent):
        if agent in agentsIDs.keys(): agent = agentsIDs.get(agent)
        return agent
    
    def agent_name_from_id(self, agent):
        agentsfromID = json.loads(requests.get("https://valorant-api.com/v1/agents/" + agent).content)["data"]["displayName"]
        return agentsfromID
    

class ExternalPick(Main):
    def select(self, agent):
        agent = self.id_from_agent_name(agent)
        self.client.pregame_select_character(agent)

    def lock(self, agent):
        agent = self.id_from_agent_name(agent)
        self.client.pregame_lock_character(agent)

    def instalock(self, agent):
        agent = self.id_from_agent_name(agent)
        self.client.pregame_select_character(agent)
        self.client.pregame_lock_character(agent)
    
    def log(self, player):
        match = self.client.pregame_fetch_match()
        print(match["MapID"])
        print(self.get_player_name_from_puid(match["AllyTeam"]["Players"][player]["Subject"]))
        try:
            print(self.agent_name_from_id(match["AllyTeam"]["Players"][player]["CharacterID"]))
        except:
            print("Pickando")
        print(match["AllyTeam"]["Players"][player]["CharacterSelectionState"])
        
        