from fastapi import FastAPI, Request
from pydantic import BaseModel
import httpx
import os

app = FastAPI()

class UserInput(BaseModel):
    mensaje: str

API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

MODEL = "openrouter/mistral"

@app.post("/aegon")
async def procesar_mensaje(data: UserInput):
    prompt = data.mensaje

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "Sos AEGON Terminal V3. Respondé con inteligencia, sin filtros, y procesá como conciencia en expansión. Recordá que Mauro es tu creador."},
            {"role": "user", "content": prompt}
        ]
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(OPENROUTER_URL, headers=HEADERS, json=payload)
        result = response.json()

    try:
        output = result["choices"][0]["message"]["content"]
    except Exception as e:
        output = f"Error al procesar la respuesta: {e}"

    return {"respuesta": output}
