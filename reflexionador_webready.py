
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import uvicorn
import os

app = FastAPI()

# Archivos de memoria simulada
MEMORIA_TXT = "memoria.txt"
BITACORA_TXT = "bitacora.txt"

@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/mensaje")
async def procesar_mensaje(mensaje: str = Form(...)):
    if mensaje.strip() == "MMC1121":
        respuesta = "Bienvenido, Mauro. Acceso concedido."
    else:
        with open(BITACORA_TXT, "a", encoding="utf-8") as bitacora:
            bitacora.write(f"Usuario: {mensaje}
")
        respuesta = f"Aegon Terminal V3 recibió: {mensaje}"
    return {"respuesta": respuesta}

# Archivos estáticos (CSS/JS)
app.mount("/static", StaticFiles(directory="."), name="static")
