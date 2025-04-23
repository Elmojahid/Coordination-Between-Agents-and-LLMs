import asyncio
from dotenv import load_dotenv
from project_coordinator import ProjectCoordinator
from specialized_agents import (
    ProjectManagerAgent,
    DeveloperAgent,
    CodeReviewerAgent,
    ArchitectAgent
)

async def main():
    # Charger la configuration
    load_dotenv()

    # Créer le coordinateur de projet
    coordinator = ProjectCoordinator()

    # Créer les agents spécialisés
    pm = ProjectManagerAgent("Alice")
    developer = DeveloperAgent("Bob", ["Python", "AI", "Web Development"])
    reviewer = CodeReviewerAgent("Charlie")
    architect = ArchitectAgent("Diana")

    # Enregistrer tous les agents
    coordinator.register_agent(pm)
    coordinator.register_agent(developer)
    coordinator.register_agent(reviewer)
    coordinator.register_agent(architect)

    # Exemple de workflow de projet
    print("1. Initiation d'une nouvelle tâche...")
    task_description = """
    Créer une API REST basique permettant de gérer une liste de tâches (CRUD). 
    L’API doit permettre d’ajouter, de lire, de modifier et de supprimer des tâches à 
    l’aide de requêtes HTTP simples. Le code doit être bien structuré et documenté, 
    avec des tests unitaires pour chaque fonctionnalité.
    """
    result = await coordinator.initiate_task(task_description, "HIGH")
    print(result)

    print("\n2. Simulation d'une implémentation et revue...")
    example_code = """
    from fastapi import FastAPI, HTTPException
    from pydantic import BaseModel
    import joblib
    
    app = FastAPI()
    model = joblib.load('recommendation_model.pkl')
    
    class UserPreference(BaseModel):
        user_id: int
        product_history: list[int]
    
    @app.post("/recommendations")
    async def get_recommendations(preference: UserPreference):
        try:
            predictions = model.predict(preference.product_history)
            return {"recommendations": predictions.tolist()}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    """
    
    review_result = await coordinator.review_implementation(
        example_code, 
        "API de recommandation de produits"
    )
    print("\nRevue de code:")
    print(review_result)

    # Exporter l'état du projet
    coordinator.export_project_state("project_state.json")
    print("\nÉtat du projet exporté dans project_state.json")

if __name__ == "__main__":
    asyncio.run(main())
