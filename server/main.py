from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import uvicorn
import asyncio
from datetime import datetime

from response_engine import ResponseEngine
from portfolio_data import PortfolioData

app = FastAPI(title="Jeremy's Portfolio API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize response engine
response_engine = ResponseEngine()
portfolio_data = PortfolioData()

class ChatRequest(BaseModel):
    message: str
    context: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    intent: str
    timestamp: str
    processing_time_ms: int

@app.get("/")
async def root():
    return {"message": "Jeremy's Portfolio API is running!"}

@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    start_time = datetime.now()
    
    try:
        # Generate response using the engine
        response_data = await response_engine.generate_response(request.message)
        
        end_time = datetime.now()
        processing_time = int((end_time - start_time).total_seconds() * 1000)
        
        return ChatResponse(
            response=response_data["response"],
            intent=response_data["intent"],
            timestamp=datetime.now().isoformat(),
            processing_time_ms=processing_time
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")

@app.get("/api/portfolio/projects")
async def get_projects():
    return portfolio_data.get_projects()

@app.get("/api/portfolio/skills")
async def get_skills():
    return portfolio_data.get_skills()

@app.get("/api/portfolio/experience")
async def get_experience():
    return portfolio_data.get_experience()

@app.get("/api/portfolio/contact")
async def get_contact():
    return portfolio_data.get_contact()

@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
