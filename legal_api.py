#!/usr/bin/env python3
"""
Simple FastAPI server for the legal LLM
Run with: python legal_api.py
Then visit: http://localhost:8000/docs
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import uvicorn
import os

# Global variables for model
model = None
tokenizer = None
device = None

def load_model():
    """Load the trained model"""
    global model, tokenizer, device

    if model is not None:
        return model, tokenizer, device

    model_path = "apple_silicon_models/final_model"

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at {model_path}")

    print("🔧 Loading legal LLM...")
    device = torch.device('mps' if torch.backends.mps.is_available() else 'cpu')

    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    model.to(device)
    model.eval()

    print(f"✅ Model loaded on {device}")
    return model, tokenizer, device

# FastAPI setup
app = FastAPI(
    title="Legal LLM API",
    description="API for generating legal text using trained LLM",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerationRequest(BaseModel):
    prompt: str
    max_length: int = 200
    temperature: float = 0.8
    top_p: float = 0.9
    top_k: int = 50

class GenerationResponse(BaseModel):
    generated_text: str
    prompt: str
    parameters: dict

@app.on_event("startup")
async def startup_event():
    """Load model on startup"""
    load_model()

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Legal LLM API is running",
        "docs": "/docs",
        "generate": "/generate"
    }

@app.get("/health")
async def health():
    """Health check"""
    return {"status": "healthy", "model_loaded": model is not None}

@app.post("/generate", response_model=GenerationResponse)
async def generate_text(request: GenerationRequest):
    """Generate legal text"""
    try:
        # Load model if not loaded
        global model, tokenizer, device
        if model is None:
            model, tokenizer, device = load_model()

        # Validate parameters
        if not request.prompt or not request.prompt.strip():
            raise HTTPException(status_code=400, detail="Prompt cannot be empty")
        if request.temperature < 0.1 or request.temperature > 2.0:
            raise HTTPException(status_code=400, detail="Temperature must be between 0.1 and 2.0")
        if request.max_length < 10 or request.max_length > 1000:
            raise HTTPException(status_code=400, detail="Max length must be between 10 and 1000")

        # Encode prompt
        inputs = tokenizer(request.prompt, return_tensors="pt").to(device)

        # Generate text
        with torch.no_grad():
            outputs = model.generate(
                inputs["input_ids"],
                attention_mask=inputs.get("attention_mask"),
                max_length=request.max_length,
                num_return_sequences=1,
                temperature=request.temperature,
                do_sample=True,
                top_p=request.top_p,
                top_k=request.top_k,
                pad_token_id=tokenizer.eos_token_id,
                repetition_penalty=1.2
            )

        # Decode generated text
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return GenerationResponse(
            generated_text=generated_text,
            prompt=request.prompt,
            parameters={
                "max_length": request.max_length,
                "temperature": request.temperature,
                "top_p": request.top_p,
                "top_k": request.top_k
            }
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Generation failed: {str(e)}")

if __name__ == "__main__":
    port = 9090  # Port between 9000-10000 as requested
    print("🚀 Starting Legal LLM API server...")
    print(f"📖 API docs: http://localhost:{port}/docs")
    print(f"🔗 Health check: http://localhost:{port}/health")
    uvicorn.run(app, host="0.0.0.0", port=port)
