from typing import Dict, List
from agent import Agent

class Coordinator:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def register_agent(self, agent: Agent):
        """Enregistrer un nouvel agent dans le système"""
        self.agents[agent.name] = agent
        print(f"Agent {agent.name} enregistré avec le rôle: {agent.role}")

    def send_message(self, sender_name: str, receiver_name: str, message: str):
        """Envoyer un message d'un agent à un autre"""
        if sender_name in self.agents and receiver_name in self.agents:
            self.agents[receiver_name].receive_message(message, sender_name)
        else:
            print(f"Erreur: Agent non trouvé")

    def broadcast_message(self, sender_name: str, message: str):
        """Diffuser un message à tous les agents sauf l'expéditeur"""
        if sender_name in self.agents:
            for agent_name, agent in self.agents.items():
                if agent_name != sender_name:
                    agent.receive_message(message, sender_name)
        else:
            print(f"Erreur: Agent expéditeur non trouvé")

    def get_agent_list(self) -> List[str]:
        """Obtenir la liste des agents enregistrés"""
        return list(self.agents.keys())
