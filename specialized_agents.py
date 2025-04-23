from agent import Agent
from typing import List, Dict
import json

class ProjectManagerAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name, "Project Manager")
        self.current_tasks = []
        self.team_availability = {}

    async def assign_task(self, task: Dict, developer_agent: str) -> str:
        prompt = f"""
        En tant que Project Manager, comment devrais-je assigner cette tâche:
        Tâche: {task['description']}
        Priorité: {task['priority']}
        À développeur: {developer_agent}
        """
        response = await self.process_with_llm(prompt)
        self.current_tasks.append({"task": task, "assignee": developer_agent})
        return response

class DeveloperAgent(Agent):
    def __init__(self, name: str, expertise: List[str]):
        super().__init__(name, "Developer")
        self.expertise = expertise
        self.current_task = None

    async def generate_code(self, task_description: str) -> str:
        prompt = (
            f"En tant que développeur expert, générer le code pour la tâche suivante :\n"
            f"{task_description}\n\n"
            f"Le code doit être complet et inclure :\n"
            f"1. Les imports nécessaires\n"
            f"2. La gestion des erreurs\n"
            f"3. Les commentaires explicatifs\n"
            f"4. Les tests unitaires basiques\n"
            f"5. Un exemple d'utilisation\n\n"
            f"Utiliser les meilleures pratiques de développement et les design patterns appropriés.\n"
            f"Répondre uniquement avec le code, sans explications supplémentaires."
        )
        code = await self.process_with_llm(prompt)
        return code

    async def analyze_task(self, task_description: str) -> str:
        prompt = (
            f"En tant que développeur spécialisé en {', '.join(self.expertise)},\n"
            f"fournir une analyse technique détaillée de la tâche suivante :\n"
            f"{task_description}\n\n"
            f"Inclure :\n"
            f"1. Les points techniques clés\n"
            f"2. Les défis potentiels\n"
            f"3. Les solutions proposées\n"
            f"4. Les technologies recommandées\n"
            f"5. Une estimation de l'effort"
        )
        analysis = await self.process_with_llm(prompt)
        return analysis

class CodeReviewerAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name, "Code Reviewer")
        self.review_history = []

    async def review_code(self, code: str, context: str) -> str:
        prompt = f"""
        En tant que reviewer de code, analyse ce code:
        Code: {code}
        Contexte: {context}
        Fournis une revue détaillée en considérant:
        - La qualité du code
        - Les potentiels problèmes
        - Les suggestions d'amélioration
        """
        review = await self.process_with_llm(prompt)
        self.review_history.append({"code": code, "review": review})
        return review

class ArchitectAgent(Agent):
    def __init__(self, name: str):
        super().__init__(name, "System Architect")
        self.design_decisions = {}

    async def evaluate_architecture(self, proposal: str) -> str:
        prompt = f"""
        En tant qu'architecte système, évalue cette proposition:
        {proposal}
        Considère:
        - La scalabilité
        - La maintenabilité
        - Les patterns de conception appropriés
        """
        evaluation = await self.process_with_llm(prompt)
        self.design_decisions[proposal] = evaluation
        return evaluation
