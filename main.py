import asyncio
from dotenv import load_dotenv
import os
from agent import Agent
from coordinator import Coordinator

async def main():
    # Charger les variables d'environnement (pour la clé API OpenAI)
    load_dotenv()

    # Créer le coordinateur
    coordinator = Coordinator()

    # Créer quelques agents avec différents rôles
    agent1 = Agent("Agent1", "Analyste de données")
    agent2 = Agent("Agent2", "Assistant de recherche")
    agent3 = Agent("Agent3", "Synthétiseur d'information")

    # Enregistrer les agents auprès du coordinateur
    coordinator.register_agent(agent1)
    coordinator.register_agent(agent2)
    coordinator.register_agent(agent3)

    # Exemple de communication entre agents
    coordinator.send_message("Agent1", "Agent2", "Pouvez-vous analyser ces données ?")
    
    # Exemple d'utilisation du LLM par un agent
    response = await agent2.process_with_llm(
        "Comment devrions-nous procéder pour analyser les données reçues ?"
    )
    print(f"\nRéponse du LLM à Agent2: {response}")

    # Exemple de diffusion
    coordinator.broadcast_message("Agent2", "Analyse terminée, voici les résultats!")

    # Exemple de mise à jour des connaissances
    agent2.update_knowledge("analyse_status", "completed")
    print(f"\nStatut de l'analyse pour Agent2: {agent2.get_knowledge('analyse_status')}")

if __name__ == "__main__":
    asyncio.run(main())
