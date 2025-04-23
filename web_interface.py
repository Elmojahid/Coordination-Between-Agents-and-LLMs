from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
import uvicorn
import json
import os
from pathlib import Path
import asyncio
from project_coordinator import ProjectCoordinator
from specialized_agents import (
    ProjectManagerAgent,
    DeveloperAgent,
    CodeReviewerAgent,
    ArchitectAgent
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialiser le système d'agents
coordinator = ProjectCoordinator()
pm = ProjectManagerAgent("Alice")
developer = DeveloperAgent("Bob", ["Python", "AI", "Web Development"])
reviewer = CodeReviewerAgent("Charlie")
architect = ArchitectAgent("Diana")

# Enregistrer les agents
coordinator.register_agent(pm)
coordinator.register_agent(developer)
coordinator.register_agent(reviewer)
coordinator.register_agent(architect)

# Initialiser le fichier project_state.json s'il n'existe pas
def init_project_state():
    if not os.path.exists("project_state.json"):
        with open("project_state.json", "w", encoding="utf-8") as f:
            json.dump({
                "tasks": [],
                "code_reviews": [],
                "architecture_decisions": []
            }, f, ensure_ascii=False, indent=2)

# Sauvegarder l'état du projet
def save_project_state(state):
    with open("project_state.json", "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

@app.get("/")
async def home(request: Request):
    init_project_state()
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/api/project-state")
async def get_project_state():
    try:
        with open("project_state.json", "r", encoding="utf-8") as f:
            return JSONResponse(json.load(f))
    except FileNotFoundError:
        init_project_state()
        return JSONResponse({
            "tasks": [],
            "code_reviews": [],
            "architecture_decisions": []
        })

@app.post("/api/initiate-task")
async def initiate_task(request: Request):
    try:
        data = await request.json()
        task_description = data.get("description", "")
        priority = data.get("priority", "MEDIUM")
        
        if not task_description:
            raise HTTPException(status_code=400, detail="La description de la tâche est requise")
        
        # Lire l'état actuel
        with open("project_state.json", "r", encoding="utf-8") as f:
            state = json.load(f)
        
        # Créer la nouvelle tâche
        new_task = {
            "task": {
                "description": task_description,
                "priority": priority,
                "architecture_evaluation": await architect.process_with_llm(f"Évaluer l'architecture pour: {task_description}")
            },
            "assignment": await pm.process_with_llm(f"Assigner la tâche: {task_description}"),
            "analysis": await developer.process_with_llm(f"Analyser la tâche: {task_description}"),
            "implementation": await developer.generate_code(task_description)
        }
        
        # Ajouter la tâche à l'état
        state["tasks"].append(new_task)
        
        # Sauvegarder l'état mis à jour
        save_project_state(state)
        
        return {"status": "success", "message": "Tâche créée avec succès"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/review-code")
async def review_code(request: Request):
    try:
        data = await request.json()
        code = data.get("code", "")
        task_description = data.get("task_description", "")
        
        if not code or not task_description:
            raise HTTPException(status_code=400, detail="Le code et la description de la tâche sont requis")
        
        # Lire l'état actuel
        with open("project_state.json", "r", encoding="utf-8") as f:
            state = json.load(f)
        
        # Créer la nouvelle revue
        review_result = await reviewer.process_with_llm(f"Revue du code pour la tâche: {task_description}\nCode:\n{code}")
        
        new_review = {
            "task": task_description,
            "code": code,
            "review": review_result
        }
        
        # Ajouter la revue à l'état
        state["code_reviews"].append(new_review)
        
        # Sauvegarder l'état mis à jour
        save_project_state(state)
        
        return {"status": "success", "review": review_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    init_project_state()
    uvicorn.run(app, host="127.0.0.1", port=8000)
