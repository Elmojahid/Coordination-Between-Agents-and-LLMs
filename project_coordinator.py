from coordinator import Coordinator
from specialized_agents import ProjectManagerAgent, DeveloperAgent, CodeReviewerAgent, ArchitectAgent
from typing import Dict, List
import json

class ProjectCoordinator(Coordinator):
    def __init__(self):
        super().__init__()
        self.project_state = {
            "tasks": [],
            "design_documents": [],
            "code_reviews": [],
            "architecture_decisions": []
        }

    async def initiate_task(self, task_description: str, priority: str):
        """Initier une nouvelle tâche dans le projet"""
        # L'architecte évalue d'abord l'impact technique
        architect = next((agent for agent in self.agents.values() 
                         if isinstance(agent, ArchitectAgent)), None)
        if architect:
            arch_evaluation = await architect.evaluate_architecture(
                f"Impact technique de la tâche: {task_description}"
            )
            
            # Le project manager assigne la tâche
            pm = next((agent for agent in self.agents.values() 
                      if isinstance(agent, ProjectManagerAgent)), None)
            if pm:
                # Trouver le développeur le plus approprié
                developer = next((agent for agent in self.agents.values() 
                                if isinstance(agent, DeveloperAgent)), None)
                if developer:
                    task = {
                        "description": task_description,
                        "priority": priority,
                        "architecture_evaluation": arch_evaluation
                    }
                    assignment = await pm.assign_task(task, developer.name)
                    
                    # Le développeur analyse la tâche
                    analysis = await developer.analyze_task(task_description)
                    
                    self.project_state["tasks"].append({
                        "task": task,
                        "assignment": assignment,
                        "analysis": analysis
                    })
                    
                    return "Tâche initiée avec succès"
        return "Erreur: Agents requis non disponibles"

    async def review_implementation(self, code: str, task_description: str):
        """Demander une revue de code"""
        reviewer = next((agent for agent in self.agents.values() 
                        if isinstance(agent, CodeReviewerAgent)), None)
        if reviewer:
            review = await reviewer.review_code(code, task_description)
            self.project_state["code_reviews"].append({
                "code": code,
                "task": task_description,
                "review": review
            })
            return review
        return "Erreur: Reviewer non disponible"

    def get_project_status(self) -> Dict:
        """Obtenir l'état actuel du projet"""
        return self.project_state

    def export_project_state(self, filename: str):
        """Exporter l'état du projet en JSON"""
        with open(filename, 'w') as f:
            json.dump(self.project_state, f, indent=2)
