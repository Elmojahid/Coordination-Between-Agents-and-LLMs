from typing import List, Dict
import os
from dotenv import load_dotenv
import requests

load_dotenv()  # ← Cette ligne est ESSENTIELLE

class DeepseekAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.deepseek.com/v1'

    async def create_chat_completion(self, messages, model="deepseek-chat"):
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            data = {
                'model': model,
                'messages': messages,
                'temperature': 0.7,
                'max_tokens': 1000
            }
            response = requests.post(
                f'{self.base_url}/chat/completions',
                headers=headers,
                json=data
            )
            response.raise_for_status()  # Raise an error for bad responses
            result = response.json()
            
            # Simulate OpenAI-like response structure if needed
            if 'choices' not in result:
                return {
                    'choices': [{
                        'message': {
                            'content': result.get('response', 'No response received')
                        }
                    }]
                }
            return result
        except requests.exceptions.RequestException as e:
            raise Exception(f"Erreur lors de la communication avec Deepseek: {str(e)}")
        except ValueError as e:
            raise Exception(f"Erreur lors du traitement de la réponse: {str(e)}")

# Initialize the Deepseek client
client = DeepseekAPI(api_key=os.getenv('DEEPSEEK_API_KEY'))

class Agent:
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role
        self.messages: List[Dict] = []
        self.knowledge_base = {}

    def receive_message(self, message: str, sender: str):
        """Recevoir un message d'un autre agent"""
        self.messages.append({
            "sender": sender,
            "content": message
        })
        print(f"{self.name} a reçu un message de {sender}: {message}")

    async def process_with_llm(self, prompt: str) -> str:
        """Utiliser le LLM pour traiter une requête"""
        try:
            # Simuler une réponse locale pour le développement
            # Cette partie sera remplacée par l'intégration réelle avec Deepseek
            # quand l'API sera disponible
            simulated_responses = {
                "Project Manager": "Je vais assigner cette tâche à l'équipe de développement.",
                "Developer": "Je vais analyser les exigences et commencer le développement.",
                "Code Reviewer": "Le code semble bien structuré mais nécessite quelques améliorations.",
                "System Architect": "L'architecture proposée est scalable et maintainable."
            }
            
            return simulated_responses.get(self.role, f"En tant que {self.role}, je vais traiter cette tâche.")
            
            # Code pour l'API réelle (temporairement commenté)
            '''response = await client.create_chat_completion(
                messages=[
                    {"role": "system", "content": f"Tu es un agent assistant nommé {self.name} avec le rôle de {self.role}."}, 
                    {"role": "user", "content": prompt}
                ]
            )
            return response['choices'][0]['message']['content']'''
        except Exception as e:
            print(f"Détail de l'erreur: {str(e)}")
            return f"Erreur lors de la communication avec le LLM: {str(e)}"

    def update_knowledge(self, key: str, value: str):
        """Mettre à jour la base de connaissances de l'agent"""
        self.knowledge_base[key] = value

    def get_knowledge(self, key: str) -> str:
        """Récupérer une information de la base de connaissances"""
        return self.knowledge_base.get(key, "Information non trouvée")
