#version1
# 
# from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# OpenAI API setup in the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, or specify domains for better security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

class TextRequest(BaseModel):
    text: str
    task: str

@app.post("/process_text/")
async def process_text(request: TextRequest):
    prompt_dict = {
        "grammar_correction": "Correct the grammar of the following text:",
        "style_enhancement": "Enhance the style of the following text:",
        "tone_adjustment": "Adjust the tone of the following text:"
    }
    prompt = f"{prompt_dict.get(request.task, '')} {request.text}"

    try:
        # Use the ChatCompletion API
        
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use GPT-4o model
            messages=[
                {"role": "system", "content": "You are a helpful writing assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7,
        )

        # Extract the message content correctly
        result = response.choices[0].message.content.strip()
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

